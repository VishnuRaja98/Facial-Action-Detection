import os
from PIL import Image
# from os import walk
import numpy as np
import random
import glob

f=(glob.glob("C:/Users/vishn/Pictures/Camera Roll/avinash*.jpg"))


images_array1=[]
images_array=[]
labels_array=[]

im=Image.open(f[0])
# print("Width,height are",img.size)
width, height = im.size
left = (width - height)/2
top = (height - height)/2
right = (width + height)/2
bottom = (height + height)/2

print(len(f))
for i in range(len(f)):
	img=Image.open(f[i])  
	# print("Width,height are",img.size)
	# width, height = img.size
	# left = (width - height)/2
	# top = (height - height)/2
	# right = (width + height)/2
	# bottom = (height + height)/2

	img=img.crop((left, top, right, bottom))
	img=img.resize((256,256))
	# img=img.convert('L')
	# images_array1=[]
	images_array1.append([np.array(img),[1,0,0]])
	# img.save(name)

# print("left done")
for i in images_array1:
	images_array.append(i[0])
	labels_array.append(i[1])


train_images=np.array(images_array)
train_labels=np.array(labels_array)

train_images=train_images/255.0

print(train_images.shape)
print(train_labels)

# print(train_images[0])

np.save('saved_images_test2',train_images)
np.save('saved_labels_test2',train_labels)