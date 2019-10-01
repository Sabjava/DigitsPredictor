from DigitImageClassifier import DigitImageClassifier

SIZE = 100 # number of test records
def load_data():
	"""Return ``image_data`` read from file test.csv 
	into a list of SIZE 2-tuples ``(x, y)``.  
	``x`` is a 784-dimensional list containing the input image.  
	``y`` is a correct digit for ``x``
	lines in the test.csv file have first 784 fields corresponding to the values
	of the image array
	last field corresponds to the correct digit
	this file is generated based on MNIST dataset used for training the model based on
	http://neuralnetworksanddeeplearning.com/chap1.html
	"""

	i = 0
	image_data  = [[0] * SIZE for i in range(2)]
	with open("tests.csv") as lines:
		for line in lines:
			values = line.split(",")
			image_data[1][i] = int(float(values.pop().rstrip()))
			image_data[0][i] = list(map(float, values))
			i = i+1
			if i == SIZE: break
	return image_data

image_data = load_data()

network = DigitImageClassifier(["layer1.csv", "layer2.csv"])

print ("Prediction:\t",  "Probability:\t", "Digit:")

count = 0
total = 0
for i in range(0,SIZE):
	image = image_data[0][i]
	digit_test = image_data[1][i]
	digit, prob = network.predict(image)
	print (digit, "\t\t%.4f\t\t" % prob, digit_test)
	total = total +1
	if (digit == digit_test):
		count = count +1
print ("Predicted: ", count, "Total: ", total, "Accuracy: ", "%.1f"  % (100*count/total))



