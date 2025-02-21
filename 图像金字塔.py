import cv2

#图像金子塔的上下定义是图像的定义,上下采样都会损失信息
img = cv2.imread('2.jpg')
# 高斯金字塔
"""
up = cv2.pyrUp(img) # 上采样，向金字塔底部
down = cv2.pyrDown(img) # 下采样，向金字塔上部
test = cv2.pyrUp(img)
test = cv2.pyrDown(test) # 进行一次上采样，再进行一次下采样，上采样平均化，下采样损失精度，两次操作后，图像精度减少
cv2.imshow('test',test)
cv2.imshow('img',img)
"""

# 拉普拉斯金字塔
down = cv2.pyrDown(img)
print(down.shape)
up = cv2. pyrUp(down) # 这里会存在一个问题，如果输入的图像的长宽是奇数，再第一次down操作之后，会进半个单位的长度
print(up.shape + img.shape)
final = cv2.subtract(img, up)
cv2.imshow('final',final)
cv2.waitKey()