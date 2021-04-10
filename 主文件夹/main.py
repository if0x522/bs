import cv2 as cv
import numpy as np 
import os
import urllib.parse
import socket
import webserver
import facefind
import threading


# image resize date
Resize_x=0
Resize_y=0 
# resize s
s = 0.6
bz = 0
NameList = []
datew = cv.imread('a.jpg')
facedate = 'fenleiqi/haarcascade_frontalface_alt2.xml'
FacesDateCtor = cv.CascadeClassifier(facedate)
EyesClass = 'fenleiqi/haarcascade_eye.xml'
EyesDateCtor = cv.CascadeClassifier(EyesClass)

class myThread(threading.Thread):
    def run(self):
        engine = facefind.InitPyttsx()
        while(True):
            if bz == 1:
                name1 = facefind.shiBie(datew,recognizer)
                facefind.PyttsxSay(engine,name1)
                bz = 0


def findAndDispaly():
    capture = facefind.CaptureOpen()
    image = facefind.ImgInput(capture)
    facefind.InifImg(image)
    facefind.dispalyInit(1)
    while(True):
        image = facefind.ImgInput(capture)
        imageF = facefind.FacesFind(image)
        if imageF==0:
            facefind.DisPaly(image,0)
        else:
            bz = 1
            datew = imageF
            facefind.DisPaly(image,imageF)
        if cv.waitKey(20)&0xFF == 27:
            break
    facefind.CaptureClose(capture)
    facefind.dispalyInit(0)


s,sok = webserver.WebInit()
if s == None:
    while(True):
        webserver.Urls(sok)
else:
    recognizer = facefind.XunLian()
    thread1 = myThread()
    thread1.start()
    findAndDispaly()
