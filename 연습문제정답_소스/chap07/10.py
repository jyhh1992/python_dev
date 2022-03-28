import numpy as np, cv2
from Common.filters import filter

image = cv2.imread("images/filter_sharpen.jpg") # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")

# 샤프닝 마스크 원소 지정
mask1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], np.float32)
mask2 = np.array([[1/9, 1/9, 1/9],
                  [1/9, 1/9, 1/9],
                  [1/9, 1/9, 1/9]], np.float32)

b, g, r = cv2.split(image)

filtered1 = [filter(b, mask1), filter(g, mask1), filter(r, mask1)]
filtered2 = [filter(b, mask2), filter(g, mask2), filter(r, mask2)]

dst1 = cv2.merge(filtered1)
dst2 = cv2.filter2D(image, cv2.CV_8U, mask1)
dst3 = cv2.merge(filtered2)
dst4 = cv2.filter2D(image, cv2.CV_8U, mask2)


cv2.imshow("image", image)
cv2.imshow("sharpen User", cv2.convertScaleAbs(dst1))
cv2.imshow("sharpen OpenCV", cv2.convertScaleAbs(dst2))
cv2.imshow("bluring User", cv2.convertScaleAbs(dst3))
cv2.imshow("bluring OpenCV", cv2.convertScaleAbs(dst4))

cv2.waitKey(0)