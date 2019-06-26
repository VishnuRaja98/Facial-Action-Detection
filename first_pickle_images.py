import os
import glob
from PIL import Image
import numpy as np
import random
import matplotlib.pyplot as plt 

images_array1=[]
images_array=[]
labels_array=[]

f=(glob.glob("C:/Users/vishn/Pictures/Camera Roll/left1/left_small/*.jpg"))

for fname in f:
	images_array1.append([np.array(Image.open(fname)),[1,0,0]])

f=(glob.glob("C:/Users/vishn/Pictures/Camera Roll/right1/right_small/*.jpg"))

for fname in f:
	images_array1.append([np.array(Image.open(fname)),[0,0,1]])

f=(glob.glob("C:/Users/vishn/Pictures/Camera Roll/center1/center_small/*.jpg"))

for fname in f:
	images_array1.append([np.array(Image.open(fname)),[0,1,0]])


# print(images_array[0])

random.shuffle(images_array1)

for i in images_array1:
	images_array.append(i[0])
	labels_array.append(i[1])

# train_images=np.array(i[0] for i in images_array)
# train_labels=np.array(i[1] for i in images_array)


# print(images_array[0])

# train_images=train_images / 255.0
# for i in images_array:
# 	i[0]=i[0]/255.0


train_images=np.array(images_array)
train_labels=np.array(labels_array)

train_images=train_images/255.0

print(train_images.shape)
print(train_labels)

print(train_images[0])

np.save('saved_images',train_images[:2500])
np.save('saved_labels',train_labels[:2500])
np.save('saved_images_test',train_images[2500:])
np.save('saved_labels_test',train_labels[2500:])

# plt.figure(figsize=(10,10))
# for i in range(25):
#     plt.subplot(5,5,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[i], cmap=plt.cm.binary)
#     plt.xlabel(train_labels[i])
# plt.show()
# print(train_images)
