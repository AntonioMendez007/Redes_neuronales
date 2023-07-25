
from math import exp
from random import seed
from random import random
import numpy as np
import time
import pandas as pd
from sklearn import linear_model
from random import random
from math import exp
from random import randrange
from random import seed
from csv import reader
import time

start = time.time()


# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
    network = list()
    hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
    network.append(output_layer)
    return network
 
# Calculate neuron activation for an input
def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i] * inputs[i]
    return activation
 
# Transfer neuron activation
def transfer(activation):
 return 1.0 / (1.0 + exp(-activation))
 
# Forward propagate input to a network output
def forward_propagate(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = transfer(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs
 
# Calculate the derivative of an neuron output
def transfer_derivative(output):
    return output * (1.0 - output)
 
# Backpropagate error
def backward_propagate_error(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = list()
        if i != len(network)-1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += (neuron['weights'][j] * neuron['delta'])
                errors.append(error)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(expected[j] - neuron['output'])
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])
 
#Update network weights with error
def update_weights(network, row, l_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i - 1]]
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
        neuron['weights'][-1] += l_rate * neuron['delta']
 
# Train a network for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
    for epoch in range(n_epoch):
        sum_error = 0
        for row in train:
            outputs = forward_propagate(network, row)
            expected = [0 for i in range(n_outputs)]
            #expected[row[-1]] = 1
            backward_propagate_error(network, expected)
            update_weights(network, row, l_rate)
        print('>epoch=%d, lrate=%.3f, error=%.8f' % (epoch, l_rate, sum_error))

 
# Test training backprop algorithm
'''
for i in range(len(dataset[0])-1):
    str_column_to_float(dataset, i)
'''
#seed(1)

#leer dataset
#df = pd.read_csv("xor.csv")
'''
df = [[0,0,0,2],
[0,0,1,1],
[0,1,0,2],
[0,1,1,1],
[1,0,0,2],
[1,0,1,1],
[1,1,0,2],
[1,1,1,1]
     ]
'''
df=[[-1,-1,-1],
[-1,1,1],
[1,-1,1],
[1,1,-1]
]
# evaluate algorithm

n_inputs = len(df[0]) - 1
n_outputs = len(set([row[-1] for row in df]))

network = initialize_network(3, 2, 1)
train_network(network, df, 0.033, 51, n_outputs)
for layer in network:
 print(layer)

print("Tiempo de ejecucion:")
end = time.time()
print(end - start)
