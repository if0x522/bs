import cv2 as cv
import numpy as np

def a():
    cv.namedWindow('123',cv.WINDOW_NORMAL)
    cv.namedWindow('223',cv.WINDOW_NORMAL)
#cv.namedWindow('323',cv.WINDOW_NORMAL)
capture = cv.VideoCapture(0)
ret,img = capture.read()
size = img.shape
s = 0.5
Dsize = (int(size[1]*s),int(size[0]*s))
ReImg = cv.resize(img,Dsize)
#mash = np.zeros((480,640),np.uint8)
#mash.fill(255)
#ReImg2 = ReImg(cv.copyTo(img,mash))
#ReImg2 = np.copyto(img,ReImg)
def b(img,ReImg):
    cv.imshow('123',ReImg)
    cv.imshow('223',img)
#    cv.imshow('323',ReImg2)
a()
b(img,ReImg)

while(True):
    if(cv.waitKey(20)&0xFF == 27):
        break
cv.destroyAllWindows()