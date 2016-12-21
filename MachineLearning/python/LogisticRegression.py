# coding:utf-8
'''
Logistics Regression 逻辑回归
解决二分类问题
'''
import random
import math

'''
Logistics Regression 模型类
'''
class LogisticsRegression:

    def __init__(self, trainInputs, trainOutputs):
        self.trainInputs = trainInputs;
        self.trainOutputs = trainOutputs;
        # theta0
        self.bias = random.randint(-1,1) # [-1, 1]
        # theta1 .....
        self.weights = []
        for i in range(len(trainInputs[0])):
            self.weights.append(random.randint(-1,1)) #[-1, 1]


    # 开始训练
    def fit(self, echo, learningRate, costFunc='CrossEntropy'):
        for i in range(echo):
            weightGradient = []
            for y in range(len(self.weights)):
                weightGradient.append(0)
            biasGradient = 0
            for j in range(len(self.trainInputs)):
                outputValue = 0
                for z in range(len(self.trainInputs[j])):
                    outputValue += self.weights[z] * self.trainInputs[j][z]
                outputValue += self.bias
                outputValue = 1 / ( 1 + math.exp(-outputValue)) 
                for z in range(len(self.trainInputs[j])):
                    if costFunc == 'CrossEntropy':
                        weightGradient[z] += (self.trainOutputs[j] - outputValue) * self.trainInputs[j][z]
                    elif costFunc == 'RMS':
                        weightGradient[z] += (self.trainOutputs[j] - outputValue) * outputValue * (1 - outputValue) * self.trainInputs[j][z]

                if costFunc == 'CrossEntropy':
                    biasGradient += (self.trainOutputs[j] - outputValue) 
                elif costFunc == 'RMS':
                    biasGradient += (self.trainOutputs[j] - outputValue) * outputValue * (1 - outputValue)
                
            # 更新权重
            for x in range(len(self.weights)):
                self.weights[x] += learningRate * weightGradient[x] / len(self.trainInputs)

            # 更新偏置
            self.bias += learningRate * biasGradient / len(self.trainInputs)

            if i % 100 == 0:
                print "ECHO NUM: ", i, " WITH_ COST: ", biasGradient




    # 预测
    def predict(self, testInputs):
        predictValue = 0
        for i in range(len(testInputs)):
            predictValue += self.weights[i] * testInputs[i]
        predictValue += self.bias
        return 1 / ( 1 + math.exp(-predictValue))





# ======================= 测试代码

random.seed(1)


testTrainInputs = [[0,0,0], [1,1,1], [2,2,2], [0,1,0], [1,1,0], [1,2,3], [2,3,1]]
testTrainOutputs = [1, 1, 1, 0, 0, 0, 0, 0]
logisticsRegression = LogisticsRegression(testTrainInputs,testTrainOutputs)
print logisticsRegression.predict([0,0,0])

logisticsRegression.fit(10000,0.5,costFunc='CrossEntropy')

print logisticsRegression.predict([0,0,0])

correctCount = 0
for i in range(len(testTrainInputs)):
    value = 0
    if logisticsRegression.predict(testTrainInputs[i]) >= 0.5:
        value = 1
    if value == testTrainOutputs[i]:
        correctCount += 1


print "Correct Percent: ", (correctCount / len(testTrainInputs)) * 100, " %"
