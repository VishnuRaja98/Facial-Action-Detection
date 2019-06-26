import cv2
import numpy as np
import os
from PIL import Image
import glob

name=input("Enter name :")
print(name)
path=name
count=0
# os.rmdir(name+"_db")

os.mkdir(name+"_db")

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(path+'_output.avi',fourcc, 20.0, (1280,720))
flag=1

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret==True:

		out.write(frame)
		
		
		# frame=frame.crop((left, top, right, bottom))
		# frame=frame.resize((256,256))
		# frame=frame[left:right,top:bottom]
		# if flag==1:
		# 	print(frame.size)
		# 	flag=0
		cv2.imshow('frame',frame)

		# frame=cv2.resize(frame,(256,256))
		
		cv2.imwrite(path+"_db/"+str(count)+".jpg",frame)
		count=count+1
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

os.mkdir(name)
cwd = os.getcwd()
# print(cwd+"/"+name+"_db/*.jpg")
f=(glob.glob(cwd+"/"+name+"_db/*.jpg"))

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
	print("Width,height are",img.size)
	# width, height = img.size
	# left = (width - height)/2
	# top = (height - height)/2
	# right = (width + height)/2
	# bottom = (height + height)/2

	img=img.crop((left, top, right, bottom))
	print(im.size)
	img=img.resize((256,256))
	# img=img.convert('L')
	img.save(cwd+"/"+name+"/"+str(i)+".jpg")

print("done")
# os.remove(name+"_db")
# os.remove(path+'_output.avi')	