import cv2 as cv

img = cv.imread('dog.jpg')
cv.imshow("dog", img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

#blur
blur = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

#edge cascade
canny = cv.Canny(blur, 100, 100)
# cv.imshow('canny', canny)

#dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=3)
# cv.imshow('dilated', dilated)

#erode
eroded = cv.erode(dilated, (3, 3), iterations=3)
# cv.imshow('eroded', eroded)

#resize
resize = cv.resize(img, (500, 500), interpolation= cv.INTER_CUBIC)
# cv.imshow("resize", resize)

#cropping
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)