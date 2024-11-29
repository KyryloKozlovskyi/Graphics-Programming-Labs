import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
mg = cv2.imread('ATU1.jpg',)
mg = cv2.cvtColor(mg, cv2.COLOR_BGR2RGB)  # Fix colour issues

# cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(mg, cv2.COLOR_BGR2GRAY)

# Harris corner detection
imgHarris = gray_image.copy()  # Copy grayscale image
block_size = 2
aperture_size = 3
k = 0.04
dst = cv2.cornerHarris(imgHarris, block_size, aperture_size, k)

# Specify number of rows and columns
nrows = 3
ncols = 3

# Originall
plt.subplot(nrows, ncols, 1), plt.imshow(mg, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
# Gray scale
plt.subplot(nrows, ncols, 2), plt.imshow(gray_image, cmap='gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
plt.show()
