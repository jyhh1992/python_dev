import numpy as np, cv2, math

def draw_houghLines(src, lines, nline):
    if src.ndim <3:
        dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)  # 컬러 영상 변환
    else:
        dst = src.copy()

    for i in range(min(len(lines), nline)):
        rho, radian = lines[i, 0, 0:2]  # 수직거리 , 각도 - 3차원 행렬임
        a, b = math.cos(radian), math.sin(radian)
        pt = (a * rho, b * rho)  # 검출 직선상의 한 좌표 계산
        delta = (-1000 * b, 1000 * a)  # 직선상의 이동 위치
        pt1 = np.add(pt, delta).astype('int')
        pt2 = np.subtract(pt, delta).astype('int')
        cv2.line(dst, tuple(pt1), tuple(pt2), (0, 255, 0), 2, cv2.LINE_AA)
    return dst

image = cv2.imread('images/hough2.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 에러")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 2, 2)
canny = cv2.Canny(blur, 50, 150, 5)

rho, theta = 1, np.pi / 180
lines = cv2.HoughLines(canny, rho, theta, 80)
dst = draw_houghLines(image, lines, 10)

cv2.imshow("canny", canny)
cv2.imshow("detected lines", dst)
cv2.waitKey(0)
