import cv2
import numpy as np

img = cv2.imread('test_2.jpg')
gray_img = cv2.imread('test_2.jpg', cv2.IMREAD_GRAYSCALE) # 灰度图
# img =cv2.pyrUp(img)
# gray_img = cv2.pyrUp(gray_img)
ret, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY) # 二值化处理
# cv2.imshow('??',thresh)
contours, hierarchy = cv2.findContours(thresh, 0,cv2.CHAIN_APPROX_SIMPLE) # 调用findContours,返回轮廓（list）和层级

new_img=cv2.drawContours(img.copy(), contours, -1, (0 ,0, 255), 2)
cv2.imshow('draw_img', new_img)
cv2.waitKey()