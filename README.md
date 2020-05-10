# Introduction
This project was created as and assignment for an internship. It predicts the variety of wine based on text reviews

# Dependecies
* Python 3.7.7
* Pandas 1.0.3
* Keras 1.1.0
* Scikit-learn 0.22.1
* Tensorflow 2.1.0

# Dataset
* The train-dev set consisted of 82657 examples  
![TrainData](/Images/TrainData.png)  

* The test set consisted of 20665 examples  
![TestData](/Images/TestData.png)  

20% of the Train set was used as a dev set.  
The CSV files are availabe in the Data Folder  

# Model Description
I used a pretrained 50D glove vector and a doube layered LSTM followed by a softmax dense unit consisting of 28 units to classify in the 28 different variety of wine available
