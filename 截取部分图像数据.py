import cv2

img = cv2.imread('1.jpg')
tupian = img[200:1000, 600:2000]
cv2.imshow('show', tupian)
cv2.waitKey(0)
