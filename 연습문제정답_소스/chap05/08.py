import numpy as np, cv2

image  = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)         # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 ")

mask = np.zeros(image.shape[:2], np.uint8)
center = (190,170)

cv2.ellipse(mask, center, (50, 80), 0, 0, 360, 255, -1)
dst = cv2.bitwise_and(image, image, mask = mask)

cv2.imshow("image", image)
cv2.imshow("dst", dst)
cv2.waitKey()