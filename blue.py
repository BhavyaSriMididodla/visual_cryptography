#importing the libraries 
import cv2 
import numpy as np 
  
#reading the image 
img = cv2.imread(r'C:\crypto\blue.jpg') 
  
#creating an empty numpy array to store the blue image 
blueImg = np.zeros((img.shape[0], img.shape[1], 3), np.uint8) 
  
#adding the blue color to the image 
blueImg[:, :, 0] = img[:, :, 0] 
  
#showing the image 
cv2.imshow('Blue image', blueImg)
cv2.imwrite("blue.jpg", blueImg) 
cv2.waitKey(0) 
cv2.destroyAllWindows()