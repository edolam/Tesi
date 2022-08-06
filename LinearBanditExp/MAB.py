
import numpy as np
import math

t = 1  # number of rounds
T = 10  # numbers of rounds
L = 10  # ||a|| <= L
theta_stimato = [1, 0.5, 0.5] #np.array([])  theta
A = [] #collector of arm
num_arms = 0 #number of arms
W = [] #distribution of probability to play arms
N = [] #number of times an arm is played

class theta():
    vector = np.array([])
    best_arm = -1

    def __init__(self, param):
        self.vector = param
        i = 0
        best = -5
        while i < num_arms:
            tmp = np.dot( A[i].arm_vector, np.transpose(self.vector))
            if best < tmp:
                best = tmp
                self.best_arm = i


class arm():
    arm_vector = np.array([])

    def __init__(self, vector):
        self.arm_vector = vector
        global num_arms, A
        A.append(self)
        W.append(0)
        N.append(0)
        num_arms +=1

    def pull_arm(self):
        return np.dot(self.arm_vector, np.transpose(theta_stimato)) + np.random.normal(0, 1)

    def norm(self):
        return np.linalg.norm(self.arm_vector)

def design_matrix(w):
    V=[]
    i= 0
    while i < num_arms:
      b = [A[i].arm_vector]
      a = np.swapaxes(b, 0, 1)
      ris = np.matmul(a, b) * w[i]
      if (i == 0):
        V = ris
      else:
        V += ris
      i+=1
    return V

def norm_2_mat(x, V):
  b = [x]
  a = np.swapaxes(b, 0, 1)
  ris = np.sqrt(np.matmul(np.matmul(b,V),a))
  return ris[0][0]
