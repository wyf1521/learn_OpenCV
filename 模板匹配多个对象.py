import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg',0)
template = cv2.imread('face.jpg',0)
h,w=template.shape[::-1]
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res>=threshold)
for pt  in zip(*loc[::-1]):
    bottom_right = (pt[0]+w,pt[1]+h)
    cv2.rectangle(img,pt,bottom_right,255,3)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
plt.imshow(img,cmap='gray')
plt.xticks([]),plt.yticks([])
plt.show()