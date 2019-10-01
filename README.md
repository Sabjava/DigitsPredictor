# DigitsPredictor

#### DigitImageClassifier.py 
Implementation of handwritten digits image classifier based on multilayer perceptron model as in [1]

The parameters of the model are:

* Input layer: an image array dimension 784 (28x28x1 grayscale image)
* Hidden layer: 30 neurons
* Output layer: 10 neurons

Model was trained as  decribed in [1], weights and biases were saved in the CSV files: 
* layer1.csv - hidden layer 
* layer2.csv - output layer

Last column in the files corresponds to the biases, the rest of the columns are weights

Model uses sigmoid activation function
  
#### testDigitImageClassifier.py 
Script  to test DigitImageClassifier.
Test cases are read from CSV file and generated from MNIST data [2].

First 784 fileds of a record correspond to the image array, last digit is a digit label of the image

[1] http://neuralnetworksanddeeplearning.com/chap1.html

[2] http://yann.lecun.com/exdb/mnist/
