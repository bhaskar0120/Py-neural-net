# Helper functions for Neural network
from matrix import Matrix
import math
def sigmoid(x:Matrix) -> Matrix:
    ''' Sigmoid function '''
    x.perform(lambda x: 1/(1+math.exp(-x)))

def sigmoid_prime(x:Matrix) -> Matrix:
    ''' Derivative of sigmoid function '''
    x.perform(lambda x: x*(1-x))

def relu(x:Matrix) -> Matrix:
    ''' ReLU function '''
    x.perform(lambda x: max(0,x))

def relu_prime(x:Matrix) -> Matrix:
    ''' Derivative of ReLU function '''
    x.perform(lambda x: 1 if x > 0 else 0)
