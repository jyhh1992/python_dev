import numpy as np, cv2

image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기

if image1 is None or image2 is None : raise Exception("영상 파일 읽기 오류 발생")

h, w = image1.shape[:2]
alpha, beta = 0.5, 0.5

dst = cv2.repeat(image1, 1, 3 )
dst[:, w:w+w] = cv2.addWeighted(image1, alpha, image2, beta, 0 )
dst[:, w*2:w*3] = image2

cv2.imshow('dst', dst)
cv2.waitKey(0)
