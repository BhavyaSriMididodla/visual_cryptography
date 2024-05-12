# import the necessary packages
import numpy as np
import cv2

# load the image
image = cv2.imread(r"C:\crypto\red.jpg")

# create a blank red image
blank_red = np.zeros((image.shape[0], image.shape[1], 3), dtype="uint8")
blank_red[:,:] = (0, 0, 255)

# convert the grayscale image to red
red_image = cv2.addWeighted(image, 0.6, blank_red, 0.4, 0)

# save the image
cv2.imshow("Red Image", red_image)
cv2.imwrite("red_image.png", red_image)