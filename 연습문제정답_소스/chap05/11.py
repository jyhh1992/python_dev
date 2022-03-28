import cv2, numpy as np
from Common.utils import put_string

capture = cv2.VideoCapture(0)  # 0번 카메라 연결
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)      # 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)     # 카메라 프레임 높이

x,y,w,h = (30,30, 320,240)
blue = np.full( (360, 640, 3) , (255,0,0) , np.uint8 )
mask = np.full( (360, 640) , 0 , np.uint8 )
cv2.rectangle(mask, (x,y,w,h), 255, -1 )


while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받기
    if not ret: break
    cv2.rectangle(frame, (x,y,w,h), (0,0,255), 2 )

    inner = cv2.bitwise_and(frame, frame, mask=mask)  # 로고의 전경 복사
    outter = cv2.bitwise_and(blue, blue, mask=~mask)  # 로고의 전경 복사

    if cv2.waitKey(30) >= 0: break
    cv2.imshow("ex11 - mainWindow", inner+outter)  # 윈도우에 영상 띄우기
    cv2.resizeWindow("ex11 - mainWindow", 400, 300)

capture.release()