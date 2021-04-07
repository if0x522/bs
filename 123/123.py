import cv2
import numpy as np
images=[]
images.append(cv2.resize(cv2.imread("faceimg/jby/jby1.jpg", cv2.IMREAD_GRAYSCALE),(102,102)))
images.append(cv2.resize(cv2.imread("faceimg/jby/jby3.jpg", cv2.IMREAD_GRAYSCALE),(102,102)))
images.append(cv2.resize(cv2.imread("faceimg/ldy/ldy2.jpg", cv2.IMREAD_GRAYSCALE),(102,102)))
images.append(cv2.resize(cv2.imread("faceimg/ldy/ldy3.jpg", cv2.IMREAD_GRAYSCALE),(102,102)))
labels=[0,0,1,1]
#print(labels)
recognizer = cv2.face.EigenFaceRecognizer_create()
recognizer.train(images, np.array(labels))
predict_image=cv2.resize(cv2.imread("faceimg/ldy/ldy5.jpg", cv2.IMREAD_GRAYSCALE),(102,102))
label, confidence= recognizer.predict(predict_image)
print("label=", label)
print("confidence=", confidence)


