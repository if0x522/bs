import cv2 as cv
import numpy as np 


def findface(img):
    # 图片转换为灰度图
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # 载入人脸特征数据
#    face_datector = cv.CascadeClassifier('if0x522-opencv-master/opencv/data/lbpcascades/lbpcascade_frontalface_improved.xml')
#    face_datector = cv.CascadeClassifier('if0x522-opencv-master/opencv/data/lbpcascades/lbpcascade_frontalface.xml')
    cc = 'if0x522-opencv-master/opencv/data/haarcascades_cuda/haarcascade_frontalface_alt2.xml'
    face_datector = cv.CascadeClassifier(cc)
    # 人脸检测
    faces = face_datector.detectMultiScale(gray,1.07,5)
    return faces
jj = 1
for j in range(10):
    j +=1
#    src = 'images/ldy/ldy'+str(j)+'.jpg'
#    src = 'images/wxf/wxf'+str(j)+'.jpg'
    src = 'images/jby/jby'+str(j)+'.jpg'
#    src = 'images/test/t'+str(j)+'.jpg'
    cv.namedWindow('photo',cv.WINDOW_NORMAL)
#    src = 'images/ldy/ldy1.jpg'
    img = cv.imread(src)
    face = findface(img)
    i = 0
    for x,y,w,h in face:
        facewidname = "face" + str(i)
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        face_one = img[y:(y+h),x:(x+w)]
        resrc = 'faceimg/jby/jby'+str(jj)+'.jpg'
        jj+=1
        cv.namedWindow(facewidname,cv.WINDOW_NORMAL)
        cv.imshow(facewidname,face_one)
        cv.imwrite(resrc,face_one)
        i+=1
    cv.imshow('photo',img)
    ky = cv.waitKey()
    if ky == 65:
        cv.destroyAllWindows()
    elif ky == 27:
        break

cv.destroyAllWindows()







cv.imshow('face',img)
