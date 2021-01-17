import numpy as np


def AND1(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    temp = x1 * w1 + x2 * w2
    if temp <= theta:
        return 0
    elif temp > theta:
        return 1


# AND function that implements bias and weight
def AND2(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
