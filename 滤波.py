import cv2
import numpy as np


# 均值滤波相当于简单的平均卷积操作

def show(img, name):
    img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
    cv2.imshow(name, img)
    cv2.waitKey(0)


img = cv2.imread('test.jpg')
blur = cv2.blur(img, (3, 3))  # 均值滤波
aussian = cv2.GaussianBlur(img, (5, 5), 1)  # 高斯滤波
median = cv2.medianBlur(img, 5)  # 中值滤波效果最好
res = np.hstack((blur, aussian, median))
# vstack就是竖过来拼接
show(res, 'blur')
