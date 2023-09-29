import random, functions
from itertools import chain
from numpy import load

data = load('mnist.npz')
layer1weights, layer2weights, outputLayerWeights=[], [], []

for i in range(16):
    layer1weights.append(functions.generateRandomList(784))
    layer2weights.append(functions.generateRandomList(16))
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
print (layer2)
output = None