import cv2 as cv


def get_img_info(image):
    # image.shape   --获取图片像素数
    print(image.shape)
    # image.size   --获取图片大小
    print(image.size)
    print(image.dtype)

def face_find(src,resrc,s):
    # 图片转换为灰度图
    gray = cv.cvtColor(resrc,cv.COLOR_BGR2GRAY)
    # 载入人脸特征数据
    #face_datector = cv.CascadeClassifier('if0x522-opencv-master/opencv/data/haarcascades/haarcascade_frontalface_alt_tree.xml')
    ee = 'if0x522-opencv-master/opencv/data/haarcascades_cuda/haarcascade_eye.xml'
    cc = 'if0x522-opencv-master/opencv/data/haarcascades_cuda/haarcascade_frontalface_alt2.xml'
    face_datector = cv.CascadeClassifier(cc)
    eye_datector = cv.CascadeClassifier(ee)
    # 人脸检测
    faces = face_datector.detectMultiScale(gray,1.07,5)
    print(faces)
    for x,y,w,h in faces:
        face_img = gray[y:(y+h),x:(x+w)]
        eyes = eye_datector.detectMultiScale(face_img,1.06,5,cv.CASCADE_SCALE_IMAGE,(20,20))
        x = int(x/s)
        y = int(y/s)
        w = int(w/s)
        h = int(h/s)
        cv.rectangle(src,(x,y),(x+w,y+h),(255,0,0),2)
        for ex,ey,ew,eh in eyes:
            ex = int(ex/s+x)
            ey = int(ey/s+y)
            ew = int(ew/s)
            eh = int(eh/s)
            cv.rectangle(src,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)
        
    cv.imshow('face',src)

# 读入图片
#src = cv.imread('./images/face.jpg')
# 创建窗口
#cv.namedWindow('123.jpg',cv.WINDOW_NORMAL)
cv.namedWindow('face',cv.WINDOW_NORMAL)
# 设置全屏化显示
cv.namedWindow(winname,flags)
#cv.setWindowProperty('123.jpg',cv.WND_PROP_FULLSCREEN,cv.WINDOW_FULLSCREEN)
# 图片显示
#cv.imshow('123.jpg',src)
cv.setWindowProperty(winname,prop_id,prop_value)
# 调用摄像头
capture = cv.VideoCapture(0)
while(True):
    # 读入一帧
    ret,frame = capture.read()
    #frame = cv.flip(frame,1)
    size = frame.shape
    s = 0.4
    print(size[0])
    print(size[1])
    print(size[2])
    dsize = (int(size[1]*s),int(size[0]*s))
    reframe = cv.resize(frame,dsize)
    print(reframe.shape)
    face_find(frame,reframe,s)
    if cv.waitKey(20)&0xFF == 27:
        break
#get_img_info(src)

# 循环按esc退出
#while(True):
 #   if cv.waitKey(20)&0xFF == 27:
#        break
# 安全关闭
cv.destroyAllWindows()
