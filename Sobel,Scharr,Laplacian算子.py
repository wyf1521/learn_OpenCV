import cv2

img = cv2.imread('1.jpg')


# scharr算子相比sobel算子，灵敏度更高一点
def Sobelxy():
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, 3)
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, 3)
    sobel_y = cv2.convertScaleAbs(sobel_y)
    sobel_x = cv2.resize(sobel_x, (0, 0), fx=0.5, fy=0.5)  # 比例缩放
    sobel_y = cv2.resize(sobel_y, (0, 0), fx=0.5, fy=0.5)  # 比例缩放
    sobel_xy = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)  # 分开计算dx和dy效果会更好
    return sobel_xy


def Scharrxy():
    Scharr_x = cv2.Scharr(img, cv2.CV_64F, 1, 0, 3)
    Scharr_x = cv2.convertScaleAbs(Scharr_x)
    Scharr_y = cv2.Scharr(img, cv2.CV_64F, 0, 1, 3)
    Scharr_y = cv2.convertScaleAbs(Scharr_y)
    Scharr_x = cv2.resize(Scharr_x, (0, 0), fx=0.5, fy=0.5)  # 比例缩放
    Scharr_y = cv2.resize(Scharr_y, (0, 0), fx=0.5, fy=0.5)  # 比例缩放
    Scharr_xy = cv2.addWeighted(Scharr_x, 0.5, Scharr_y, 0.5, 0)  # 分开计算dx和dy效果会更好
    return Scharr_xy


def Laplacian():
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)
    laplacian = cv2.resize(laplacian, (0, 0), fx=0.5, fy=0.5)
    return laplacian


sobel_xy = Sobelxy()
scharr_xy = Scharrxy()
laplacian = Laplacian()
cv2.imshow('sobel', sobel_xy)
cv2.imshow('scharr', scharr_xy)
cv2.imshow('laplacian', laplacian)
cv2.waitKey(0)
