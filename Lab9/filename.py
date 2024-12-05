import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
mg = cv2.imread('ATU1.jpg',)
mg = cv2.cvtColor(mg, cv2.COLOR_BGR2RGB)  # Fix colour issues

# Load the second image
mg2 = cv2.imread('ATU.jpg',)
mg2 = cv2.cvtColor(mg2, cv2.COLOR_BGR2RGB)  # Fix colour issues

# Grayscale the image
gray_image = cv2.cvtColor(mg, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(mg2, cv2.COLOR_BGR2GRAY)

# Initiate ORB detector
orb = cv2.ORB_create()

# Find the keypoints with ORB for both images
kp = orb.detect(gray_image,None)
kp2 = orb.detect(gray_image2, None)
 
# Compute the descriptors with ORB for both images
kp, des = orb.compute(gray_image, kp)
kp2, des2 = orb.compute(gray_image2, kp2)

# Draw keypoints for both images
img2 = cv2.drawKeypoints(gray_image, kp, None, color=(0,255,0), flags=0)
img2_2 = cv2.drawKeypoints(gray_image2, kp2, None, color=(0, 255, 0), flags=0)

# Harris corner detection
imgHarris = mg.copy()  # Copy of the original image
imgHarris2 = mg2.copy()  # Copy of the second image
block_size = 2
aperture_size = 3
k = 0.04

# Harris corner detection for the first image
dst = cv2.cornerHarris(gray_image, block_size, aperture_size, k)
# Loops through every element in the 2d matrix
threshold = 0.1  # number between 0 and 1
for i in range(len(dst)):
    for j in range(len(dst[i])):
        if dst[i][j] > (threshold*dst.max()):
            cv2.circle(imgHarris, (j, i), 3, (255, 170, 29), -1)

# Harris corner detection for the second image
dst2 = cv2.cornerHarris(gray_image2, block_size, aperture_size, k)
# Loops through every element in the 2d matrix
threshold = 0.1  # number between 0 and 1
for i in range(len(dst2)):
    for j in range(len(dst2[i])):
        if dst2[i][j] > (threshold*dst2.max()):
            cv2.circle(imgHarris2, (j, i), 3, (255, 170, 29), -1)

# Shi Tomasi
maxCorners = 100
qualityLevel = 0.01
minDistance = 10

# Detect corners for the first image
corners = cv2.goodFeaturesToTrack(
    gray_image, maxCorners, qualityLevel, minDistance)
corners = np.int0(corners)  # convert corners values to integer
imgShiTomasi = mg.copy()  # Copy of the original image

# Plot GFTT corners on the first image
for i in corners:
    x, y = i.ravel()
    cv2.circle(imgShiTomasi, (x, y), 3, (170, 255, 29), -1)

# Detect corners for the second image
corners2 = cv2.goodFeaturesToTrack(
    gray_image2, maxCorners, qualityLevel, minDistance)
corners2 = np.int0(corners2)  # convert corners values to integer
imgShiTomasi2 = mg2.copy()  # Copy of the original image

# Plot GFTT corners on the second image
for i in corners2:
    x, y = i.ravel()
    cv2.circle(imgShiTomasi2, (x, y), 3, (170, 255, 29), -1)

# Specify number of rows and columns
nrows = 3
ncols = 4

# Originall
plt.subplot(nrows, ncols, 1), plt.imshow(mg, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
# Gray scale
plt.subplot(nrows, ncols, 2), plt.imshow(gray_image, cmap='gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
# Harris
plt.subplot(nrows, ncols, 3), plt.imshow(imgHarris, cmap='gray')
plt.title('Harris'), plt.xticks([]), plt.yticks([])
# GFTT
plt.subplot(nrows, ncols, 4), plt.imshow(imgShiTomasi, cmap='gray')
plt.title('GFTT'), plt.xticks([]), plt.yticks([])
# ORB
plt.subplot(nrows, ncols, 5), plt.imshow(img2, cmap='gray')
plt.title('ORB'), plt.xticks([]), plt.yticks([])
# Second image
plt.subplot(nrows, ncols, 6), plt.imshow(mg2, cmap='gray')
plt.title('Second Image'), plt.xticks([]), plt.yticks([])
# Gray scale
plt.subplot(nrows, ncols, 7), plt.imshow(gray_image2, cmap='gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
# Harris
plt.subplot(nrows, ncols, 8), plt.imshow(imgHarris2, cmap='gray')
plt.title('Harris'), plt.xticks([]), plt.yticks([])
# GFTT
plt.subplot(nrows, ncols, 9), plt.imshow(imgShiTomasi2, cmap='gray')
plt.title('GFTT'), plt.xticks([]), plt.yticks([])
# ORB
plt.subplot(nrows, ncols, 10), plt.imshow(img2_2, cmap='gray')
plt.title('ORB'), plt.xticks([]), plt.yticks([])
# Show plotted imgages
plt.show()
