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

# One-hot encoding the output
y = np_utils.to_categorical(y)

# Create Sequential Model with Sequential() wrapper for neural network model
# to provide common functions like fit(), evaluate(), compile()
xor = Sequential()

# Add Keras Layers (neural network layers including fully connected,
# max pool, and activation layers) using function add()

# 1st Layer - Add NN Layer with input data of size: 8 and nodes (dimensions): 2
#   Note: Only required to set input dimensions for first layer since Keras infers shape of remainder
#   Hint: This next line is where you can change the size of the first hidden layer, it's current size is 8
xor.add(Dense(8, input_dim=2))

# 2nd Layer - Add sigmoid activation layer
#   Hint: This next line is where you can change the activation function to "relu"
xor.add(Activation("sigmoid"))

# 3rd Layer - Add fully connected layer with 2 nodes (dimensions)
#   Note: 3rd layer (last layer output of model) takes output of 1st/2nd Layer
#         and sets output dimensions
xor.add(Dense(2))

# 4th Layer - Add sigmoid activation layer
xor.add(Activation("sigmoid"))

# Compile the previously built model
#   - Loss Function             - categorical_crossentropy
#   - Optimiser                 - adam
#   - Metrics (to evaluate)     - accuracy
xor.compile(loss="categorical_crossentropy", optimizer="adam", metrics = ['accuracy'])

# Print the model architecture
# xor.summary()

# Fit the model
#   - Epoch (Note: Keras 1 nb_epoch; Keras 2 epochs)
#   - Verbose
history = xor.fit(X, y, epochs=10, verbose=0)

# Scoring and evaluate the model
score = xor.evaluate(X, y)
print("\nAccuracy: ", score[-1])

# Checking the predictions
print("\nPredictions:")
print(xor.predict_proba(X))