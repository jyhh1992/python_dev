import numpy as np, cv2

image  = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)         # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 ")

x,y,w,h = (50,50, 100,100)
cv2.rectangle(image, (x,y,w,h), (255,0,0), 2)

tmp = image[y:y + h, x:x + w]
img50 = np.full( tmp.shape, (50,50,50), np.uint8)
cv2.add(tmp, img50, tmp )

x,y,w,h = (300,200, 100,100)
cv2.rectangle(image, (x,y,w,h), (255,0,0), 2)

tmp = image[y:y + h, x:x + w]
noimage = np.full( tmp.shape, (50,50,50), np.uint8)
cv2.scaleAdd(tmp, 2.0, noimage, tmp)                # 영상대비 증가

cv2.imshow("image", image)
cv2.waitKey()