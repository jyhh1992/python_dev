import numpy as np,  cv2
from Common.interpolation import bilinear_value
from Common.utils import contain            # 사각형으로 범위 확인 함수

def rotate(img, degree):
    dst = np.zeros(img.shape, img.dtype)                     # 목적 영상 생성
    radian = (degree/180) * np.pi                               # 회전 각도 - 라디언
    sin, cos = np.sin(radian), np.cos(radian)   # 사인, 코사인 값 미리 계산

    for i in range(img.shape[0]):                                       # 목적 영상 순회 - 역방향 사상
        for j in range(img.shape[1]):
            y = -j * sin + i * cos
            x =  j * cos + i * sin                  # 회선 변환 수식
            if contain((y, x), img.shape):             # 입력 영상의 범위 확인
                dst[i, j, 0] = bilinear_value(img[:,:,0], [x, y])           # 화소값 양선형 보간
                dst[i, j, 1] = bilinear_value(img[:,:,1], [x, y])  # 화소값 양선형 보간
                dst[i, j, 2] = bilinear_value(img[:,:,2], [x, y])  # 화소값 양선형 보간
    return dst

image = cv2.imread('images/rotate.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일을 읽기 에러")

dst = rotate(image, 20)                                        # 원점 기준 회전 변환

cv2.imshow("image", image)
cv2.imshow("ex12", dst)
cv2.waitKey()