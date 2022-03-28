import cv2
from Common.filters import differential

image = cv2.imread("images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1, 0, 0,    0, 1, 0,    0, 0, 0]     # 로버츠 마스크
data2 = [ 0, 0, -1,   0, 1, 0,    0, 0, 0]
data3 = [-1, 0, 1,   -1, 0, 1,   -1, 0, 1]     # 프리웻 마스크
data4 = [-1,-1,-1,    0, 0, 0,    1, 1, 1]
data5 = [-1, 0, 1,   -2, 0, 2,   -1, 0, 1]     # 소벨 마스크
data6 = [-1, -2, -1,  0, 0, 0,    1, 2, 1]

dst1, _, _ = differential(image, data1, data2)  # 두 방향 회선 및 크기(에지 강도) 계산
dst2, _, _ = differential(image, data3, data4)  # 두 방향 회선 및 크기(에지 강도) 계산
dst3, _, _ = differential(image, data5, data6)  # 두 방향 회선 및 크기(에지 강도) 계산

cv2.imshow("roberts edge", dst1)
cv2.imshow("prewitt edge", dst2)
cv2.imshow("sobel edge", dst3)
cv2.waitKey(0)