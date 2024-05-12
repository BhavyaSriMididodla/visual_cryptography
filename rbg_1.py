'''import numpy as np
import cv2

# load the image
image = cv2.imread('C:\crypto\Recovered.jpg')

# convert the image to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# extract the RGB pixels from the image
r, g, b = cv2.split(rgb_image)

# show the image
cv2.imshow("RGB Image", rgb_image)
cv2.waitKey(0)'''

import matplotlib.pyplot as plt
import cv2

# read image
img = cv2.imread(r'D:\UROP\dlena.jpg')

# extract RGB pixels
r, g, b = cv2.split(img)
cv2.imwrite('red.jpg',r)
cv2.imwrite('green.jpg',g)
cv2.imwrite('blue.jpg',b)
# plot the Red, Green and Blue components
plt.figure(figsize=(20,10))
plt.subplot(131)
plt.imshow(r,cmap='Reds_r')
plt.title('Red channel')
cv2.imwrite('red.jpg',r)
plt.axis('off')
plt.subplot(132)
plt.imshow(g,cmap='Greens_r')
plt.title('Green channel')
cv2.imwrite('green.jpg',g)
plt.axis('off')
plt.subplot(133)
plt.imshow(b,cmap='Blues_r')
#plt.imsave()
plt.title('Blue channel')
cv2.imwrite('blue.jpg',b)
plt.axis('off')
plt.show()

'''import matplotlib.pyplot as plt
import cv2
img = cv2.imread('C:\crypto\Recovered.jpg')
r, g, b = cv2.split(img)
img[:,:,2] = r
img[:,:,1] = g
img[:,:,0] = b
plt.imshow(img[:,:,2])'''