# Food Mnist solution


## About Food Mnist

- Food-MNIST is a dataset with 10 food categories, with 5,000 images. 
- For each
class, 125 manually reviewed test images are provided as well as 375 training images.
- All images were
rescaled to have a maximum side length of 512 pixels.
- The dataset has only 4 classes.


Each training and test example is assigned to one of the following labels:
- 0 : apple pie
- 1 : baby back ribs
- 2 : baklava
- 3 : beef carpaccio

## Library used

List of libraries mainly used 

- Keras
- Numpy
- Matplotlib
- Seaborn 
- Pandas
- Tensorflow 

## Dataset Exploration 

- Reading image data
- Exploration of image data
- Visualizing 

## Implementing using CNN

### Creating a 2 hidden layer neural network 
- Using activation function relu and sigmoid where relu in the hidden layer and and sigmoid in output layer
- Cross validating multiple times to see the accuracies but relu in the hidden layer and and sigmoid in output layer gives best results 

#### Implementing by increasing no of layers
- By increasing no of layers and using relu in the hidden layer and and sigmoid in output layer gives the better accuracy
- Cross validating with different activation functions used in different layer but gives poor accuracy

#### Dropout 
- Used Dropout after every layer except output layer
- It is improving the accuracy 

#### Callbacks 
- Here different checkpoints are used like ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
- It basically save the model in a directory and let it run until it finds the best model




