import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
mg = cv2.imread('ATU1.jpg',)
mg = cv2.cvtColor(mg, cv2.COLOR_BGR2RGB)  # Fix colour issues

# cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(mg, cv2.COLOR_BGR2GRAY)

# Harris corner detection
imgHarris = mg.copy()  # Copy of the original image
block_size = 2
aperture_size = 3
k = 0.04
# Grayscale image used as input
dst = cv2.cornerHarris(gray_image, block_size, aperture_size, k)
# Loops through every element in the 2d matrix
threshold = 0.1  # number between 0 and 1
for i in range(len(dst)):
    for j in range(len(dst[i])):
        if dst[i][j] > (threshold*dst.max()):
            cv2.circle(imgHarris, (j, i), 3, (255, 170, 29), -1)

# Shi Tomasi
maxCorners = 4
qualityLevel = 0.01
minDistance = 10
# Detect corners
corners = cv2.goodFeaturesToTrack(
    gray_image, maxCorners, qualityLevel, minDistance)
corners = np.int8(corners)  # convert corners values to integer
imgShiTomasi = mg.copy()  # Copy of the original image

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
# Show plotted imgages
plt.show()
