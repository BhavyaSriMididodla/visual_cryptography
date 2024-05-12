#Using OpenCV
import cv2

#Read the gray scale image
img = cv2.imread(r'C:\crypto\green.jpg', 0)

#Convert to green image
green_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
green_img[:,:,1] = 255

#Save the image
cv2.imwrite('green.jpg', green_img)