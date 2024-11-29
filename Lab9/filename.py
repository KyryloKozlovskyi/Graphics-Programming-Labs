import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
mg = cv2.imread('ATU1.jpg',)
mg = cv2.cvtColor(mg, cv2.COLOR_BGR2RGB)  # Fix colour issues

# cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(mg, cv2.COLOR_BGR2GRAY)

# Harris corner detection
imgHarris = mg.copy()  # Copy grayscale image
block_size = 2
aperture_size = 3
k = 0.04
dst = cv2.cornerHarris(gray_image, block_size, aperture_size, k)

threshold = 0.25  # number between 0 and 1
for i in range(len(dst)):
    for j in range(len(dst[i])):
        if dst[i][j] > (threshold*dst.max()):
            cv2.circle(imgHarris, (j, i), 3, (0, 75, 75), -1)

# Specify number of rows and columns
nrows = 3
ncols = 3

# Originall
plt.subplot(nrows, ncols, 1), plt.imshow(mg, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
# Gray scale
plt.subplot(nrows, ncols, 2), plt.imshow(gray_image, cmap='gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
# Harris
plt.subplot(nrows, ncols, 3), plt.imshow(imgHarris, cmap='gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
plt.show()
