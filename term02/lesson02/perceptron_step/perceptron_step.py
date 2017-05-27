import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def stepFunction(t):
    """
    Return Step
    """
    if np.mean(t) >= 0:
        return 1
    return 0

def prediction(X, W, b):
    """
    Returns Dot Product of X and W
    """

    # Reshape as say (99,1) instead of (99,)
    X = np.reshape(X,(len(X),1))
    W = W.T
    return stepFunction((np.matmul(X,W)+b)[0])

def perceptronStep(X, y, W, b, learn_rate = 0.01):
    """
    Perceptron Step Algorithm to move Boundary Line closer to
    misclassified Points.
    :param X: data
    :param y: labels
    :param W: weights (array)
    :param b: bias
    :param learn_rate: alpha
    :return: W and b
    """
    for i in range(len(X)):

        # Prediction Equation
        y_hat = prediction(X[i],W,b)

        # If Positive Labelled Point misclassified in Negative area
        # (i.e. Inputs - Predicted Label
        if y[i]-y_hat == 1:

            # wi + α * xi
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b += learn_rate

        # If Negative Labelled Point misclassified in Positive area
        elif y[i]-y_hat == -1:

            # wi - α * xi
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate
        # Otherwise labelled point classified correctly so do nothing
    return W, b

def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 25):
    """
    Run Perceptron algorithm repeatedly on the dataset.
    Returns some Boundary Lines obtained from iterations to plot.
    Adjust Learning Rate and Epochs to see different results.
    """

    # Note: .T access the attribute T (transpose) of the object (a NumPy array)
    # https://stackoverflow.com/questions/5741372/syntax-in-python-t
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
    return boundary_lines

dataset_location_local = "data.csv"
dataset_file = Path(dataset_location_local)
df = pd.read_csv(dataset_location_local, nrows=None)

# Add missing dataset labels
dataset_labels = "X1,X2,y"
df.columns = [str(label) for label in dataset_labels.split(',') if label]
X = np.array([df['X1'], df['X2']])

# List of Tuples returned
res = trainPerceptronAlgorithm(X, df['y'], 0.01, 25)
print(res)

# Plot the list of Tuples returned
x_val = [x[0] for x in res]
y_val = [x[1] for x in res]

# Plot the returned Boundary Lines
plt.plot(x_val,y_val, 'go') # use '-' for line

X1_0 = df.loc[df['y'] == 0, 'X1']
X1_1 = df.loc[df['y'] == 1, 'X1']
X2_0 = df.loc[df['y'] == 0, 'X2']
X2_1 = df.loc[df['y'] == 1, 'X2']

# Plot Input Data
plt.plot(X1_0, X2_0, 'bo')
plt.plot(X1_1, X2_1, 'ro')
plt.show()