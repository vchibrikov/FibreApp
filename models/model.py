# Import necessary libraries
import tensorflow as tf
from tensorflow.keras import layers, models, applications, optimizers, losses
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
import tensorflow_addons as tfa # Run: pip install tensorflow-addons (Provides advanced optimizers like AdamW)
import keras_cv # Run: pip install keras-cv
import os

# --- 1. SETUP ---
# Path to the training dataset directory (contains subfolders for each class)
train_dir = "./path/to/train/dir/" # Substituted user-specific path
# Path to the testing/validation dataset directory
test_dir = "./path/to/test/dir/" # Substituted user-specific path
# Directory where the trained model files (.h5 and .tflite) will be saved
model_save_dir = "./path/to/model/save/dir" # Substituted user-specific path and project name
# Image size: 224x224 is standard for EfficientNetB0 and optimized for the target Android app
img_size = (224, 224)
# Batch size for training and validation
batch_size = 32

# Ensure the save directory structure exists
os.makedirs(model_save_dir, exist_ok=True)

# --- 2. DATA LOADING ---
# Load training images from the directory structure
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    train_dir,
    image_size=img_size,
    batch_size=batch_size,
    label_mode='categorical' # Labels are encoded as a one-hot categorical vector
)

# Load testing/validation images
test_ds = tf.keras.preprocessing.image_dataset_from_directory(
    test_dir,
    image_size=img_size,
    batch_size=batch_size,
    label_mode='categorical'
)

# Get the names of the classes (subfolder names) and the total number of classes
class_names = train_ds.class_names
num_classes = len(class_names)

# Optimize data loading performance by prefetching data
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.prefetch(buffer_size=AUTOTUNE)

# Calculate class weights to handle dataset imbalance
# The formula applies a higher weight to less frequent classes.
train_class_counts = {
    class_name: len(os.listdir(os.path.join(train_dir, class_name)))
    for class_name in class_names
}
total = sum(train_class_counts.values())
class_indices = {name: idx for idx, name in enumerate(class_names)}
class_weight = {
    class_indices[class_name]: total / (len(class_names) * count)
    for class_name, count in train_class_counts.items()
}
# class_weight will be passed to model.fit()

# --- 3. STATE-OF-THE-ART DATA AUGMENTATION ---
# Define a sequential model for on-the-fly data augmentation
data_augmentation = tf.keras.Sequential([
    # Rescaling is implicitly handled by the EfficientNet preprocessing layer inside the base_model
    # Randomly flip images horizontally
    layers.RandomFlip("horizontal"),
    # Randomly rotate images by up to 15% of 360 degrees
    layers.RandomRotation(factor=0.15),
    # Randomly zoom images (in/out)
    layers.RandomZoom(height_factor=(-0.2, 0.2), width_factor=(-0.2, 0.2)),
    # Randomly adjust contrast
    layers.RandomContrast(factor=0.2),
], name="data_augmentation")

# --- 4. BUILD MODEL (Transfer Learning) ---
# Use EfficientNetB0 as the base for transfer learning, optimized for 224x224 inputs
base_model = applications.EfficientNetB0(
    input_shape=(224, 224, 3), # Expected image dimensions (Height, Width, Color Channels)
    include_top=False, # Exclude the default fully connected layers
    weights='imagenet' # Initialize weights with pre-trained ImageNet values
)
# Freeze the base model layers initially (only train the new head)
base_model.trainable = False

# Construct the final model: Augmentation -> Base Model -> New Classification Head
model = models.Sequential([
    # Apply data augmentation to the input images
    data_augmentation,
    # The pre-trained convolutional base
    base_model,
    # Reduce dimensionality using Global Average Pooling
    layers.GlobalAveragePooling2D(),
    # New hidden dense layer for classification
    layers.Dense(256, activation='relu'),
    # Normalize activations to speed up training
    layers.BatchNormalization(),
    # Regularization to prevent overfitting
    layers.Dropout(0.4),
    # Output layer: one node per class with softmax for probability distribution
    layers.Dense(num_classes, activation='softmax')
])

# --- 5. COMPILE WITH ADVANCED OPTIMIZER & LOSS ---
initial_compiler_settings = {
    # AdamW is a robust optimizer (Adam with weight decay regularization)
    "optimizer": tfa.optimizers.AdamW(weight_decay=1e-5),
    # Use Categorical Crossentropy with Label Smoothing (0.1) for better regularization
    "loss": losses.CategoricalCrossentropy(label_smoothing=0.1),
    # Track Accuracy and Precision metrics
    "metrics": ['accuracy', tf.keras.metrics.Precision()]
}
model.compile(**initial_compiler_settings)

# Callbacks for better training control
# Stop training if validation loss doesn't improve for 5 epochs
early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
# Reduce the learning rate if validation loss plateaus
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=2, min_lr=1e-7)

# --- 6. TWO-STAGE TRAINING (Standard practice for fine-tuning) ---

# -- STAGE 1: Train the classifier head (Feature Extraction) --
# The base model is frozen (base_model.trainable = False)
print("--- STAGE 1: Training the top layers (Classifier Head) ---")
history = model.fit(
    train_ds,
    validation_data=test_ds,
    epochs=15, # Train for a fixed number of epochs
    callbacks=[early_stop, reduce_lr],
    class_weight=class_weight
)

# -- STAGE 2: Unfreeze and fine-tune (Adjusting the convolutional base) --
print("\n--- STAGE 2: Fine-tuning the full model ---")
# Unfreeze the base model completely
base_model.trainable = True

# Strategically freeze the bottom layers (for low-level feature extraction)
# and only fine-tune the top 30 layers (for task-specific features)
for layer in base_model.layers[:-30]:
    layer.trainable = False

# Re-compile with a very low learning rate for gentle fine-tuning
fine_tune_compiler_settings = {
    # Use a much smaller learning rate to prevent catastrophic forgetting
    "optimizer": tfa.optimizers.AdamW(learning_rate=1e-5, weight_decay=1e-6),
    "loss": losses.CategoricalCrossentropy(label_smoothing=0.1),
    "metrics": ['accuracy', tf.keras.metrics.Precision()]
}
model.compile(**fine_tune_compiler_settings)

# Continue training from the last epoch of Stage 1
history_fine_tune = model.fit(
    train_ds,
    validation_data=test_ds,
    epochs=25,
    callbacks=[early_stop, reduce_lr],
    class_weight=class_weight,
    initial_epoch=history.epoch[-1] # Start epoch count from where Stage 1 left off
)

# --- 7. FINAL EVALUATION AND SAVING ---
print("\n--- Evaluating final fine-tuned model ---")
loss, acc, prec = model.evaluate(test_ds)
print(f"Final loss: {loss:.4f}, accuracy: {acc:.4f}, precision: {prec:.4f}")

# Save the model in the standard Keras format (.h5)
model_path = os.path.join(model_save_dir, "model.h5")
model.save(model_path)
print(f"Saved .h5 model to: {model_path}")

# Convert the Keras model to the TFLite format for mobile deployment (Android app)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model (.tflite)
tflite_path = os.path.join(model_save_dir, "model.tflite")
with open(tflite_path, "wb") as f:
    f.write(tflite_model)
print(f"Saved .tflite model to: {tflite_path}")
