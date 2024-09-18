# Importing required libraries
from PIL import Image, ImageEnhance
import cv2
import matplotlib.pyplot as plt

# Load an image using Pillow and OpenCV
pillow_img = Image.open('tiger.jpg')
opencv_img = cv2.imread('tiger.jpg')

# Pillow Transformations

# 1. Resize image using Pillow
resized_pillow_img = pillow_img.resize((300, 300))

# 2. Rotate image by 45 degrees using Pillow
rotated_pillow_img = pillow_img.rotate(45)

# 3. Flip image horizontally using Pillow
flipped_pillow_img = pillow_img.transpose(Image.FLIP_LEFT_RIGHT)

# 4. Brightness adjustment using Pillow
enhancer = ImageEnhance.Brightness(pillow_img)
brightened_pillow_img = enhancer.enhance(1.5)  # Increase brightness by 50%

# OpenCV Transformations

# 1. Resize image using OpenCV
resized_opencv_img = cv2.resize(opencv_img, (300, 300))

# 2. Rotate image by 45 degrees using OpenCV
(h, w) = opencv_img.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_opencv_img = cv2.warpAffine(opencv_img, matrix, (w, h))

# 3. Flip image horizontally using OpenCV
flipped_opencv_img = cv2.flip(opencv_img, 1)

# 4. Brightness adjustment using OpenCV (Convert to HSV and adjust V channel)
hsv_img = cv2.cvtColor(opencv_img, cv2.COLOR_BGR2HSV)
hsv_img[:, :, 2] = cv2.multiply(hsv_img[:, :, 2], 1.5)
brightened_opencv_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

# Plotting all transformations side by side
fig, axs = plt.subplots(2, 5, figsize=(15, 6))

# Original Images
axs[0, 0].imshow(pillow_img)
axs[0, 0].set_title('Original (Pillow)')
axs[0, 0].axis('off')

axs[1, 0].imshow(cv2.cvtColor(opencv_img, cv2.COLOR_BGR2RGB))
axs[1, 0].set_title('Original (OpenCV)')
axs[1, 0].axis('off')

# Pillow Transformations
axs[0, 1].imshow(resized_pillow_img)
axs[0, 1].set_title('Pillow Resized')
axs[0, 1].axis('off')

axs[0, 2].imshow(rotated_pillow_img)
axs[0, 2].set_title('Pillow Rotated')
axs[0, 2].axis('off')

axs[0, 3].imshow(flipped_pillow_img)
axs[0, 3].set_title('Pillow Flipped')
axs[0, 3].axis('off')

axs[0, 4].imshow(brightened_pillow_img)
axs[0, 4].set_title('Pillow Brightened')
axs[0, 4].axis('off')

# OpenCV Transformations
axs[1, 1].imshow(cv2.cvtColor(resized_opencv_img, cv2.COLOR_BGR2RGB))
axs[1, 1].set_title('OpenCV Resized')
axs[1, 1].axis('off')

axs[1, 2].imshow(cv2.cvtColor(rotated_opencv_img, cv2.COLOR_BGR2RGB))
axs[1, 2].set_title('OpenCV Rotated')
axs[1, 2].axis('off')

axs[1, 3].imshow(cv2.cvtColor(flipped_opencv_img, cv2.COLOR_BGR2RGB))
axs[1, 3].set_title('OpenCV Flipped')
axs[1, 3].axis('off')

axs[1, 4].imshow(cv2.cvtColor(brightened_opencv_img, cv2.COLOR_BGR2RGB))
axs[1, 4].set_title('OpenCV Brightened')
axs[1, 4].axis('off')

# Adjust layout
plt.tight_layout()
plt.show()