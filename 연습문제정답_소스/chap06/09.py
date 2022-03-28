import numpy as np, cv2

def onChange(value):												# 트랙바 콜백 함수
    alpha = cv2.getTrackbarPos('image1', 'dst') / 100
    beta = cv2.getTrackbarPos('image2', 'dst') / 100

    dst[:, w:w+w] = cv2.addWeighted(image1, alpha, image2, beta, 0)
    cv2.imshow('dst', dst)


image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기

if image1 is None or image2 is None : raise Exception("영상 파일 읽기 오류 발생")

h, w = image1.shape[:2]
dst = cv2.repeat(image1, 1, 3 )
dst[:, w:w+w] = 0
dst[:, w*2:w*3] = image2

cv2.imshow('dst', dst)
cv2.createTrackbar("image1", 'dst', 0, 100, onChange)	# 트랙바 콜백 함수 등록
cv2.createTrackbar("image2" , 'dst', 0, 100, onChange)	# 트랙바 콜백 함수 등록
onChange(50)
cv2.waitKey(0)
