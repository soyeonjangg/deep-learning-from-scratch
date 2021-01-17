import numpy as np


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array(
        [-0.5, -0.5]
    )  # the only diff between AND is that weight and bias are different
    b = 0.7
    tmp = np.sum(x, w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
