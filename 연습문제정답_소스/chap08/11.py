import numpy as np,  cv2
from Common.interpolation import bilinear_value
from Common.utils import contain   , ck_time               # 사각형으로 범위 확인 함수

def rotate_pt(img, degree, pt):
    dst = np.zeros(img.shape[:2], img.dtype)                     # 목적 영상 생성
    radian = (degree/180) * np.pi                               # 회전 각도 - 라디언
    sin, cos = np.sin(radian), np.cos(radian)   # 사인, 코사인 값 미리 계산

    for i in range(img.shape[0]):                              # 목적 영상 순회 - 역방향 사상
        for j in range(img.shape[1]):
            jj, ii = np.subtract((j, i), pt)                # 중심좌표 평행이동,
            y = -jj * sin + ii * cos               # 회선 변환 수식
            x =  jj * cos + ii * sin
            x, y = np.add((x, y), pt)
            if contain((y, x), img.shape):                      # 입력 영상의 범위 확인
                dst[i, j] = bilinear_value(img, [x, y])           # 화소값 양선형 보간
    return dst

image = cv2.imread('images/rotate.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일을 읽기 에러")

pt = (100,100)
angle = 30

rot_mat = cv2.getRotationMatrix2D(pt, angle, 1)
dst1 = rotate_pt(image, -angle, pt )                             # 영상 중심 기준 회전 변환
dst2 = cv2.warpAffine(image, rot_mat, image.shape[::-1], cv2.INTER_LINEAR)

cv2.imshow("ex11", image)
cv2.imshow("dst1-rotate_pt()", dst1)
cv2.imshow("dst2-warpAffine()", dst2)
cv2.waitKey(0)