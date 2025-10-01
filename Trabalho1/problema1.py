import math
import numpy as np
import matplotlib.pyplot as plt

# C = 80e^(-2t)+20e^(-0.1^x) = 10 -> C(x)= 80e^(-2t)+20e^(-0.1^x)-10
def f(x):
    return 80*math.exp(-2*x)+20*math.exp(-0.1**x)-10

def df(x):
    return -160*math.exp(-2*x)+20*math.exp((-0.01)**x)*((-0.01)**x)*math.log(-0.01)

