import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('1.jpg')  # 读取彩色图像，cv2读取的格式是BGR格式
grayscale_img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
# print(img) # h高 w宽 c层数
cv2.imshow('img', img)
cv2.imshow('img', img)
cv2.imwrite('grayscale_1.jpg', img)
cv2.waitKey(0)  # 0 代表任意操作后关闭，其他数字则是在x毫秒后关闭
