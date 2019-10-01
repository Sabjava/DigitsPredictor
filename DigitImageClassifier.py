import math    

class Neuron:
	def __init__(self, bias,weights):		
		self.bias = bias
		self.weights = weights

class Layer:
	def __init__(self, file):
	## parses a CSV file with weights and biases (first position in the record)
	## converts string values to floats and initialises neurons of the layer
		self.neurons  = []
		with open(file) as lines:
			for line in lines:
				values = line.split(",")
				weights =[]
				bias = float(values[0])
				for i in range(1,len(values)):
					weights.append(float(values[i]))				
				neuron = Neuron(bias, weights)
				self.neurons.append(neuron)

	def process_image (self, image):
		"""Return the output array of the layer given an image array is input."""		
		if len(image)!= len (self.neurons[0].weights):
			raise ValueError ("Input image length does not match model weights:" , 
						len(image), " vs ", len (self.neurons[0].weights))
		out = []
		
		for neuron in self.neurons:
			result=0
			i=0
			for weight in (neuron.weights):
				result += weight * image[i]
				i = i+1
			result += neuron.bias
			out.append(result)
		out = self.activate(out)
		return out 

	def activate(self,x):
		# sigmoid activation function
		result = []
		for i in range (0,len(x)):
			sigmoidCell = 1 / (1 + math.e ** -x[i])
			result.append(sigmoidCell)
		return result;

class DigitImageClassifier:
	def __init__(self, files):
		self.layers = []
		for file in files:
			self.layers.append (Layer(file))
	
	def predict(self, image):
		for l in self.layers:		
			image = l.process_image(image)
		max_value = max(image)
		max_index = image.index(max_value)
		return (max_index, max_value)



		 
	