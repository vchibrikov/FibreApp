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

<table> <thead> <tr> <th colspan="2">Description of the project</th> </tr> </thead> 
  
<tbody> <tr> <td>Project title:</td> <td>Research and dissemination of knowledge about the content of pectin, cellulose, and dietary fiber in fruits and vegetables</td> </tr>
  
<tr> <td>Project no:</td> <td>NdS-II/SP/0258/2023/01</td> </tr> </tbody>

<tbody> <tr> <td>Founding source:</td> <td>Minister of Science and Higher Education of Poland, “Science for Society II” program
</td> </tr> <tr> 

<td> Project manager:</td> <td>Prof. D.Sc. Artur Zdunek, corr. member of PAS</td> </tr> </tbody>

<tbody> <tr> <td>Data managers:</td> <td>Prof. D.Sc. Justyna Cybulska; Ph.D. Vadym Chibrikov
</td> </tr> 
  
<tr> <td>Keywords:</td> <td>Cellulose; hemicellulose; pectin; dietary fiber; Android application; iOS application; machine learning; image classification model</td> </tr> </tbody> 

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

<td>Sample description:</td> <td>model.tflite was generated with model.py; model.mlmodel was generated in CreateML; model.py is a home-made Python code for the creation of a TensorFlow Lite model with a transfer learning methodology </td> </tr> </tbody>

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

<tbody> <tr> <td>Datafile name:</td> <td>In .tflite and .mlmodel files, classes are numerically encoded to represent the following species: 1. Apple; 2. Apricot; 3. Asparagus; 4. Avocado; 5. Banana; 6. Broad bean; 7. Green bean; 8. Red beetroot; 9. Bell pepper; 10. Blueberry; 11. Broccoli; 12. White cabbage; 13. Carrot; 14. Celery; 15. Champignon; 16. Sweet cherry; 17. Chinese cabbage; 18. Chokeberry; 19. Corn; 20. Cucumber; 21. Red grapes; 22. Dill; 23. Doughnut peach; 24. Eggplant; 25. Grapefruit; 26. Iceberg lettuce; 27. Kiwifruit; 28. Leek; 29. Lemon; 30. White grapes; 31. Lime; 32. Mango; 33. Melon; 34. Onion; 35. Orange; 36. Parsley (leaves); 37. Parsley (root); 38. Peach; 39. Pear; 40. Pineapple; 41. Plum; 42. Potato; 43. Pumpkin; 44. Radish; 45. Raspberry; 46. Strawberry; 47. Sweet potato; 48. Tomato; 49. Watermelon; 50. Zucchini</td> </tr> <tr> 

<td>Datafile format:</td> <td>.tflite; .mlmodel; .py</td> </tr> </tbody> <table>



























