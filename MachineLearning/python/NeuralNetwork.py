# coding:utf-8
import math
import random


LEARNING_RATE = 0.005

'''
属性包括error, inputs, netValue, outputValue, weights, bias
netValue = weights * inputs
outValue = actionFunciton(netValue)
'''
class Neuron:

 

    def __init__(self, bias, weights):
        self.bias = bias
        self.weights = weights
        self.outputValue = 0

    def calculate_output(self, inputs):
        self.inputs = inputs
        self.calculate_netValue()
        self.outputValue = self.activation_function()
        return self.outputValue

    def calculate_netValue(self):
        total = 0
        for i in range(len(self.inputs)):
            total += self.inputs[i] * self.weights[i]
        self.netValue = total + self.bias

    def activation_function(self):
        return 1 / (1 + math.exp(-self.netValue))

    def calculate_error(self, neurons, target, position):
        if len(neurons) > 0:
            total = 0
            for i in range(len(neurons)):
                total += neurons[i].weights[position] * neurons[i].error
            self.error = self.outputValue * (1 - self.outputValue) * total
        else:
            self.error = (target - self.outputValue)   # self.outputValue * (1 - self.outputValue) * (target - self.outputValue)     第一个是交叉熵代价函数， 第二个是方差代价函数
        # print self.error

    def update_weights(self, neurons, training_inputs):
        if len(neurons) == 0:
            for i in range(len(self.weights)):
                self.weights[i] += (LEARNING_RATE * self.error * training_inputs[i])
        else:
            for i in range(len(self.weights)):
                self.weights[i] += (LEARNING_RATE * self.error *  self.inputs[i]) # self.error * neurons[i].outputValue)  前一个的outputValue其实就是这个neuron的input

    def update_bias(self):
        self.bias += (LEARNING_RATE * self.error)


class NeuronLayer:

    def __init__(self, num_neuron, bias, pervious_num_neuron):
        self.bias = bias if bias else random.random()
        self.neurons = []
        weights = []
        for i in range(pervious_num_neuron):
            weights.append(random.random())
        for i in range(num_neuron):
            self.neurons.append(Neuron(self.bias, weights))

    def feed_forward(self, inputs):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.calculate_output(inputs))
        return outputs

    def get_outputs(self):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.outputValue)
        return outputs


class NeuronNetwork:

    def __init__(self, layers):
        self.layers = []
        pervious_num_neuron = 0
        for i in range(len(layers)):
            self.layers.append(NeuronLayer(layers[i], 0.5, pervious_num_neuron))
            pervious_num_neuron = layers[i]

    def feed_forward(self, inputs):
        for i in range(1, len(self.layers)):
            self.layers[i].feed_forward(inputs)
            inputs = self.layers[i].get_outputs()
        return inputs

    # 训练
    def fit(self, training_inputs, training_outputs):
        for z in range(len(training_inputs)):
            self.feed_forward(training_inputs[z])

            temp = self.layers[::-1]
            for i in range(len(temp) - 1):
                for j in range(len(temp[i].neurons)):
                    if i == 0:
                        temp[i].neurons[j].calculate_error([], training_outputs[z][j], j)
                    else:
                        temp[i].neurons[j].calculate_error(temp[i - 1].neurons, [], j)
            for i in range(1, len(self.layers)):
                for j in range(len(self.layers[i].neurons)):
                    if i == 1:
                        self.layers[i].neurons[j].update_weights([], training_inputs[z])
                        self.layers[i].neurons[j].update_bias()
                    else:
                        self.layers[i].neurons[j].update_weights(self.layers[i - 1].neurons, [])
                        self.layers[i].neurons[j].update_bias()


    def predict(self,inputs):
    	print self.feed_forward(inputs)



random.seed(1)
nn = NeuronNetwork([2, 10, 1])
print 'Before Train'
nn.predict([0,0])
nn.predict([1,1])
nn.predict([1,0])
nn.predict([0,1])
for i in range(100000):
	nn.fit([[0, 0], [1, 1], [1, 0], [0, 1]], [[1], [1], [0], [0]])
print 'Aftet Train'
nn.predict([0,0])
nn.predict([1,1])
nn.predict([1,0])
nn.predict([0,1])

	



