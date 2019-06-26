import numpy as np
import matplotlib.pyplot as plt 
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

def max_val(batch):
	max_index=0
	for i in range(len(batch)):
		if batch[i]>batch[max_index]:
			max_index=i 
	# print(batch,'maxindex=',max_index)
	return max_index


train_images=np.load("saved_images.npy")
train_labels=np.load("saved_labels.npy")
test_images=np.load("saved_images_test.npy")
test_labels=np.load("saved_labels_test.npy")
# train_labels=train_labels[:2500]
# train_images=train_images[:2500]
# plt.figure(figsize=(10,10))
# for i in range(25):
#     plt.subplot(5,5,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[i])
#     plt.xlabel(train_labels[i])
# plt.show()
print(train_images[0].shape)



model=Sequential()

model.add(Conv2D(16, (5, 5), strides=(1, 1), activation='relu', input_shape=train_images[0].shape))
model.add(MaxPooling2D(pool_size=(4, 4), strides=(4, 4)))
model.add(Conv2D(16, (4, 4), strides=(1, 1), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Flatten())
model.add(Dropout(0.5))
model.add(Dense(2000, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2000, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(3,activation='sigmoid'))
# print(train_images.shape)

# model = keras.Sequential([
# 	keras.layers.Conv2D(filters=16,kernel_size=(5,5),strides=(1,1),activation=tf.nn.relu),
# 	keras.layers.MaxPool2D(pool_size=(4,4),strides=(4,4)),
# 	keras.layers.Conv2D(filters=16,kernel_size=(4,4),strides=(1,1),activation=tf.nn.relu),
# 	keras.layers.MaxPool2D(pool_size=(2,2),strides=(2,2)),
#     keras.layers.Flatten(),
#     keras.layers.Dropout(rate=0.5),
#     keras.layers.Dense(2000, activation=tf.nn.relu),
#     keras.layers.Dropout(rate=0.5),
#     keras.layers.Dense(2000, activation=tf.nn.relu),
#     keras.layers.Dropout(rate=0.5),
#     keras.layers.Dense(3, activation=tf.nn.sigmoid)
# ])


model.compile(optimizer='adamax', 
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)

model.evaluate(test_images, test_labels)

result_batch = model.predict(test_images[:25])
values=['left','center','right']
labels_batch = []
for i in range(25):
	labels_batch.append(values[max_val(result_batch[i])])

# print(labels_batch)


# print(model.predict(test_images[:10]))
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_images[i])
    plt.xlabel(labels_batch[i])
plt.show()

model.save('first_run.h5')