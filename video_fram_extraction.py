import cv2
import numpy as np
print(cv2.__version__)
# vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/8_video.mp4")
# success,image=vidcap.read()
count=0
# success=True
# while success:
#   cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/checkingVideo/frame8_%d.jpg" % count, image)     # save frame as JPEG file
#   success,image = vidcap.read()
#   # print('Read a new frame: ', success)
#   count += 1

# vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/9_video.mp4")
# success,image=vidcap.read()
# count=0
# success=True
# while success:
#   cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/checkingVideo/frame9_%d.jpg" % count, image)     # save frame as JPEG file
#   success,image = vidcap.read()
#   # print('Read a new frame: ', success)
#   count += 1

# vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/10_video.mp4")
# success,image=vidcap.read()
# count=0
# success=True
# while success:
#   cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/checkingVideo/frame10_%d.jpg" % count, image)     # save frame as JPEG file
#   success,image = vidcap.read()
#   # print('Read a new frame: ', success)
#   count += 1

vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/left3.mp4")
success,image=vidcap.read()
count=0
success=True
while success:
  cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/left1/left%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  # print('Read a new frame: ', success)
  count += 1
vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/left2.mp4")
success,image=vidcap.read()
success=True
while success:
  cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/left1/left%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  # print('Read a new frame: ', success)
  count += 1
vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/left1.mp4")
success,image=vidcap.read()
success=True
while success:
  cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/left1/left%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1



vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/right3.mp4")
success,image=vidcap.read()
count=0
success=True
while success:
  cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/right1/right%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  # print('Read a new frame: ', success)
  count += 1
vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/right2.mp4")
success,image=vidcap.read()
success=True
while success:
  cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/right1/right%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  # print('Read a new frame: ', success)
  count += 1
vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/right1.mp4")
success,image=vidcap.read()
success=True
while success:
  cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/right1/right%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1



vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/center3.mp4")
success,image=vidcap.read()
count=0
success=True
while success:
  cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/center1/center%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  # print('Read a new frame: ', success)
  count += 1
vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/center2.mp4")
success,image=vidcap.read()
success=True
while success:
  cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/center1/center%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  # print('Read a new frame: ', success)
  count += 1
vidcap=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/center1.mp4")
success,image=vidcap.read()
success=True
while success:
  cv2.imwrite("C:/Users/vishn/Pictures/Camera Roll/center1/center%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  # print('Read a new frame: ', success)
  count += 1
# vidcap_top2=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/top2.mp4")
# vidcap_bottom2=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/bottom2.mp4")
# vidcap_left1=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/left1.mp4")
# vidcap_right1=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/right1.mp4")
# vidcap_center1=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/center1.mp4")
# vidcap_top1=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/top1.mp4")
# vidcap_bottom1=cv2.VideoCapture("C:/Users/vishn/Pictures/Camera Roll/bottom1.mp4")


# images_array=[]
# labels_array=[]

# success=True
# while success:
# 	success,image = vidcap_left3.read()
# 	images_array.append(np.array(image))
# 	labels_array.append(1)

# success=True
# while success:
# 	success,image = vidcap_right3.read()
# 	images_array.append(np.array(image))
# 	labels_array.append(3)

# success=True
# while success:
# 	success,image = vidcap_center3.read()
# 	images_array.append(np.array(image))
# 	labels_array.append(2)

# success=True
# while success:
# 	success,image = vidcap_top3.read()
# 	images_array.append(np.array(image))

# success=True
# while success:
# 	success,image = vidcap_bottom3.read()
# 	images_array.append(np.array(image))

# success=True
# while success:
# 	success,image = vidcap_left2.read()
# 	images_array.append(np.array(image))
# 	labels_array.append(1)

# success=True
# while success:
# 	success,image = vidcap_right2.read()
# 	images_array.append(np.array(image))
# 	labels_array.append(3)

# success=True
# while success:
# 	success,image = vidcap_center2.read()
# 	images_array.append(np.array(image))
# 	labels_array.append(2)

# success=True
# while success:
# 	success,image = vidcap_top2.read()
# 	images_array.append(np.array(image))

# success=True
# while success:
# 	success,image = vidcap_bottom2.read()
# 	images_array.append(np.array(image))

# success=True
# while success:
# 	success,image = vidcap_left1.read()
# 	images_array.append(np.array(image))
# 	labels_array.append(1)

# success=True
# while success:
# 	success,image = vidcap_right1.read()
# 	images_array.append(np.array(image))
# 	labels_array.append(3)

# success=True
# while success:
# 	success,image = vidcap_center1.read()
# 	images_array.append(np.array(image))
# 	labels_array.append(2)

# success=True
# while success:
# 	success,image = vidcap_top1.read()
# 	images_array.append(np.array(image))

# success=True
# while success:
# 	success,image = vidcap_bottom1.read()
# 	images_array.append(np.array(image))
# train_images=np.array(images_array)
# train_labels=np.array(labels_array)

# train_images=train_images/255
# print("length of train labels=",len(train_labels))
# print("shape of train images=",train_images.shape)
# model = keras.Sequential([
#     keras.layers.Flatten(input_shape=(128, 128)),
#     keras.layers.Dense(128, activation=tf.nn.relu),
#     keras.layers.Dense(10, activation=tf.nn.softmax)
# ])

# model.compile(optimizer='adam', 
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])

# model.fit(train_images, train_labels, epochs=5)


