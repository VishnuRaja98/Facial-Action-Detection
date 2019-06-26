import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt 

def max_val(batch):
	max_index=0
	for i in range(len(batch)):
		if batch[i]>batch[max_index]:
			max_index=i 
	# print(batch,'maxindex=',max_index)
	return max_index

test_images=np.load("saved_images_test.npy")
test_labels=np.load("saved_labels_test.npy")

model = load_model('first_run.h5')

result_batch = model.predict(test_images[25:50])
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
    plt.imshow(test_images[i+25])
    plt.xlabel(labels_batch[i])
plt.show()


