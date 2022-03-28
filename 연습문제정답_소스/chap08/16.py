import numpy as np, cv2
from Common.utils import contain_pts, put_string  # 좌표로 범위 확인 함수

def draw_rect(img):
    rois = [(p - small, small * 2) for p in pts1]
    for (x, y), (w, h) in np.int32(rois):
        roi = img[y:y + h, x:x + w]  # 좌표 사각형 범위 가져오기
        val = np.full(roi.shape, 80,
                      np.uint8)  # 컬러(3차원) 행렬 생성		cv2.add(roi, val, roi)                      			# 관심영역 밝기 증가
        cv2.add(roi, val, roi)
        cv2.rectangle(img, (x, y, w, h), (0, 255, 0), 1)
    cv2.polylines(img, [pts1.astype(int)], True, (0, 255, 0), 1)  # pts는 numpy 배열
    cv2.imshow(title, img)

def warp(img):
    perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, perspect_mat, (350, 400), cv2.INTER_CUBIC)
    cv2.imshow("perspective transform", dst)

def onMouse(event, x, y, flags, param):
    global check
    if event == cv2.EVENT_LBUTTONDOWN:
        for i, p in enumerate(pts1):
            p1, p2 = p - small, p + small  # p점에서 우상단, 좌하단 좌표생성
            if contain_pts((x, y), p1, p2): check = i

    if event == cv2.EVENT_LBUTTONUP: check = -1  # 좌표 번호 초기화

    if check >= 0:  # 좌표 사각형 선택 시
        pts1[check] = (x, y)
        draw_rect(np.copy(image))
        warp(image)

small = np.array((12, 12))  # 좌표 사각형 크기
check = -1  # 선택 좌표 사각형 번호 초기화
pts1 = np.float32([(100, 100), (300, 100), (300, 300), (100, 300)])
pts2 = np.float32([(0, 0), (400, 0), (400, 350), (0, 350)])  # 목적 영상 4개 좌표                         # 목적 영상 4개 좌표

capture = cv2.VideoCapture(0)  # 0번 카메라 연결
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

title = "ex16"
cv2.namedWindow(title)
cv2.setMouseCallback(title, onMouse, 0)

dst = np.full((400,350,3,),(255,255,255), np.uint8)
cv2.imshow("perspective transform", dst)

while True:  # 무한 반복
    ret, image = capture.read()  # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(30) >= 0: break
    draw_rect(np.copy(image))
capture.release()

