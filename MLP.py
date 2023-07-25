import numpy as np
from random import random

class Network:
    def __init__(self,layers_dim):
        self.layers_dim=layers_dim
        self.parameters={}
        self.grads={}
        self.initialize_parameters()
    
    def initialize_parameters(self):
        np.random.seed(3)
        layer_dims=self.layers_dim
        L=len(layer_dims)
        for l in range(1,L):
            self.parameters['W'+str(l)]=np.random.rand(layer_dims[l],layer_dims[l-1])*0.01
            self.parameters['b' + str(l)]=np.zeros((layer_dims[l],1))
    
    def linear_forward(self,A,W,b):
        Z=np.dot(W,A)+b
        cache=(A,W,b)
        return Z,cache

    def linear_activation_forward(self,A_prev,W,b,activation):
        Z, linear_cache = self.linear_forward(A_prev,W,b)
        A, activation_cache = activation(Z)

        cache = (linear_cache,activation_cache)
        return A,cache
    
    def forward_propagate(self,X,parameters):
        caches = []
        A=X
        L=len(parameters)//2
        #RELU para la  capa 1 a la capa L-1
        for l in range(1,L):
            A_prev=A

            A, cache = self.linear_activation_forward(
                A_prev,parameters['W' + str(l)],
                parameters['b' + str(l)],
                activation=self.relu
            )
            caches.append(cache)
        preds,cache=self.linear_activation_forward(
                A,parameters['W' + str(L)],
                parameters['b' + str(L)],
                activation=self.sigmoid
        )
        caches.append(cache)
        return preds,caches
    
    def relu(self,Z):
        A = np.maximum(0,Z)
        return A
    
    def sigmoid(self,Z):
        A=1/(1+np.exp(-Z))
        return A

    def linear_backward(self,dZ,cache):
        A_prev,W,b=cache
        m=A_prev.shape[1]
        dw=np.dot(dZ,cache[0].T)/m
        db=np.squeeze(np.sum(dZ,axis=1,keepdims=True))
        dA_prev=np.dot(cache[1].T,dZ)
        return dA_prev,dw,db
    def linear_activation_backward(self,dA,cache,activation_backward):
        linear_cache,activation_cache=cache
        dZ=activation_backward(dA,activation_cache)
        dA_prev,dW,db=self.linear_backward(dZ,linear_cache)
        return dA_prev,dW,db
    
    def relu_backward(dA,cache):
        Z=cache
        dZ=np.array(dA,copy=True)
        dZ[Z<=0]=0
        return dZ
    
    def sigmoid_backward(dA,cache):
        Z=cache
        s=1/(1+np.exp(-Z))
        dZ=dA*s*(1-s)
        return dZ
    
    def back_propagate(self,preds,Y,caches):
        L=len(caches)
        m=preds.shape[1]
        Y=Y.reshape(preds.shape)

        dpreds= - (Y/preds-[1-Y]/(1-preds))
        current_cache=caches[-1]
        self.grads["dA" + str(L)],self.grads["dW" + str(L)],self.grads["db" + str(L)]=self.linear_backward(sigmoid_backward(
            dpreds,current_cache[1]),current_cache[0]
            )
        for l in reversed(range(L-1)):
            current_cache=caches[l]
            dA_prev_temp,dW_temp,db_temp=self.linear_activation_backward(sigmoid_backward(
                dpreds,current_cache[1]),current_cache[0])
            self.grads["dA" + str(l+1)]=dA_prev_temp
            self.grads["dW" + str(l+1)]=dW_temp
            self.grads["db" + str(l+1)]=db_temp
    def update_parameters(self,parameters,grads,learning_rate):
        L=len(parameters)//2
        for l in range(L):
            parameters["W" + str(l+1)]=parameters["W" + str(l+1)]-learning_rate*grads["dW"]


#arquitectura: 3 entradas, 4 neuronas para cada capa intermedia
#              1 salida
mlp=Network([3,4,4,1])

print("W1 = "+str(mlp.parameters["W1"]))
print("W1 shape = "+str(mlp.parameters["W1"].shape))
print("b1 = "+str(mlp.parameters["b1"]))
print("b1 shape = "+str(mlp.parameters["b1"].shape)+'\n')

print("W2 = "+str(mlp.parameters["W2"]))
print("W2 shape = "+str(mlp.parameters["W2"].shape))
print("b2 = "+str(mlp.parameters["b2"]))
print("b2 shape = "+str(mlp.parameters["b2"].shape)+'\n')

print("W3 = "+str(mlp.parameters["W3"]))
print("W3 shape = "+str(mlp.parameters["W3"].shape))
print("b3 = "+str(mlp.parameters["b3"].shape))
print("b3 shape = "+str(mlp.parameters["b3"].shape)+'\n')

np.random.seed(1)
X=np.random.randn(3,5)
Y=np.asarray([[1,1,1,1,0]]) 
preds,caches=mlp.forward_propagate(X,mlp.parameters)
print("preds = "+ str(preds))   

