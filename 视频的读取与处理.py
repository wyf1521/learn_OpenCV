import cv2
# 我也不知道为啥输出的图像是倒过来的，查了一圈，说可以用cv2.flip处理
vc = cv2.VideoCapture('void.mp4')
if vc.isOpened():
    open, frame = vc.read()
else:
    open = False
while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', gray)
        if (cv2.waitKey(10) & 0xFF == 27):
            break
vc.release()
