import numpy as np
import argparse
import cv2


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread('test_2.jpg')
gray_img = cv2.imread('test_2.jpg', cv2.IMREAD_GRAYSCALE)
retVal, ref = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU)
# cv2.findContours()函数接受的参数为二值图，即黑白的（不是灰度图）,cv2.RETR_EXTERNAL只检测外轮廓，cv2.CHAIN_APPROX_SIMPLE只保留终点坐标
# 返回的list中每个元素都是图像中的一个轮廓和层级
refCnts, hierarchy = cv2.findContours(ref, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
img = cv2.drawContours(img.copy(), refCnts, -1, (0, 0, 255), 2)
cv_show('img', img)
print(np.array(refCnts).shape)