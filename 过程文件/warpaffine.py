import cv2
#import matplotlib.pyplot as plt
import numpy as np

def cv_show(name,img):
    """图像显示函数
    name：字符串，窗口名称
    img：numpy.ndarray，图像
    """
    cv2.namedWindow(name,cv2.WINDOW_NORMAL)
    cv2.imshow(name,img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()

def img_show(name,img):
    """matplotlib图像显示函数
    name：字符串，图像标题
    img：numpy.ndarray，图像
    """
    if len(img.shape) == 3:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#    plt.imshow(img,'gray')
    #plt.xticks([])
    #plt.yticks([])
#    plt.xlabel(name,fontproperties='FangSong',fontsize=12)
    
def rotate_bound(image,angle):
    #获取图像的尺寸
    #旋转中心
    (h,w) = image.shape[:2]
    (cx,cy) = (w/2,h/2)
    
    #设置旋转矩阵
    M = cv2.getRotationMatrix2D((cx,cy),-angle,1.0)
    cos = np.abs(M[0,0])
    sin = np.abs(M[0,1])
    
    # 计算图像旋转后的新边界
    nW = int((h*sin)+(w*cos))
    nH = int((h*cos)+(w*sin))
    
    # 调整旋转矩阵的移动距离（t_{x}, t_{y}）
    M[0,2] += (nW/2) - cx
    M[1,2] += (nH/2) - cy
    
    return cv2.warpAffine(image,M,(nW,nH))



if __name__=="__main__":

    img1 = cv2.imread("images/ldy/ldy6.jpg")
    img2 = rotate_bound(img1,20)
    cv_show('rotate15',img2)
    cv_show("fdsfds",img1)
    cv2.waitKey()
    cv2.destroyAllWindows()
#    plt.figure(figsize=(12,8),dpi=80)
#    plt.subplot(121)
#    img_show('原图',img1)
#    plt.subplot(122)
#    img_show('顺时针旋转20°',img2)