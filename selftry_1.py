import tensorflow as tf
from tensorflow import keras
import glob
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 


filelist=glob.glob("C:/Users/vishn/Pictures/Camera Roll/final_db_img/*.jpg")

images_array=[np.array(Image.open(fname)) for fname in filelist]

train_images=np.array(images_array)

labels_array=[]
for fname in filelist:
	if "left" in fname:
		labels_array.append(0)
	elif "right" in fname:
		labels_array.append(2) 
	elif "center" in fname:
		labels_array.append(1) 
	elif "top" in fname:
		labels_array.append(3)
	elif "bottom" in fname:
		labels_array.append(4)

train_labels=np.array(labels_array)
train_images=train_images/255
# print(train_labels)

for i in range(18):
	print(train_labels[100*i])
		
print("length of train labels=",len(train_labels))
print("shape of train images=",train_images.shape)

# plt.figure(figsize=(10,10))
# for i in range(25):
#     plt.subplot(5,5,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[800+i], cmap=plt.cm.binary)
#     plt.xlabel(train_labels[800+i])
# plt.show()

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(256, 256)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)
