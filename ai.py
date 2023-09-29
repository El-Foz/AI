import random, functions
from itertools import chain
from numpy import load

data = load('mnist.npz')
layer1weights, layer2weights, outputLayerWeights=[], [], []

for i in range(16):
    layer1weights.append(functions.generateRandomList(784))
    layer2weights.append(functions.generateRandomList(16))
for i in range(10):    
    outputLayerWeights.append(functions.generateRandomList(16))

inputNum=random.randint(0, 60_000)
mnist = data.files
input = data["x_train"][inputNum]
layer1 = []
layer2 = []
outputLayer=[]
bias=1

input=list(chain.from_iterable(input))
for l in input:
    input[l]=int(input[l])
i=0
for i in range(16):
    layer1.append(functions.appendNeuron(input, layer1weights[i], bias))
for i in range(16):
    layer2.append(functions.appendNeuron(layer1, layer2weights[i], bias))
for i in range(10):
    outputLayer.append(functions.appendNeuron(layer2, outputLayerWeights[i], bias))
n=[0, -1]
output=-1
for i in range(10):
    if outputLayer[i]>n[0]:
        n[0]=outputLayer[i]
        n[1]=i
        output=i
print(output)
