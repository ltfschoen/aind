# References:
# - Keras Multi-Layer Perceptron https://github.com/fchollet/keras/blob/master/examples/mnist_mlp.py
# - Keras Sequential https://keras.io/getting-started/sequential-model-guide/

import numpy as np
from keras.utils import np_utils
import tensorflow as tf
tf.python_io.control_flow_ops = tf

# Set random seed
np.random.seed(42)

# Our data
X = np.array([[0,0],[0,1],[1,0],[1,1]]).astype('float32')
y = np.array([[0],[1],[1],[0]]).astype('float32')

# Setup Keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten

# Convert labels to categorical one-hot encoding the output
y = np_utils.to_categorical(y)

# Create Sequential Model with Sequential() wrapper for neural network model
# to provide common functions like fit(), evaluate(), compile()
xor = Sequential()

# Add Keras Layers (neural network layers including
# fully connected (i.e. Flatten(), Dense()),
# max pool, and activation layers) using function add()

# 1st Layer - Add Hidden Layer with input data of size: 8 and nodes (dimensions): 2
#   Note: Only required to set input dimensions for first layer since Keras infers shape of remainder
xor.add(Dense(32, input_dim=2))

# 2nd Layer - Add sigmoid activation function layer (i.e. relu, sigmoid, softmax, tanh)
xor.add(Activation("sigmoid"))

# 3rd Layer - Add fully connected layer with 2 nodes (dimensions) since output has 2 classes
#   Note: 3rd layer (last layer output of model) takes output of 1st/2nd Layer
#         and sets output dimensions
xor.add(Dense(2))

# 4th Layer - Add sigmoid activation function layer
xor.add(Activation("softmax"))

# Configure the learning process prior to Training the model.
# Compile the previously built model
#   - Loss Function (objective for model to try to minimise)
#                               - i.e. categorical_crossentropy, mean_squared_error
#                               - Reference: https://keras.io/losses/
#   - Optimiser                 - i.e. adam, rmsprop, adagrad, adadelta, adamax, nadam, tfoptimizer, sgd
#                               - Reference: https://keras.io/optimizers/
#   - Metrics (to evaluate)     - i.e. accuracy
#                               - Note: Custom metric function optional
#                                   - Reference: https://keras.io/getting-started/sequential-model-guide/
xor.compile(loss="categorical_crossentropy", optimizer="adam", metrics = ['accuracy'])

# Print the model architecture
# xor.summary()

# Training the model on Numpy arrays of input data and labels using the fit() function
#   - Epoch (Note: Keras 1 nb_epoch; Keras 2 epochs)
#   - Verbose
history = xor.fit(X, y, epochs=1000, verbose=3)

# Scoring and evaluate the model
score = xor.evaluate(X, y)
print("\nAccuracy: ", score[-1])

# Checking the predictions
print("\nPredictions:")
print(xor.predict_proba(X))