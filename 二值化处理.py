import cv2
import numpy as np

img = cv2.imread("123.jpg").astype(np.float)
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()
out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)
th = 140
out[out < th] = 0
out[out >= th] = 255
# cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)