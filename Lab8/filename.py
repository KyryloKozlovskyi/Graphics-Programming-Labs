import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
mg = cv2.imread('IMG.jpg',)
mg = cv2.cvtColor(mg, cv2.COLOR_BGR2RGB)  # Fix colour issues

# cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(mg, cv2.COLOR_BGR2GRAY)

# Specify kernel size
KernelSizeWidth = 3
KernelSizeHeight = 3
KernelSizeWidth2 = 13
KernelSizeHeight2 = 13

# GaussianBlur to blur the image
imgOut = cv2.GaussianBlur(gray_image, (KernelSizeWidth, KernelSizeHeight), 0)
imgOut2 = cv2.GaussianBlur(
    gray_image, (KernelSizeWidth2, KernelSizeHeight2), 0)

# Sobel edge detection
sobelHorizontal = cv2.Sobel(imgOut, cv2.CV_64F, 1, 0, ksize=5)  # x dir
sobelVertical = cv2.Sobel(imgOut, cv2.CV_64F, 0, 1, ksize=5)  # y dir
sobelXY = sobelHorizontal + sobelVertical

# Specify threshholds
cannyThreshold = 100
cannyParam2 = 200

# Canny edge detection
canny = cv2.Canny(mg, cannyThreshold, cannyParam2)

# Specify number of rows and columns
nrows = 3
ncols = 3

# Plot gray colour, 3x3, 13x13 blur images
# Original image
plt.subplot(nrows, ncols, 1), plt.imshow(mg, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
# Gray scale
plt.subplot(nrows, ncols, 2), plt.imshow(gray_image, cmap='gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
# 3x3 Blur
plt.subplot(nrows, ncols, 3), plt.imshow(imgOut, cmap='gray')
plt.title('3x3 Blur'), plt.xticks([]), plt.yticks([])
# 13x13 Blur
plt.subplot(nrows, ncols, 4), plt.imshow(imgOut2, cmap='gray')
plt.title('13x13 Blur'), plt.xticks([]), plt.yticks([])
# Sobel (X) Horizontal
plt.subplot(nrows, ncols, 5), plt.imshow(sobelHorizontal, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# Sobel (Y) Vertical
plt.subplot(nrows, ncols, 6), plt.imshow(sobelVertical, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
# Sobel (XY)
plt.subplot(nrows, ncols, 7), plt.imshow(sobelVertical, cmap='gray')
plt.title('Sobel XY'), plt.xticks([]), plt.yticks([])
# Canny
plt.subplot(nrows, ncols, 8), plt.imshow(canny, cmap='gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])
plt.show()
