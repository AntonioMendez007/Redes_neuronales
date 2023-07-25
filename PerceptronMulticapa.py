import numpy as np
import time
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, accuracy_score, mean_squared_error,r2_score
from random import random
from math import exp
from random import randrange
from random import seed
from csv import reader

start = time.time()

# Inicializar la neurona
def initialize_network(n_inputs, n_hidden, n_outputs):
    network = list()
    hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
    network.append(output_layer)
    return network

 #Calculate neuron activation for an input
def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i] * inputs[i]
    return activation

# Acyivación de las neuronas de transferencia
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

# Calcular la derivada de las neuronas de entrada
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

# 7. Update network weights with error
def update_weights(network, row, l_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i - 1]]
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
        neuron['weights'][-1] += l_rate * neuron['delta']

# 8. Train a network for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
    for epoch in range(n_epoch):
        sum_error = 0
        for row in train:
            outputs = forward_propagate(network, row)
            expected = [0 for i in range(n_outputs)]
            expected[row[-1]] = 1
            backward_propagate_error(network, expected)
            update_weights(network, row, l_rate)
        print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))

df = [[2.7550537003,0],
 [1.465489372,2.362125076,1],
 [3.396561688,4.400293529,1],
 [1.38807019,1.850220317,0]]
n_inputs = len(df[0]) - 1
n_outputs = len(set([row[-1] for row in df]))
    

# evaluate algorithm
n_folds = 3

n_hidden = 2

network = initialize_network(n_inputs,n_hidden,n_outputs)
train_network(network, df, 0.1, 20, n_outputs)
for layer in network:
    print(layer)



