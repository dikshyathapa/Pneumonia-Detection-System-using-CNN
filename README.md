# Pneumonia-Detection-System-using-CNN
By using chest X-ray images , pneumonia can be detected by using convolution neural networks.
By using chest X-ray images ,pneumonia detection can be done by using convolution neural network. I have created the model using convolutional Neural Network (CNN) that detects pneumonia with a good value of accuracy. Datasets were preprocessed, normalized, augmented and further trained and tested the large amount of data obtained. CNN different layers were performed to extract the image features. In 20 epochs, when validation loss is at lowest, we saved the model and downloaded it. Then, we deploy that model into our pneumonia detection website where User can upload a Chest X-ray images. 

This trained model helps us detect whether a patient is suffering from pneumonia or the result is normal. The model type that we used in this project is “sequential” which is the easiest way to build a model in keras. It allows to build a model layer by layer. After all data are loaded and preprocessing is done convolution neural network (CNN) is defined. Kernel size is a size of our filter for our convolution. Firstly, a convolution layer is used with input of 62*62 size of image which extracts features from the image or parts of an image. Max pooling layer is used as the second layer of the network that reduces the dimensionality of each feature to focus on the most important elements. There are several rounds of convolution and max pooling used. A fully connected layer that takes a flattened form of the features identified in the previous layers, and uses them to make a prediction about the image. Dense layer is a layer type we used in for our output layer. Finally, two dense layer is used and the input is given to the final fully connected layer which results in two classes. also evaluated the confusion matrix to see how accurate our model is. Pneumonia Detection using Convolution Neural Network focuses on detecting pneumonia with the help of chest X-ray images. In this Machine Learning project, I build a pneumonia detection system. This system is used to detect whether a person has pneumonia or not based on an X-ray image of their chest. This project is also proposed to analyze the different kinds of pre-existing models and their tools for detecting a disease from radiology. Our system takes input as an image and detect if the person has pneumonia or not

![image](https://user-images.githubusercontent.com/113717229/201525342-212ea179-5085-4008-9997-c123d3dc2dc0.png)








![image](https://user-images.githubusercontent.com/113717229/201525401-d9508aa2-556e-43a9-a874-e769e0577d39.png)




![image](https://user-images.githubusercontent.com/113717229/201525434-5ef65525-ea83-43df-a31d-9404ccb6ca5d.png)





![image](https://user-images.githubusercontent.com/113717229/201525454-5a05ec90-6ee9-4f40-8e96-2a04e487fcec.png)

