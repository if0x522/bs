import cv2 as cv

# 调用摄像头
capture = cv.VideoCapture(0)
# 读入一帧
ret,frame = capture.read()
# 保存图片
cv.imwrite('images/face.jpg',frame)


