import cv2 as cv
import numpy as np

#mod = cv.face.FisherFaceRecognizer_create()
#cv.namedWindow('face',cv.WINDOW_NORMAL)
#namelist = ['jby','ldy','wxf']
#mod.load('face.xml')
mod = cv.face_FisherFaceRecognizer.read('face.xml')
#for name in namelist:
#    for i in range(2):
#        j =i+9
#        src = 'faceimg'+name+'/'+name+str(j)+'.jpg'
img = cv.imread('faceimg/ldy/ldy9.jpg')
img = cv.resize(cv.cvtColor(img,cv.COLOR_BGR2GRAY),(102,102))
yname,ycon = mod.predict(img)
print(yname)
print(ycon)

