import cv2

image = cv2.imread("images/test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 에러")

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 100)  # JPEG 화질 설정
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 10]  # PNG 압축 레벨 설정

cv2.imshow('ex13', image)
cv2.waitKey()
## 행렬을 영상 파일로 저장
cv2.imwrite("images/write_test1.jpg", image, params_jpg)  # 지정 화질로 저장
cv2.imwrite("images/write_test2.png", image, params_png)
print("저장 완료")