import cv2
import os

#  read an image
img = cv2.imread('bike.jpg', 1)
# Will be an numpy ndarray
print(type(img))
# will be nd array
print(img)
# check for path
print(os.path.exists('/home/faiz/ubuntu_18.04_workspace/Python_WorkArea/PythonPrac/OpenCV/Read-Modify-Write-Image/bike.jpg'))

print('---------------------------------------------------------')
# pixels can be seen as
print(img[0][0])
print(img[0][1])

# Working code to see the image displayed
#  can see the image as
# hold the window for particular key
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('-------------------')
# To see the image size and dimension
print(img.shape)
# resizing of image
resized_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
print(resized_img.shape)

cv2.imshow("Resized Image Window By Half", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# write image to external

cv2.imwrite("Original Image.jpg", img)
cv2.imwrite("Resized Image Window By Half.jpg", resized_img)
