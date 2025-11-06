# FibreApp: Mobile machine learning tool for fruit and vegetable fiber content

FibreApp is a repository of Pyhton code, Tensorflow and CoreML models for machine learning image classification.

Repository created for the project under the program of the Minister of Science and Higher Education of Poland titled "Science for Society II".

Project number - NdS-II/SP/0258/2023/01.

Funding amiunt - 1 000 000 PLN.

Total project value - 1 000 000 PLN.

More information on the project: www.fibreapp.pl

For any additional issue, please contact v.chibrikov@ipan.lublin.pl

Download FibreApp in App Store (iOS): https://apps.apple.com/pl/app/fibreapp/id6747246858?l=en

Download FibreApp in Google Play (Android): https://play.google.com/store/apps/details?id=ipan.lublin.pl.fibreapp&hl=en

Download image dataset for machine learning: https://doi.org/10.5281/zenodo.17369912

FibreApp Android code repository: https://github.com/vchibrikov/android_fibreapp.git

FibreApp iOS code repository: 

FibreApp image dataset: https://github.com/vchibrikov/images_fibreapp

<table> <thead> <tr> <th colspan="2">Description of the project</th> </tr> </thead> 
  
<tbody> <tr> <td>Project title:</td> <td>Research and dissemination of knowledge about the content of pectin, cellulose, and dietary fiber in fruits and vegetables</td> </tr>
  
<tr> <td>Project no:</td> <td>NdS-II/SP/0258/2023/01</td> </tr> </tbody>

<tbody> <tr> <td>Founding source:</td> <td>Minister of Science and Higher Education of Poland, “Science for Society II” program
</td> </tr> <tr> 

<td> Project manager:</td> <td>Prof. D.Sc. Artur Zdunek, corr. member of PAS</td> </tr> </tbody>

<tbody> <tr> <td>Data managers:</td> <td>Prof. D.Sc. Justyna Cybulska <br>Ph.D. Vadym Chibrikov
</td> </tr> 
  
<tr> <td>Keywords:</td> <td>Cellulose <br>Hemicellulose <br>Pectin <br>Dietary fiber <br>Android application <br>iOS application <br>Machine learning <br>Image classification model</td> </tr> </tbody> 

<thead> <tr> <th colspan="2">Institution</th> </tr> </thead> 

<tbody> <tr> <td>Facility name:</td> <td>Institute of Agrophysics, Polish Academy of Sciences </td> </tr> <tr> 

<td> Facility division:</td> <td>Department of Microstructure and Mechanics of Biomaterials</td> </tr> </tbody>

<tbody> <tr> <td>Facility address:</td> <td>Doświadczalna 4, 20-290 Lublin, Poland </td> </tr> 
  
<tr> <td>Facility URL:</td> <td>www.ipan.lublin.pl</td> </tr> </tbody> <table>

## models

<thead> <tr> <th colspan="2">models dataset – general information</th> </tr> </thead> 

<tbody> <tr> <td>Dataset name:</td> <td>models</td> </tr> <tr> 

<td>Dataset description:</td> <td>The dataset contains both Image Feature Print V1-based (iOS) and EfficientNetB0-based (Android) models, as well as code to generate EfficientNetB0-based model</td> </tr> </tbody>

<thead> <tr> <th colspan="2">models dataset – saample information</th> </tr> </thead> 

<tbody> <tr> <td>Sample name:</td> <td>model.tflite; model.mlmodel; model.py</td> </tr> <tr> 

<td>Sample type:</td> <td>Machine learning models (model.tflite; model.mlmodel); Python code (model.py) </td> </tr> </tbody>

<td>Sample description:</td> <td>model.tflite was generated with model.py <br>model.mlmodel was generated in CreateML <br>model.py is a home-made Python code for the creation of a TensorFlow Lite model with a transfer learning methodology </td> </tr> </tbody>

<thead> <tr> <th colspan="2">models dataset – datafiles information</th> </tr> </thead> 

<tbody> <tr> <td>Datafile name:</td> <td>In .tflite and .mlmodel files, classes are numerically encoded to represent the following species: <br>1. Apple <br>2. Apricot <br>3. Asparagus <br>4. Avocado <br>5. Banana <br>6. Broad bean <br>7. Green bean <br>8. Red beetroot <br>9. Bell pepper <br>10. Blueberry <br>11. Broccoli <br>12. White cabbage <br>13. Carrot <br>14. Celery <br>15. Champignon <br>16. Sweet cherry <br>17. Chinese cabbage <br>18. Chokeberry <br>19. Corn <br>20. Cucumber <br>21. Red grapes <br>22. Dill <br>23. Doughnut peach <br>24. Eggplant <br>25. Grapefruit <br>26. Iceberg lettuce <br>27. Kiwifruit <br>28. Leek <br>29. Lemon <br>30. White grapes <br>31. Lime <br>32. Mango <br>33. Melon <br>34. Onion <br>35. Orange <br>36. Parsley (leaves) <br>37. Parsley (root) <br>38. Peach <br>39. Pear <br>40. Pineapple <br>41. Plum <br>42. Potato <br>43. Pumpkin <br>44. Radish <br>45. Raspberry <br>46. Strawberry <br>47. Sweet potato <br>48. Tomato <br>49. Watermelon <br>50. Zucchini</td> </tr> <tr> 

<td>Datafile format:</td> <td>.tflite; .mlmodel; .py</td> </tr> </tbody> <table></table>

## supporting_code

<table><thead> <tr> <th colspan="2">supporting_code dataset – general information</th> </tr> </thead> 

<tbody> <tr> <td>Dataset name:</td> <td>supporting_code</td> </tr> <tr> 

<td>Dataset description:</td> <td>Dataset contains home-made Python codes for handling image batches for model training</td> </tr> </tbody>

<thead> <tr> <th colspan="2">supporting_code dataset – saample information</th> </tr> </thead> 

<tbody> <tr> <td>Sample name:</td> <td>rand_filename_gen.py; <br>batch_compress.py; <br>batch_split.py; <br>batch_merge.py; <br>batch_clean.py </td> </tr> <tr> 

<td>Sample type:</td> <td>Python code</td> </tr> </tbody>

<td>Sample description:</td> <td>Dataset is a compilation of a five Python hardcoded scripts for handling large image datasets:
<br>rand_filename_gen.py – script assigns new random filenames for the whole files in directory, without changing directory structure. Crucial for copying camera data.
<br>batch_compress.py – script compresses images to a desired sizes, working with a batch, and not changing its structure. Crucial for data storage, as well as for limiting calculation efforts for model creation.
<br>batch_split.py – script splits dataset by creating another one, with the same structure. Crucial for splitting data on train, validation, and test datasets.
<br>batch_merge.py – script restores split datasets to the respective folders. Crucial for further batch data handling.
<br>batch_clean.py – script cleans path yet preserving its structure. Crucial after batch_merge.py to remove duplicate data.
</td> </tr> </tbody>

<thead> <tr> <th colspan="2">supporting_code dataset – datafiles information</th> </tr> </thead> 

<td>Datafile format:</td> <td>.py</td> </tr> </tbody> <table>

# Usage of FibreApp application

## Requirement
- iOS > 15.0
- Android > 10.0

## Installation
FibreApp can be installed for both:
- iOS: https://apps.apple.com/pl/app/fibreapp/id6747246858?l=en
- Android (https://play.google.com/store/apps/details?id=ipan.lublin.pl.fibreapp&hl=en

![fig_1](https://github.com/user-attachments/assets/48b0fcbe-62cc-40b4-9b58-f0e8e48b08c3)
**Fig.1.** FibreApp overview of the components and activities. Subsequent screenshots represent app view controllers: a) app icon appearance on a desktop; b) Main menu view controller; c) About view controller; d) Localization view controller; e) Manual search view controller; f) Camera search view controller; g) View more view controller.

The app is composed of seven principal view controllers, supported by view controller subclasses and data handling subclasses:
- Main menu view controller (Fig.1b): This facet facilitates user interaction with the subsequent view controllers – with information data (About view controller; Fig.1c), localization settings (Localization view controller; Fig.1d), manual information search (Manual search view controller; Fig.1e), and machine learning-powered livestream image classification (Camera search view controller; Fig.1f);
- Localization view controller: acts as a view controller for a dedicated language selection interface. Upon view loading, it configures the table view data and delegate sources and retrieves the currently selected language code from the persistent storage. The table presents a hardcoded array of language options, using cell configuration to display the language name and render a checkmark accessory on the row corresponding to the active language code. User interaction via row selection triggers an update to the selected language code property, persists the new code property to persistent storage for application-wide consistency, and subsequently reloads the table to update the checkmark location. In turn, every subsequent view controller checks the language code loaded and retrieves the necessary user-facing text by implementing string localization, referencing key-value pairs stored within the dedicated strings resource files for the English, Polish, and Ukrainian locales.
- About view controller executes three primary tasks: setting up the static user interface elements (like logo image and text views); configuring tap gesture recognizers on the logo for interactive linking; retrieving the language code property and fetching the localized text.
- Manual search view controller: manages a searchable, localized list of species data. Upon appearing, the view controller initiates a refresh by retrieving the user's selected language code and fetching the complete, sorted, and localized species data into the array via a shared data manager singleton. Here, the display updating method dynamically manages the displayed species array based on the current state of the search bar: if the user is actively typing, it performs a case-insensitive filter against the localized name property of each species; otherwise, it displays all species. Finally, the segue method is implemented to pass the selected object, its data list, and the active language code to the subsequent View more view controller (Fig.1g) for detailed display.
- Camera search view controller: while loading, it immediately sets up the device's camera and displays the live video feed as the screen's background. For the first setup, access confirmation is required. As the video streams, the code continuously captures frames and sends them to an image classification machine learning model (for Android, a static solution with a single frame capture was applied). Then, the model analyzes the frames to identify the fruit or object in view. Once a class is recognized, the view controller updates the labels to show the following class label, as well as some initial values (pectin, cellulose, and hemicellulose content). All text displayed on the screen is instantly localized based on the active language code property. When the class was detected, a View more button appears, tapping on which redirects the user to the View more view controller.
- View more view controller: designed to receive the list object (which holds all the data for the class selected in Manual search view controller or class detected in Camera search view controller) and the active language code. While being received, data is localized according to the active language code.
