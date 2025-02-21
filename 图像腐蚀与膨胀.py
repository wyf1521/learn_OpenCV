import cv2
import numpy as np

img = cv2.imread('1.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度处理
h = gray_img.shape[0]
w = gray_img.shape[1]
# 获取高度和宽度
n = 0
m_g = 0

# 遍历每一个灰度层
for t in range(255):
    # 使用numpy直接对数组进行运算
    n0 = gray_img[np.where(gray_img < t)]
    n1 = gray_img[np.where(gray_img >= t)]
    # 把图像的灰度数按灰度级分成2个部分，使得两个部分之间的灰度值差异最大，每个部分之间的灰度差异最小
    w0 = len(n0) / (h * w)
    # 背景像素点占整幅图像的比例
    w1 = len(n1) / (h * w)
    # 前景像素点占整幅图像的比例
    u0 = np.mean(n0) if len(n0) > 0 else 0.
    # u0为w0平均灰度
    u1 = np.mean(n1) if len(n0) > 0 else 0.
    # u1为w1平均灰度
    g = w0 * w1 * (u0 - u1) ** 2
    #        μ=ω0 *μ0 +ω1 *μ1                       5
    #        g =ω0 * (μ0 -μ)2 +ω1 * (μ1 -μ)2        6
    #  ==>   g =ω0 *ω1 * (μ0 -μ1)2                  7 类间方差
    n = t if g > m_g else n
    m_g = g if g > m_g else m_g
gray_img[gray_img < n] = 0
gray_img[gray_img >= n] = 255
#二值化处理

gary_img = np.ones((3, 3), np.uint8)
res = cv2.erode(img, gray_img, iterations=1)# 腐蚀
res = cv2.dilate(img, gray_img, iterations=1)# 膨胀
#cv2.imshow('res', res)
# 时间亿点点长，2min
cv2.waitKey(0)
