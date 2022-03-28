import numpy as np, cv2
from Common.filters import filter

def onTrackbar(value):
    th1 = cv2.getTrackbarPos('th1','canny edge')
    th2 = cv2.getTrackbarPos('th2', 'canny edge')

    canny = cv2.Canny(image, th1, th2)
    cv2.imshow("canny edge", canny)

image = cv2.imread("images/canny_track.jpg") # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")

cv2.imshow("canny edge", image)
cv2.createTrackbar("th1", "canny edge", 50, 255, onTrackbar)  # 콜백 함수 등록
cv2.createTrackbar("th2", "canny edge", 100, 255, onTrackbar)  # 콜백 함수 등록
onTrackbar(50)

cv2.waitKey(0)