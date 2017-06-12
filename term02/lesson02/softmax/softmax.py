import numpy as np

def softmax(L):
    """
    Softmax Function used to convert Score outputs
    from Linear Function (list of numbers) into Probabilities,
    and returns list of values given by the Softmax function.
    It takes Exponential of all Scores to ensure they are
    positive numbers to solve problems with 3+ classes
    (Multi-class Classification), whereas 2 class
    problems only need to use the Sigmoid Function.

    Softmax Function:

        P(class i) = e^Zi / (e^Z1 + ... + e^Zn)

        - where n is quantity of classes
        - where Zi is output Score from Linear Model for class i
    """
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result