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


test_images_2=np.load("saved_images_test2.npy")
test_labels_2=np.load("saved_labels_test2.npy")

model = load_model('first_run.h5')

result_batch = model.predict(test_images_2)
values=['left','center','right']
labels_batch = []
for i in range(14):
	labels_batch.append(values[max_val(result_batch[i])])

plt.figure(figsize=(10,10))
for i in range(14):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    
    plt.imshow(test_images_2[i])
    plt.xlabel(labels_batch[i])
plt.show()