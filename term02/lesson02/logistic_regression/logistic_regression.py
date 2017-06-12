import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

import numpy as np
# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_prime(x):
    """
    Calculate Sigmoid Function Derivative
    using Quotient Formula shown in
    Lesson 2 Part 21
    """
    return sigmoid(x)*(1-sigmoid(x))
def prediction(X, W, b):
    return sigmoid(np.matmul(X,W)+b)
def error_vector(y, y_hat):
    return [-y[i]*np.log(y_hat[i]) - (1-y[i])*np.log(1-y_hat[i]) for i in range(len(y))]
def error(y, y_hat):
    ev = error_vector(y, y_hat)
    return sum(ev)/len(ev)

# TODO: Fill in the code below to calculate the gradient of the error function.
def dErrors(X, y, y_hat):
    """
    Result should be a list of three lists:
    First list should contain gradient (partial derivatives) with respect to w1
    Second list should contain gradient (partial derivatives) with respect to w2
    Third list should contain gradient (partial derivatives) with respect to b
    """
    DErrorsDx1 = [X[i][0]*(y[i]-y_hat[i]) for i in range(len(y))]
    DErrorsDx2 = [X[i][1]*(y[i]-y_hat[i]) for i in range(len(y))]

    DErrorsDb = [y[i]-y_hat[i] for i in range(len(y))]

    return DErrorsDx1, DErrorsDx2, DErrorsDb

# TODO: Fill in the code below to implement the gradient descent step.
def gradientDescentStep(X, y, W, b, learn_rate = 0.01):
    """
    Receive inputs: data X, labels y, weights W (as array), and bias b.
    Calculate prediction, gradients.
    Uses them to update Weights and Bias W, b, then return W and b.
    Error e is calculated and returned for plotting.
    """
    # TODO: Calculate the prediction
    y_hat = prediction(X, W, b)
    errors = error_vector(y, y_hat)

    # TODO: Calculate the gradient
    derivErrors = dErrors(X, y, y_hat)

    # TODO: Update the weights
    W[0] += sum(derivErrors[0])*learn_rate
    W[1] += sum(derivErrors[1])*learn_rate
    b += sum(derivErrors[2])*learn_rate
    return W, b, sum(errors)

#    # This calculates the error
#    e = error(y, y_hat)
#    return W, b, e

def trainLR(X, y, learn_rate = 0.01, num_epochs = 100):
    """
    Runs perceptron algorithm repeatedly on the dataset,
    Returns a few of the boundary lines obtained in the iterations for plotting.
    Try changing learning rate and the num_epochs and see results plotted below.
    """

    print("X type: ", X.shape) # (2, 99)
    print("y type: ", y.shape) # (99,)
    X = X.T # convert to shape (99, 2)

    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    # Initialize the weights randomly
    W = np.array(np.random.rand(2,1))*2 -1
    b = np.random.rand(1)[0]*2 - 1
    # These are the solution lines that get plotted below.
    boundary_lines = []
    errors = []
    for i in range(num_epochs):
        # In each epoch, we apply the gradient descent step.
        W, b, error = gradientDescentStep(X, y, W, b, learn_rate)

        y_tuple = (-W[0]/W[1], -b/W[1])

        x = np.linspace(-1,1)
        line = -W[0]/W[1] * x -b/W[1]

        # Plot the Boundary Lines
        plt.plot(x, line, 'g-')

        boundary_lines.append((-W[0]/W[1], -b/W[1]))
        errors.append(error)
    return boundary_lines, errors

dataset_location_local = "data.csv"
dataset_file = Path(dataset_location_local)
df = pd.read_csv(dataset_location_local, nrows=None)

# Add missing dataset labels
dataset_labels = "X1,X2,y"
df.columns = [str(label) for label in dataset_labels.split(',') if label]
X = np.array([df['X1'], df['X2']])
y = np.array(df['y'])

plt.ylim((-1,1))

# List of Tuples returned
res, err = trainLR(X, y, 0.01, 25)
print(res)
print(err)

# Plot the list of Tuples returned
x_val = [x[0] for x in res]
y_val = [x[1] for x in res]

X1_0 = df.loc[df['y'] == 0, 'X1']
X1_1 = df.loc[df['y'] == 1, 'X1']
X2_0 = df.loc[df['y'] == 0, 'X2']
X2_1 = df.loc[df['y'] == 1, 'X2']

# Plot Input Data
plt.plot(X1_0, X2_0, 'ro')
plt.plot(X1_1, X2_1, 'bo')
plt.show()