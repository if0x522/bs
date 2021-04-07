import cv2 as cv



src = '123/f01.jpg'
img = cv.imread(src)
img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
img = cv.resize(img,(102,102))
cv.imwrite('123/f01.png',img)
