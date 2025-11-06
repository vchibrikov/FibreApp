import os
from PIL import Image
from pathlib import Path

def compress_images_multiple_sizes(source_dirs, target_root, sizes=[1024, 512, 256, 128, 64]):

# This Python code defines a function, compress_images_multiple_sizes, whose primary purpose is to 
# recursively find image files within one or more source directories, resize them into multiple square 
# thumbnail/preview sizes, and save the resulting images to an organized output structure.

    supported_extensions = {'.jpeg', '.jpg', '.png'}
    # Use the high-quality LANCZOS resampling filter
    resample_method = Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.LANCZOS

    for source_dir in source_dirs:
        source_dir = Path(source_dir)
        # Walk through all files and subdirectories
        for root, _, files in os.walk(source_dir):
            for file in files:
                ext = Path(file).suffix.lower()
                if ext not in supported_extensions:
                    continue  # Skip files that are not supported images

                src_file_path = Path(root) / file
                
                try:
                    # Open the original image once
                    with Image.open(src_file_path) as img:
                        # Convert to RGB to handle alpha channels and ensure format consistency
                        img_rgb = img.convert("RGB")

                        # Loop through all the desired sizes
                        for size in sizes:
                            # Create a specific path for the current size
                            # e.g., .../output/1024x1024/NdS-II_PAPER_IMG/...
                            rel_path = src_file_path.relative_to(source_dir)
                            target_path = Path(target_root) / f"{size}x{size}" / source_dir.name / rel_path

                            # Ensure the output directory exists
                            target_path.parent.mkdir(parents=True, exist_ok=True)
                            
                            # Resize from the original RGB image for best quality
                            resized_img = img_rgb.resize((size, size), resample=resample_method)
                            
                            # Save as JPEG
                            final_path = target_path.with_suffix('.jpg')
                            resized_img.save(final_path, format='JPEG', quality=90) # Added quality setting
                            
                            print(f"Saved ({size}x{size}): {final_path}")

                except Exception as e:
                    print(f"❌ Failed to process {src_file_path}: {e}")

# --- Example Usage ---
source_folders = ['/path/to/source/folder'] # List of source directories
output_directory = '/path/to/output/directory' # A dedicated root folder is cleaner

# Call the function with the desired list of sizes
compress_images_multiple_sizes(source_folders, output_directory, sizes=[1024, 512, 256, 128, 64])