import cv2 as cv
import numpy as np
import os
import pyttsx3


# image resize date
Resize_x=0
Resize_y=0 
# resize s
s = 0.6

NameList = []

def CaptureOpen():
    capture = cv.VideoCapture(0)
    while True:
        if(capture.isOpened()):
            return(capture)
        else:
            if(capture.open(0)):
                return(capture)

def CaptureClose(capture):
    capture.release()

def ImgInput(capture):
    while True:
        ret,img=capture.read()
        if ret:
            return(img)


def InifImg(img):
    size = img.shape
    global Resize_x,Resize_y
    Resize_x = int(size[1]*s)
    Resize_y = int(size[0]*s)

def ResizeImg(img)
    Gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    Dsize = (Resize_x,Resize_y)
    ReImg = cv.resize(Gray,Dsize)
    return(ReImg,Gray)

def FacesFind(img):
    ReImg,Gray = ResizeImg(img,)
    Faces = FacesDateCtor.detectMultiScale(ReImg,1.07,5)
    for x,y,w,h in Faces:
        FaceImgBgr = img[(y-7)//0.6:(y+h+7)//0.6,(x-7)//0.6:(x+w+7)//0.6]
        FaceImgGray = img[(y-7):(y+h+7),(x-7):(x+w+7)]
        EyesXy = EyesFind(FaceImgGray)
        LRW = EyesXy[1][0]-EyesXy[0][0]
        LRH = EyesXy[1][1]-EyesXy[1][0]
        Center = ((EyesXy[0][0]+EyesXy[1][0])//1.2,(EyesXy[1][0]+EyesXy[1][1])//1.2)
        TanA = LRh/LRW
        A = np.arctan(TanA)
        M_1 = cv.getRotationMatrix2D(Center,np.degrees(A),1)
        FaceImg = cv.warpAffine(FaceImgBgr,M_1,((w+7)//0.6,(h+7)//0.6))
        GrayFace = cv.cvtColor(FaceImg,cv.COLOR_BGR2GRAY)
        Face = FacesDateCtor.detectMultiScale(GrayFace,1.07,5)
        FaceBgr = FaceImg[x:(x+w),y:(y+h)]
        return(FaceBgr)


def EyesFind(faceimg):
    Eyes = EyesClass.detectMultiScale(ReImg,1.06,5,cv.CASCADE_SCALE_IMAGE,(20,20))
    i = 0
    EyesXy = [[0,0],[0,0]]
    for x,y,w,h in Eyes:
        EyesXy[i] = [x+w//2,y+h//2]
        i+=1
    return(EyesXy)

def XunLian():
    global NameList
    NameList = os.listdir('date/')
    images = []
    idlist = []
    i = 0
    for Name in NameList:
        imagesDir = os.listdir('date/'+Name+'/')
        for image in imagesDir:
            src = 'date/'+Name+'/'+image
            imageFace = cv.imread(src)
            images.append(imageFace)
            idlist.append(i)
        i+=1
    recognizer = cv.face_FisherFaceRecognizer()
    recognizer.train(images,np.array(idlist))
    return(recognizer)

def shiBie(img,recognizer):
    img = GuiYi(img)
    lable, confidence = recognizer.predict(img)
    return(NameList[lable])

def GuiYi(img):
    img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img = cv.resize(img,(102,102))
    return(img)

def InitPyttsx():
    engine = pyttsx3.init()
    engine.setProperty('voice','zh')
    engine.setProperty('rate',rate-20)
    return(engine)

def PyttsxSay(engine,name):
    msg = name+'来了'
    engine.say(msg)

def dispalyInit(s):
    if s==1:
        cv.namedWindow('dispaly',cv.WINDOW_NORMAL)
        cv.setWindowProperty('dispaly',cv.WND_PROP_FULLSCREEN,cv.WINDOW_FULLSCREEN)
    else:
        cv.destroyAllWindows()

def DisPaly(img):
    cv.imshow('dispaly',img)

facedate = 'if0x522-opencv-master/opencv/data/haarcascades_cuda/haarcascade_frontalface_alt2.xml‘
FacesDateCtor = cv.CascadeClassifier(facedate)
EyesClass = 'if0x522-opencv-master/opencv/data/haarcascades_cuda/haarcascade_eye.xml'
EyesDateCtor = cv.CascadeClassifier(EyesClass)

