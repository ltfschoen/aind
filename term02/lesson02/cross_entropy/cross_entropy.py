import numpy as np

def cross_entropy(Y, P):
    """
    Function takes as input two lists Y, P, such as
    (0,0,1) and (0.8,0.7,0.1) and returns float
    corresponding to their cross-entropy.

    Cross-Entropy = - (m ∑ j=1) yj * ln(pj) + (1 - yj) * ln(1 - pj)
    """

    Y = np.array(Y)
    P = np.array(P)
    m = np.arange(len(Y))

    ce_elem = []
    for j in m:
        ce_next = -(Y[j] * np.log(P[j]) + (1 - Y[j]) * np.log(1 - P[j]))
        ce_elem.append(ce_next)
    ce = np.sum(ce_elem)
    return ce

    # # ANSWER:
    # Y = np.float_(Y)
    # P = np.float_(P)
    # return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))


Y = [0, 0, 1]
P = [0.8, 0.7, 0.1]
ce = cross_entropy(Y, P)
print(ce)