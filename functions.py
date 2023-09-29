import random
def ReLU(x):
    if x>=0:
        return x
    else:
        return 0
def ReLUderiv(x):
    if x>0:
        return 1
    else:
        return 0
    
def generateRandomList(length):
    z=[]
    for i in range(length):
        z.append(random.random())
    return z

def appendNeuron(inputs, weights, bias):
    x=0
    i=0
    for i in range(len(inputs)):
        x+=inputs[i] * weights[i]
    x+=bias
    return ReLU(x)
    