import numpy as np, cv2, math
from Common.hough import accumulate, masking, select_lines
import pickle

def houghLines(src, rho, theta, thresh):
    acc_dst = masking(acc_mat, 7, 3, thresh)  # 마스킹 처리 7행,3열
    lines = select_lines(acc_dst, rho, theta, thresh)  # 직선 가져오기
    return lines

def draw_houghLines(src, lines, nline):
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)  # 컬러 영상 변환
    min_length = min(len(lines), nline)

    for i in range(min_length):
        rho, radian = lines[i, 0, 0:2]  # 수직거리 , 각도 - 3차원 행렬임
        a, b = math.cos(radian), math.sin(radian)
        pt = (a * rho, b * rho)  # 검출 직선상의 한 좌표 계산
        delta = (-1000 * b, 1000 * a)  # 직선상의 이동 위치
        pt1 = np.add(pt, delta).astype('int')
        pt2 = np.subtract(pt, delta).astype('int')
        cv2.line(dst, tuple(pt1), tuple(pt2), (0, 255, 0), 2, cv2.LINE_AA)

    return dst

with open('data.pickle', 'rb') as f:
    acc_mat = pickle.load(f)

rho, theta = 1,  np.pi / 180
lines1 = houghLines(acc_mat, rho, theta, 80)

image = cv2.imread('images/hough.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")

dst1 = draw_houghLines(image, lines1, 7)

cv2.imshow("image", image)
cv2.imshow("detected lines", dst1)
cv2.waitKey(0)