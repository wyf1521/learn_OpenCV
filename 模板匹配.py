import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg', 0)
template = cv2.imread('foot.jpg', 0)
h, w = template.shape[:2]
res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF)
# print(res.shape) # 长和宽
min_val, max_val, min_loc, amx_loc = cv2.minMaxLoc(res)
# print(min_loc) # 定位左上角的点，结合长宽，矩形就可以画出来
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF',
           'cv2.TM_SQDIFF_NORMED']
for meth in methods:
    img2 = img.copy()
    method = eval(meth)
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1]+h)
    cv2.rectangle(img2, top_left, bottom_right, 255, 2)

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img2, cmap='gray')
    plt.suptitle(meth)
    plt.show()