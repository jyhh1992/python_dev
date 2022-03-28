import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global pt1, pt2, mouse_mode

    if event == cv2.EVENT_LBUTTONUP:  # 왼쪽 버튼 떼기
        pt2 = (x, y)                        # 종료좌표 저장
        mouse_mode = 1                      # 버튼 떼기 상태 지정

        dx, dy = np.subtract(pt2, pt1).astype(float)
        angle = cv2.fastAtan2(dy, dx)
        print(angle)
        rot_mat = cv2.getRotationMatrix2D(pt1, -angle, 1)
        dst = cv2.warpAffine(image, rot_mat, image.shape[1::-1], cv2.INTER_LINEAR)
        cv2.imshow(title, dst)

    elif event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 버튼 누르기
        pt1 = (x, y)  # 시작좌표 저장
        mouse_mode = 2

    if mouse_mode >= 2:  # 왼쪽 버튼 누르기 또는 드래그
        pt2 = (x, y)
        tmp = np.copy(image)
        cv2.line(tmp, pt1, pt2, (255, 0, 0), 2)
        cv2.imshow(title, tmp)

image = cv2.imread('images/rotate.jpg', cv2.IMREAD_COLOR)
mouse_mode = 0

title = "ex13"
cv2.imshow(title, image)  # 윈도우에 영상 띄우기
cv2.setMouseCallback(title, onMouse)  # 마우스 콜백 함수 등록
cv2.waitKey(0)
