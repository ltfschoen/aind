from keras.models import Sequential
from keras.layers import Conv2D

model = Sequential()
model.add(Conv2D(filters=32, 
								 kernel_size=3, 
								 strides=2, 
								 padding='same', 
    						 activation='relu', 
    						 input_shape=(128, 128, 3)))
model.summary()

# Output
# _________________________________________________________________
# Layer (type)                 Output Shape              Param #   
# =================================================================
# conv2d_1 (Conv2D)            (None, 64, 64, 32)        896       
# =================================================================
# Total params: 896.0
# Trainable params: 896
# Non-trainable params: 0.0
# _________________________________________________________________
# 
# Formula for Number of Parameters in Convolutional Layer
# =======================================================
# 
# Number of Parameters in Convolutional Layer 
# == K * F * F * D_in + K
# == 32 * 3 * 3 * 3 + 32
# == 896
# 
# Formula for Shape of a Convolutional Layer
# =======================================================
# 
# depth == K (number of filters)
#       == 32
#       
# Width of Convolutional Layer
# =======================================================
# 64