from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Create Sequential Model for CNN
model = Sequential()

# Add sequence of Convolutional Layers to the Convolutional Neural Network (CNN)
# each followed by a Max Pooling Layer. These layers are designed to
# convert the input array of image pixels into an array where all
# spatial info extracted and only info encoding image content remains.
# In the final layer the array is flattened from an array into a vector.
# The remaining Fully Connected Layers (Dense) finalise the image content.
# The final Dense layer has an entry for each object class in the dataset.
# The softmax Activation Function ensures probabilities are returned between 0 and 1.
model.add(Conv2D(filters=16, 
								 kernel_size=2, 
								 strides=1, 
								 padding='same', 
    						 activation='relu', 
    						 input_shape=(32, 32, 3)))
model.add(MaxPooling2D(pool_size=2))

model.add(Conv2D(filters=32, kernel_size=2, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=2))

model.add(Conv2D(filters=64, kernel_size=2, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=2))

model.add(Flatten())

model.add(Dense(500, activation='relu'))
# Number of nodes in final layer should equal total number of classes in dataset
model.add(Dense(10, activation='softmax'))

model.summary()

# Output
# 
# _________________________________________________________________
# Layer (type)                 Output Shape              Param #   
# =================================================================
# conv2d_1 (Conv2D)            (None, 32, 32, 16)        208       
# _________________________________________________________________
# max_pooling2d_1 (MaxPooling2 (None, 16, 16, 16)        0         
# _________________________________________________________________
# conv2d_2 (Conv2D)            (None, 16, 16, 32)        2080      
# _________________________________________________________________
# max_pooling2d_2 (MaxPooling2 (None, 8, 8, 32)          0         
# _________________________________________________________________
# conv2d_3 (Conv2D)            (None, 8, 8, 64)          8256      
# _________________________________________________________________
# max_pooling2d_3 (MaxPooling2 (None, 4, 4, 64)          0         
# _________________________________________________________________
# flatten_1 (Flatten)          (None, 1024)              0         
# _________________________________________________________________
# dense_1 (Dense)              (None, 500)               512500    
# _________________________________________________________________
# dense_2 (Dense)              (None, 10)                5010      
# =================================================================
# Total params: 528,054.0
# Trainable params: 528,054.0
# Non-trainable params: 0.0
# _________________________________________________________________