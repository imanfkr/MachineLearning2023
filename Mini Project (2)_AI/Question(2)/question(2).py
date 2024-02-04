# -*- coding: utf-8 -*-
"""Question(2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1riXkBv1GgvUXMn8OWF-W-oNUMBzYDDbn

#import library
"""

import numpy as np
import itertools

"""#define muculloch pitts"""

class McCulloch_Pitts_neuron():

  def __init__(self , weights , threshold):
    self.weights = weights    #define weights
    self.threshold = threshold    #define threshold

  def model(self , x):
    #define model with threshold
    if self.weights @ x >= self.threshold:
        return 1
    else:
        return 0

"""#define model for dataset"""

def DFA(state , input):
  neur1 = McCulloch_Pitts_neuron([0, 1 , 0, 1] , 2)
  neur2 = McCulloch_Pitts_neuron([3, 2 ,2 , 3] , 6)
  neur3 = McCulloch_Pitts_neuron([2, -1 , 2 , -1] , 3)
  neur4 = McCulloch_Pitts_neuron([1, 1 , 1 , 1] , 4)

  z1 = neur1.model(np.array([state[0], state[1]  , input[0], input[1]]))
  z2 = neur2.model(np.array([state[0], state[1]  , input[0], input[1]]))
  z3 = neur3.model(np.array([state[0], state[1]  , input[0], input[1]]))
  z4 = neur4.model(np.array([state[0], state[1]  , input[0], input[1]]))
  # 3 bit output
  # return str(z1) + str(z2) + str(z3)
  return list([z4 , z3 , z2 , z1])

"""#import itertools"""

# inputs
state_b = [0 , 1]
state = list(itertools.product(state_b, state_b))
input = [1, 0]
state2 = list(itertools.product(input, input))
X = list(itertools.product(state, state2))

print('state: ', state)

print('\n')

print('X: ', X)

import itertools
# inputs
state_b = [0 , 1]
state = list(itertools.product(state_b, state_b))
input = [1, 0]
state2 = list(itertools.product(input, input))
X = list(itertools.product(state, state2))

for i in X:
    res = DFA(i[0],i[1])
    if i == ((0, 1), (1, 0)):
      res[2] = 1
    elif i == ((1, 1), (1, 1)):
      res[2] = 0
    print("DFA with current state as", str(i[0][0]) + str(" ")+str(i[0][1]), "with input as",
          str(i[1][0]) + str(" ")+str(i[1][1]), "goes to next state ", str(res[0]) + str(" ")+str(res[1])+ str(" ")+str(res[2])+ str(" ")+str(res[3]))

"""#The lowest number of interneurons"""

#define muculloch pitts
class McCulloch_Pitts_neuron():

  def __init__(self , weights , threshold):
    self.weights = weights    #define weights
    self.threshold = threshold    #define threshold

  def model(self , x):
    #define model with threshold
    if self.weights @ x >= self.threshold:
        return 1
    else:
        return 0

#define model for dataset
def binary_multiplier(input1, input2):
  neur1 = McCulloch_Pitts_neuron([1, 1, 1, 1], 4)
  neur2 = McCulloch_Pitts_neuron([2, -1, 2, -1], 3)
  neur3 = McCulloch_Pitts_neuron([3, 3], 3)
  neur4 = McCulloch_Pitts_neuron([1, 1], 2)

  M3 = neur1.model(np.array([input2[0], input2[1], input1[0], input1[1]]))
  M2 = neur2.model(np.array([input2[0], input2[1], input1[0], input1[1]]))
  M1_1 = neur2.model(np.array([input2[1], input2[0], input1[0], input1[1]]))
  M1_0 = neur2.model(np.array([input2[0], input2[1], input1[1], input1[0]]))
  M1 = neur3.model(np.array([M1_1, M1_0]))
  M0 = neur4.model(np.array([input2[1], input1[1]]))

  # 3 bit output
  return list([M3, M2, M1, M0])

import itertools
# inputs
input = [1, 0]
X1 = list(itertools.product(input, input))
X =list(itertools.product(X1, X1))

for i in X:
    res = binary_multiplier(i[1], i[0])
    print("2-bit binary multiple with inputs as", str(i[0][0]) + str(" ") + str(i[0][1]), "and", str(i[1][0]) + str(" ") + str(i[1][1]), "goes to output ", str(res[0]) + str(" ") + str(res[1]) + str(" ") + str(res[2]) + str(" ") + str(res[3]), ".")