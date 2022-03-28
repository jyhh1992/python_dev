import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global title, image
    pt = (x, y)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, pt, 20, 100, thinkness)
        cv2.imshow(title, image)
    elif event== cv2.EVENT_LBUTTONDOWN:
        pt2 = (pt[0]+30 , pt[1] +30)
        cv2.rectangle(image, pt, pt2, 100, thinkness)
        cv2.imshow(title, image)

def onChange(value):
    global thinkness
    thinkness = value

image = np.ones((300, 300), np.uint8) * 255
title = "ex11"
thinkness = 2
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.createTrackbar("thinkness", title, thinkness, 10, onChange)	# 트랙바 콜백 함수 등록
cv2.waitKey(0)
