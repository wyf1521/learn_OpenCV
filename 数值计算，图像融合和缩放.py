import cv2

img_1 = cv2.imread('1.jpg')
"""
img_2 = img_1 + 10
img_1 += img_2  # 自动%256,确保在0-255范围内
# cv2.imshow(' ', img_1)
new_img = cv2.add(img_1, img_2)  # 超过255则复制为255,不进行%256操作
print(new_img)
"""
img_2 = cv2.imread('2.jpg')
print(img_1.shape)
img_2 = cv2.resize(img_2, (1429, 1411))
res = cv2.addWeighted(img_1, 0.4, img_2, 0.6, 0)
res = cv2.resize(res, (0, 0), fx=0.5, fy=0.5) # 比例缩放
cv2.imshow('res', res)
cv2.waitKey(0)
