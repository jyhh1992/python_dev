import cv2
from Common.utils import put_string

def bright_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_BRIGHTNESS, value) # 줌 설정

def contrast_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_CONTRAST, value)

capture = cv2.VideoCapture(0)								# 0번 카메라 연결
if capture.isOpened() is None: raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)      # 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)     # 카메라 프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)          # 오토포커싱 중지
capture.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)          # 오토포커싱 중지
capture.set(cv2.CAP_PROP_AUTO_WB, 0)          # 오토포커싱 중지

title = "ex15"              # 윈도우 이름 지정
cv2.namedWindow(title)                          # 윈도우 생성 - 반드시 생성 해야함
cv2.createTrackbar("bright" , title, 0, 200, bright_bar)
cv2.createTrackbar("contrast", title, 0, 20, contrast_bar)

while True:
    ret, frame = capture.read()                 # 카메라 영상 받기
    if not ret or cv2.waitKey(30) >= 0: break

    bright = int(capture.get(cv2.CAP_PROP_BRIGHTNESS))
    contrast = int(capture.get(cv2.CAP_PROP_CONTRAST))
    put_string(frame, "bright : " , (10, 240), bright)   # 줌 값 표시
    put_string(frame, "contrast : ", (10, 270), contrast)    # 초점 값 표시
    cv2.imshow(title, frame)

capture.release()