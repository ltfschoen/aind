# Purpose: Study Dimensionality of Maximum Pooling Layers

from keras.models import Sequential
from keras.layers import MaxPooling2D

model = Sequential()

# pool_size - height and width of the pooling window
# strides - vertical and horizontal stride. default to pool_size.
# padding - 'valid' or 'same'. default is 'valid'.
# NOTE: It is possible to represent both pool_size and strides 
# as either a number or a tuple.
model.add(MaxPooling2D(pool_size=2, 
											 strides=2, 
											 input_shape=(100, 100, 15)))
model.summary()

# Output
# _________________________________________________________________
# Layer (type)                 Output Shape              Param #   
# =================================================================
# max_pooling2d_1 (MaxPooling2 (None, 50, 50, 15)        0         
# =================================================================
# Total params: 0.0
# Trainable params: 0.0
# Non-trainable params: 0.0
# _________________________________________________________________