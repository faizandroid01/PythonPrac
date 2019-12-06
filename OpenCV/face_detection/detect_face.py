import cv2

# create a cascade Classifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# read the image from a file
img = cv2.imread("girl_face.jpg")

# Reading the image as GrayScale Image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# search the coordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

# print(type(faces))
print(faces)  # [[800 198 723 723]]

# draw a rectangle
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

# resize the image
resized_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
print(img.shape)
print(resized_img.shape)
# show the image
cv2.imshow("Resized Face Detection", resized_img)
# wait for the image to be shown
cv2.waitKey(0)
cv2.destroyAllWindows()

# write the image
cv2.imwrite("Face_detetcion_for_girls_image.jpg", resized_img)
