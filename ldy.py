import cv2 as cv

def face_find(src):
    # 图片转换为灰度图
    gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    # 载入人脸特征数据
    face_datector = cv.CascadeClassifier('if0x522-opencv-master/opencv/data/haarcascades/haarcascade_frontalface_alt_tree.xml')
    # 人脸检测
    faces = face_datector.detectMultiScale(gray,1.1,1)
    print(faces)
    for x,y,w,h in faces:
        cv.rectangle(src,(x,y),(x+w,y+h),(255,0,0),2)
    cv.imshow('face',src)

src = 'images/jby/jby10.jpg'
#src = 'images/ldy/ldy'+str(2)+'.jpg'
cv.namedWindow('face',cv.WINDOW_NORMAL)
img = cv.imread(src)
face_find(img)
if cv.waitKey()&0xFF == 27:
    cv.destroyAllWindows()
