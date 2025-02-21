import cv2

# cv2中读取图像是按照bgr的顺序读取的,uint8编码
img = cv2.imread('1.jpg')
b, g, r = cv2.split(img)
""""
print(b.shape)  # 大小
print(b.dtype)  # 编码方式
"""
new_img = cv2.merge((b, g, r))
cv2.imshow('img', new_img)

cur_img = img.copy()
cur_img[:, :, 0] = 0  # b
cur_img[:, :, 1] = 0  # g
cv2.imshow('cur_img', cur_img)  # 仅保留r
cv2.waitKey(0)
