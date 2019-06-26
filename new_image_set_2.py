import cv2
import numpy as np
import os
from PIL import Image
# from os import walk
import glob

print(cv2.__version__)
# vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/8_video.mp4")
# success,image=vidcap.read()
count=0

vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/sawant1.mp4")
success,image=vidcap.read()
count=0
success=True
while success:
  cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/sawant/sawant%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  # print('Read a new frame: ', success)
  count += 1

count=0
vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/sanket1.mp4")
success,image=vidcap.read()
count=0
success=True
while success:
  cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/sanket/sanket1%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  # print('Read a new frame: ', success)
  count += 1

count=0
vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/chaitanya1.mp4")
success,image=vidcap.read()
count=0
success=True
while success:
  cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/chaitanya/chaitanya%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  # print('Read a new frame: ', success)
  count += 1


f=(glob.glob("C:/Users/vishn/Pictures/Camera Roll/sawant/*.jpg"))

im=Image.open(f[0])
# print("Width,height are",img.size)
width, height = im.size
left = (width - height)/2
top = (height - height)/2
right = (width + height)/2
bottom = (height + height)/2

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
	name='C:/Users/vishn/Pictures/Camera Roll/sawant/sawant_small/sawant'+str(i)+".jpg"
	img.save(name)

print("sawant done")

f=(glob.glob("C:/Users/vishn/Pictures/Camera Roll/sanket/*.jpg"))

im=Image.open(f[0])
# print("Width,height are",img.size)
width, height = im.size
left = (width - height)/2
top = (height - height)/2
right = (width + height)/2
bottom = (height + height)/2

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
	name='C:/Users/vishn/Pictures/Camera Roll/sanket/sanket_small/sanket'+str(i)+".jpg"
	img.save(name)

print("sanket done")

f=(glob.glob("C:/Users/vishn/Pictures/Camera Roll/chaitanya/*.jpg"))

im=Image.open(f[0])
# print("Width,height are",img.size)
width, height = im.size
left = (width - height)/2
top = (height - height)/2
right = (width + height)/2
bottom = (height + height)/2

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
	name='C:/Users/vishn/Pictures/Camera Roll/chaitanya/chaitanya_small/chaitanya'+str(i)+".jpg"
	img.save(name)

print("sawant done")