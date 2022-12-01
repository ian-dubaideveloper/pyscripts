# Importing the Required Module
import cv2 as cv

# Reading the image
# Replace this image name to your image name
image = cv.imread("iron.jpeg")

# Converting the Image into gray_image
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Inverting the Imge
invert_image = cv.bitwise_not(gray_image)

# Blur Image
blur_image = cv.GaussianBlur(invert_image, (21,21), 0)

# Inverting the Blured Image
invert_blur = cv.bitwise_not(blur_image)

# Convert Image Into sketch
sketch = cv.divide(gray_image, invert_blur, scale=256.0)

# Generating the Sketch Image Named as Sketch.png
cv.imwrite("Sketch4.png", invert_blur)