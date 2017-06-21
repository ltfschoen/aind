# Purpose: Study Dimensionality of Convolutional Layer changes
# as a function of supplied arguments

from keras.models import Sequential
from keras.layers import Conv2D

# Create Sequential Model
model = Sequential()

# Add Layers to the Convolutional Neural Network (CNN)
model.add(Conv2D(filters=16, 
								 kernel_size=2, 
								 strides=2, 
								 padding='valid', 
    						 activation='relu', 
    						 input_shape=(200, 200, 1)))
model.summary()

# Output
# _________________________________________________________________
# Layer (type)                 Output Shape              Param #   
# =================================================================
# conv2d_1 (Conv2D)            (None, 100, 100, 16)      80        
# =================================================================
# Total params: 80.0
# Trainable params: 80
# Non-trainable params: 0.0
# _________________________________________________________________
# 
# Formula for Number of Parameters in Convolutional Layer
# =======================================================
# 
# Note: 
#  - Params # 	  - number of parameters in the Convolutional Layer depends
#                   on supplied `filters`, `filter_size`, 
#                   `input_shape`
#  - Output Shape - shape of Convolutional Layer
#                   (batch_size, height, width, depth)
#                   
# Defining the following Variables:
#  - K    - number of filters in Convolutional Layer
#  - F    - Height and Width of Convolutional Filters
#  - D_in - depth of Previous Layer
#  
# Now,
# 
# 	K = filters 
# 	F = filter_size
# 	D_in = input_shape (last value in the tuple)
# 	Weights per Filter == F * F * D_in
# 	Total Weights in Convolutional Layer == K * F * F * D_in
# 	Bias Quantity == K (since 1x Bias term per Filter)
# 	Number of Parameters in Convolutional Layer == K * F * F * D_in + K
# 	
# Formula for Shape of a Convolutional Layer
# =======================================================
# 
# Shape depends on supplied values of:
# 	- filter_size
# 	- input_shape
# 	- padding
# 	- stride
# 	
# Define the following Variables
#  - K    - the number of filters in the convolutional layer
#  - F    - the height and width of the convolutional filters
#  - S    - the stride of the convolution
#  - H_in - the height of the previous layer
#  - W_in - the width of the previous layer
#  
# Now,
# 
# 	K = filters 
# 	F = filter_size
# 	S = stride
# 	H_in = first value of input_shape tuple
# 	W_in = second value of input_shape tuple
# 	depth == K (number of filters)
# 	
# If padding = 'same', then spatial dimensions of 
# the convolutional layer are the following:
# 
#   height = ceil(float(H_in) / float(S))
#   width = ceil(float(W_in) / float(S))
#   
# If padding = 'valid', then the spatial dimensions of 
# the convolutional layer are the following:
#
#   height = ceil(float(H_in - F + 1) / float(S))
#   width = ceil(float(W_in - F + 1) / float(S))    
#   