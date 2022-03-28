import numpy as np, cv2, math

def draw_houghLines(src, lines, nline):
    if len(src.shape) <3:
        cv2.cvtColor(src, cv2.COLOR_GRAY2BGR, src)  # 컬러 영상 변환

    for i in range(min(len(lines), nline)):
        rho, radian = lines[i, 0, 0:2]  # 수직거리 , 각도 - 3차원 행렬임
        a, b = math.cos(radian), math.sin(radian)
        pt = (a * rho, b * rho)  # 검출 직선상의 한 좌표 계산
        delta = (-1000 * b, 1000 * a)  # 직선상의 이동 위치
        pt1 = np.add(pt, delta).astype('int')
        pt2 = np.subtract(pt, delta).astype('int')
        cv2.line(src, tuple(pt1), tuple(pt2), (0, 255, 0), 2, cv2.LINE_AA)

capture = cv2.VideoCapture(0)  # 0번 카메라 연결
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받기
    if not ret: break

    rho, theta = 1, np.pi / 180
    blur = cv2.GaussianBlur(frame, (5, 5), 2, 2)
    canny = cv2.Canny(blur, 100, 200, 5)
    lines = cv2.HoughLines(canny, rho, theta, 80)
    draw_houghLines(frame, lines, 5)

    if cv2.waitKey(30) >= 0: break
    cv2.imshow("ex17", frame)  # 윈도우에 영상 띄우기
capture.release()