#!/usr/bin/env python
# coding: utf-8


# ### Let's construct LeNet in Keras!
# 
# #### First let's load and prep our MNIST data

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2
from keras.datasets import mnist
from keras.utils import np_utils
import keras
import sys

input_file = open(r'/mlops/input.txt',"r")
input1 = input_file.read()
inputs = input1.split('\n')

# loads the MNIST dataset
(x_train, y_train), (x_test, y_test)  = mnist.load_data()

# Lets store the number of rows and columns
img_rows = x_train[0].shape[0]
img_cols = x_train[1].shape[0]

# Getting our date in the right 'shape' needed for Keras
# We need to add a 4th dimenion to our date thereby changing our
# Our original image shape of (60000,28,28) to (60000,28,28,1)
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

# store the shape of a single image 
input_shape = (img_rows, img_cols, 1)

# change our image type to float32 data type
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Normalize our data by changing the range from (0 to 255) to (0 to 1)
x_train /= 255
x_test /= 255

# Now we one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

num_classes = y_test.shape[1]
num_pixels = x_train.shape[1] * x_train.shape[2]

kernel_size1=int(inputs[0])
pool_size1=int(inputs[1]) 
epoch_number=int(inputs[2])
learn_rate_no=float(inputs[3])
Convlayer_no=int(inputs[4])
fc_input=int(inputs[5])
neuron_no=int(inputs[6])

#create model
model = Sequential()

for i in range(1,Convlayer_no):
         #kernel_size_one=int(input[0])
         #kernel_size_two=int(inputs[1])
         #filter_size1=int(inputs[2])
         #pool_size_one=int(inputs[3])
         #pool_size_two=int(inputs[4])
        # 2 sets of CRP (Convolution, RELU, Pooling)
         model.add(Conv2D(filters=20,kernel_size=(kernel_size1, kernel_size1),
         padding = 'same',input_shape = input_shape))
         model.add(Activation("relu"))
         model.add(MaxPooling2D(pool_size = (pool_size1, pool_size1)))
         model.summary()

# Fully connected layers (w/ RELU)
#fc_input_layer = inputs[8]
for j in range(1,int(fc_input)):
               neuron_no = int(inputs[6])
               model.add(Flatten())
               model.add(Dense(neuron_no))
               model.add(Activation("relu"))
               inputs[6]=int(inputs[6])-(int(inputs[6])/2)

# Softmax (for classification)
model.add(Dense(num_classes))
model.add(Activation("softmax"))
           
model.compile(loss = 'categorical_crossentropy',
              optimizer = keras.optimizers.Adadelta(learning_rate=learn_rate_no),
              metrics = ['accuracy'])

# Training Parameters
batch_size = 128
epochs = epoch_number

history = model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(x_test, y_test),
          shuffle=True )

model.save("mnist_LeNetnew.h5")

# Evaluate the performance of our trained model
scores = model.evaluate(x_test, y_test, verbose=1)
print('Test Loss:', scores[0])
print('Test accuracy:', scores[1])
print(scores[0])
print(scores[1])


accuracy= open(r'/mlops/new_accuracy.txt', "w")
accuracy.seek(0)
accuracy.write(str(scores[1]))
accuracy.close()

display_matter = open(r'/mlops/displayresult.html',"r+")
display_matter.read()
display_matter.write('<pre>\n---------------------------------------------\n')
display_matter.write('\nAccuracy achieved : ' + str(scores[1])+'\n</pre>')
display_matter.close()






