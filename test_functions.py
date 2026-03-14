import numpy as np

def f1_poly5(x):
    return x**5 - 5*x**3 + 4*x + 1

def f2_sin_neg2(x):
    return 1 / (np.sin(x)**2)

def f3_exp_decay(x):
    return np.exp(-x**2)


def exact_values():
    return {
        'f1': 2**6/6 - 5*2**4/4 + 4*2**2/2 + 2,
        'f2': 1/np.tan(0.5) - 1/np.tan(2),
        'f3': 0.886226925452758,
    }
