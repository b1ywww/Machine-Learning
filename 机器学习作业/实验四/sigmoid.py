import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.arange(0.,10., 0.5)
y = sigmoid(x)

plt.plot(x, y)