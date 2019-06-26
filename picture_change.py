import os
from PIL import Image
# from os import walk
import glob

f=(glob.glob("C:/Users/vishn/Pictures/Camera Roll/left1/*.jpg"))

im=Image.open(f[0])
# print("Width,height are",img.size)
width, height = im.size
left = (width - height)/2
top = (height - height)/2
right = (width + height)/2
bottom = (height + height)/2

# print(left, top, right, bottom)


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
	name='C:/Users/vishn/Pictures/Camera Roll/left1/left_small/left'+str(i)+".jpg"
	img.save(name)

print("left done")



f=(glob.glob("C:/Users/vishn/Pictures/Camera Roll/right1/*.jpg"))

for i in range(len(f)):
	img=Image.open(f[i])
	# width, height = img.size
	# left = (width - height)/2
	# top = (height - height)/2
	# right = (width + height)/2
	# bottom = (height + height)/2

	img=img.crop((left, top, right, bottom))
	# print("Width,height are",img.size)
	# 
	img=img.resize((256,256))
	# img=img.convert('L')
	name='C:/Users/vishn/Pictures/Camera Roll/right1/right_small/right'+str(i)+".jpg"
	img.save(name)

print("right done")

f=(glob.glob("C:/Users/vishn/Pictures/Camera Roll/center1/*.jpg"))

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
	name='C:/Users/vishn/Pictures/Camera Roll/center1/center_small/center'+str(i)+".jpg"
	img.save(name)

print("center done")	

# f=(glob.glob("C:/Users/vishn/Pictures/Camera Roll/top/*.jpg"))

# for i in range(len(f)):
# 	img=Image.open(f[i])
# 	# print("Width,height are",img.size)
# 	img=img.resize((128,128))
# 	img=img.convert('L')
# 	name='C:/Users/vishn/Pictures/Camera Roll/top/top_small/img_top'+str(i)+".jpg"
# 	img.save(name)

# print("top done")

# f=(glob.glob("C:/Users/vishn/Pictures/Camera Roll/bottom/*.jpg"))

# for i in range(len(f)):
# 	img=Image.open(f[i])
# 	# print("Width,height are",img.size)
# 	img=img.resize((128,128))
# 	img=img.convert('L')
# 	name='C:/Users/vishn/Pictures/Camera Roll/bottom/bottom_small/img_bottom'+str(i)+".jpg"
# 	img.save(name)

# print("bottom done")


# f=(glob.glob("C:/Users/vishn/Pictures/Camera Roll/checking/*.jpg"))
# for i in range(len(f)):
# 	img=Image.open(f[i])
# 	print(img.histogram())
