# FaceMask-Detection


A simple project to learn more about face detection in python. This project aims to detect whether or not an individual is wearing a mask and alert him/her. With so many people infected worldwide, the Covid-19 pandemic shows no signs of abating. As a permanent solution is yet to be found, lockdowns remain the only way to slow its spread. However, the lockdowns are also pushing major economies to the brink. Living through a pandemic is strange. Most of us have never been asked to make sacrifices like this before -- staying home and limiting contact with others. All that disruption can make people anxious. And for some, that includes  ignoring the novel coronavirus altogether and carrying on as though it's business as usual. Despite repeated pleas from public health and government officials to stay at home and slow the spread of Covid-19, many people just won't. Although there are few basic requirements for which people are helpless and they have to get out of their homes. Many things can’t be stopped like the patients who have to go through medical procedures once in a week or people from small towns who need to buy food themselves due to lack of online services. What we can do is just follow certain precautions and guidelines which can help us to survive this pandemic.
The Face Mask Detection System can be used at airports to detect travelers without masks. Face data of travelers can be captured in the system at the entrance. If a traveler is found to be without a face mask, their picture is sent to the airport authorities so that they could take quick action.
Using Face Mask Detection System, Hospitals can monitor if their staff is wearing masks during their shift or not. If quarantine people who are required to wear a mask, the system can keep an eye and detect if the mask is present or anyone who enters the hospital should be wearing a mask.
The Face Mask Detection System can be used at office premises to detect if employees are maintaining safety standards at work.  While entering any general stores or supermarket, there can be a camera scan at the entrance and only those customers wearing masks  will be allowed to enter.

## LBPH
For this project, a LBPH classifier is used. In this method we characterize each image in the dataset locally, and when a new unknown image is provided, we perform some analysis on it and compare the result to each of the images in the dataset. The way which we analyse the images is by characterizing the local patterns in each location in the image. 



## Files Description
1) HaarCascade: It is an Object Detection Algorithm used to identify faces in an image or a real time video. It is used to train the model.
2) resizedTrainingImages: If you wish to resize any particular image from the data set, the set of code present in resizeImages.ipynb will be useful. Some of the training images were resized and kept in this folder.
3) TestImages: This folder contains a set of images used to test the result.
4) trainingImages: It contains two folders containing the mask and no mask data set images collected from various sources like Kaggle and Google images.
5) Video: You can create your own data set by using the code present in this folder by clicking your images.
6) faceRecognition.ipynb and faceRecognition.py: Contains same code, use the file format which runs properly on your IDE. The code contains the algorithm to use Haar Cascade and train through LBPH classifiers.
7) tester.ipynb: Contains the main code, where data is trained and tested. It also contains the additional feature to alert users and test results are available for both saved and live images.
8) VideoTester.ipynb: This set of code tests the live image and alerts them.
9) Face Mask Detection.pptx: A presentation, describing the project.
10) trainingData.yml: The trained data. This file cannot be uploaded due to 25 mb+ size but can be created from the code present in tester.ipynb


