# DigitsPredictor

### DigitImageClassifier.py 
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
  
### testDigitImageClassifier.py 
Script  to test DigitImageClassifier.
Test cases are read from CSV file and generated from MNIST data [2].

First 784 fileds of a record correspond to the image array, last digit is a digit label of the image

[1] http://neuralnetworksanddeeplearning.com/chap1.html

[2] http://yann.lecun.com/exdb/mnist/


The code uses Python 3.7. To run the code
```
  git clone https://github.com/Sabjava/DigitsPredictor.git
  cd DigitsPredictor/
  gunzip *gz
  python testDigitImageClassifier.py
 ```
Output of the code is
```
Svetlanas-MacBook-Air:DigitsPredictor sab$ python testDigitImageClassifier.py 
Prediction:	 Probability:	 Digit:
4 		0.9998		 4
0 		1.0000		 0
9 		0.9997		 9
1 		0.9993		 1
3 		0.0930		 1
2 		0.9996		 2
4 		0.9964		 4
3 		1.0000		 3
2 		0.9996		 2
9 		0.0258		 7
3 		0.9987		 3
8 		0.9978		 8
6 		0.9996		 6
9 		0.9290		 9
0 		0.9518		 0
5 		0.9997		 5
6 		0.9999		 6
0 		1.0000		 0
7 		0.9995		 7
6 		0.9992		 6
1 		1.0000		 1
8 		0.9999		 8
7 		0.8352		 7
9 		0.9999		 9
3 		0.9999		 3
9 		0.9992		 9
8 		0.9988		 8
5 		1.0000		 5
5 		0.2361		 9
3 		0.9998		 3
3 		0.9999		 3
0 		0.9997		 0
7 		0.9999		 7
4 		0.9990		 4
9 		0.9896		 9
8 		0.9995		 8
0 		0.9999		 0
9 		0.9994		 9
4 		0.9980		 4
1 		0.9968		 1
4 		1.0000		 4
4 		0.9986		 4
6 		1.0000		 6
0 		0.9999		 0
4 		0.9756		 4
5 		1.0000		 5
6 		1.0000		 6
1 		0.9821		 1
0 		0.8976		 0
0 		0.9999		 0
1 		0.7205		 1
7 		0.9993		 7
1 		1.0000		 1
6 		0.9996		 6
3 		1.0000		 3
0 		0.9992		 0
2 		0.9744		 2
1 		0.9649		 1
1 		0.9746		 1
7 		0.9989		 7
8 		0.0256		 9
0 		0.9998		 0
2 		1.0000		 2
6 		1.0000		 6
7 		1.0000		 7
8 		0.9945		 8
3 		0.9943		 3
9 		0.9950		 9
0 		0.9997		 0
4 		0.9988		 4
6 		1.0000		 6
7 		0.9992		 7
4 		0.9948		 4
6 		1.0000		 6
8 		1.0000		 8
0 		0.9998		 0
7 		0.9998		 7
8 		0.9999		 8
3 		0.9998		 3
1 		0.9938		 1
5 		0.9986		 5
7 		0.9997		 7
1 		0.9992		 1
7 		1.0000		 7
1 		1.0000		 1
1 		0.9747		 1
6 		1.0000		 6
3 		0.9998		 3
0 		0.9970		 0
2 		0.9905		 2
9 		1.0000		 9
3 		0.9954		 3
1 		1.0000		 1
1 		0.9948		 1
0 		0.9999		 0
4 		1.0000		 4
9 		0.9838		 9
2 		0.9914		 2
0 		0.9986		 0
0 		0.9997		 0
Predicted:  96 Total:  100 Accuracy:  96.0
```
