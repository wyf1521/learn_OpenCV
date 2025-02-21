import cv2

img = cv2.imread('1.jpg')
top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)
new_img_one = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,
                                 borderType=cv2.BORDER_REPLICATE)  # 复制边缘像素
new_img_two = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT)  # 复制边缘像素
new_img_three = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)  # 复制边缘像素
new_img_four = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)  # 复制边缘像素
new_img_five = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_CONSTANT,
                                  value=0)  # 复制边缘像素
# cv2.imshow('img', new_img_one)
# cv2.imshow('img', new_img_two)
# cv2.imshow('img', new_img_three)
# cv2.imshow('img', new_img_four)
# cv2.imshow('img', new_img_five)
cv2.waitKey(0)
