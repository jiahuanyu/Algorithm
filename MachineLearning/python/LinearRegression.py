# coding:utf-8
'''
Linear Regression 线性回归
简单线性回归，一元线性回归
多远线性回归
'''

import random

class LinearRegression:
	def __init__(self, trainInputs, trainOutputs):
		self.trainInputs = trainInputs
		self.trainOutputs = trainOutputs
		self.weights = []
		self.bias = random.randint(-1,1)
		for i in range(len(trainInputs[0])):
			self.weights.append(random.randint(-1,1))


	def fit(self, echo, learningRate):
		for i in range(echo):
			weightGradient = []
			for y in range(len(self.weights)):
				weightGradient.append(0)
			biasGradient = 0
			for j in range(len(self.trainInputs)):
				outputValue = 0
				for z in range(len(self.trainInputs[j])):
					outputValue += self.trainInputs[j][z] * self.weights[z]
				outputValue += self.bias

				for z in range(len(self.trainInputs[j])):
					weightGradient[z] += (self.trainOutputs[j] - outputValue) * self.trainInputs[j][z]

				biasGradient += (self.trainOutputs[j] - outputValue)


			# 更weights
			for x in range(len(self.weights)):
				self.weights[x] += learningRate * weightGradient[x] / len(self.trainInputs)

         	# 更新偏置
			self.bias += learningRate * biasGradient / len(self.trainInputs)

			if i % 100 == 0:
				print "ECHO NUM: ", i, " WITH_ COST: ", biasGradient

				
	def predict(self, testInputs):
		predictValue = 0
		for i in range(len(self.weights)):
			predictValue += self.weights[i] * testInputs[i]
		return predictValue + self.bias


# ======================= 测试代码

random.seed(1)

testTrainInputs = [[0,0], [1,1], [2,2], [3,3]]
testTrainOutputs = [0, 1, 2, 3]

linearRegression = LinearRegression(testTrainInputs, testTrainOutputs)

print linearRegression.predict([1,1])

linearRegression.fit(10000, 0.001)

print linearRegression.predict([10,10])
