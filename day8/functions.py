import cv2 as cv

img = cv.imread('day8/assets/Photos/cat.jpg')
cv.imshow('Photo', img)

# Converting into grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
cany = cv.Canny(blur, 125, 175)
cv.imshow('Canny', cany)

# Dilating the image
dialted = cv.dilate(cany, (3, 3), iterations=3)
cv.imshow('Dilated', dialted)

# Eroding
eroded = cv.erode(dialted, (3, 3), iterations=1)
cv.imshow('Eroding', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
