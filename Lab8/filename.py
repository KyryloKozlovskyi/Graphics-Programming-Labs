import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
mg = cv2.imread('ATU.jpg',)
mg = cv2.cvtColor(mg, cv2.COLOR_BGR2RGB)  # Fix colour issues

# cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(mg, cv2.COLOR_BGR2GRAY)

# Specify number of rows and columns
nrows = 2
ncols = 1

# Plot both gray and colour images
plt.subplot(nrows, ncols, 1), plt.imshow(mg, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols, 2), plt.imshow(gray_image, cmap='gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
plt.show()
