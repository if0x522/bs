import cv2 as cv
import numpy as np


id = ['林黛玉','贾宝玉','王熙凤']
cv.namedWindow('face',cv.WINDOW_NORMAL)
idlist = []
image = []
for name in id:
    if name == '林黛玉':
        li = 0
        namedir = 'ldy'
    elif name == '贾宝玉':
        li = 1
        namedir = 'jby'
    elif name == '王熙凤':
        li = 2
        namedir = 'wxf'
    for i in range(8):
        j=i+1
        src = 'faceimg/'+namedir+'/'+namedir+str(j)+'.jpg'
        print(src)
        img = cv.imread(src)
        img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
        img = cv.resize(img,(102,102))
        cv.imshow('face',img)
        image.append(img)
        idlist.append(li)
        cv.waitKey()
#print(idlist)
#recognizer = cv.face.LBPHFaceRecognizer_create()
#recognizer = cv.face.EigenFaceRecognizer_create()
#recognizer = cv.face.FisherFaceRecognizer_create()
recognizer = cv.face_FisherFaceRecognizer()
#recognizer.train(image,np.array(idlist))
recognizer.train(image,np.array(idlist))
ii = recognizer.getEigenValues()
cv.imshow('face',ii)
cv.waitKey()
#recognizer.save('face.xml')
for name in id:
    if name == '林黛玉':
        namedir = 'ldy'
    elif name == '贾宝玉':
        namedir = 'jby'
    elif name == '王熙凤':
        namedir = 'wxf'
    for i in range(2):
        j = i+9
        src = 'faceimg/'+namedir+'/'+namedir+str(j)+'.jpg'
        testimg = cv.imread(src)
        testimg = cv.cvtColor(testimg,cv.COLOR_RGB2GRAY)
        testimg = cv.resize(testimg,(102,102))
        print(name)
        print(src)
        lable, confidence = recognizer.predict(testimg)
        if lable==0:
            na = '林黛玉'
        elif lable==1:
            na = '贾宝玉'
        elif lable==2:
            na = '王熙凤' 
        lable = 5
        print('识别结果'+na)
        print('预测值'+str(confidence))
        cv.imshow('face',testimg)
        cv.waitKey()

cv.destroyAllWindows()

