from paint_init05 import *
from paint_utils import *

def onMouse(event, x, y, flags, param):

    global pt1, pt2, mouse_mode, draw_mode, fkey

    if event == cv2.EVENT_LBUTTONUP:  # 왼쪽 버튼 떼기
        for i, (x0, y0, w, h) in enumerate(icons):  # 메뉴아이콘 사각형 조회
            if x0 <= x < x0+ w and y0 <= y < y0 + h:  # 메뉴 클릭 여부 검사
                if i < 6:                   # 그리기 명령이면
                    mouse_mode = 0          # 마우스 상태 초기화
                    draw_mode = i           # 그리기 모드
                else:
                    command(i)              # 일반 명령이면
                return

        pt2 = (x, y)                        # 종료좌표 저장
        mouse_mode = 1                      # 버튼 떼기 상태 지정

    elif event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 버튼 누르기
        pt1 = (x, y)  # 시작좌표 저장
        mouse_mode = 2

    if mouse_mode >= 2:  # 왼쪽 버튼 누르기 또는 드래그
        mouse_mode = 0 if x < 125 else 3  # 메뉴 영역 확인- 마우스 상태 지정
        pt2 = (x, y)
        fkey= flags

def draw(image, color=(200, 200, 200)):
    global draw_mode, thickness, pt1, pt2, fkey

    if draw_mode == DRAW_RECTANGLE:                 # 사각형 그리기
        cv2.rectangle(image, pt1, pt2, color, thickness)

    elif draw_mode == DRAW_LINE:                    # 직선 그리기
        cv2.line(image, pt1, pt2, color, thickness)

    elif draw_mode == DRAW_BRUSH:                   # 브러시 그리기
        cv2.line(image, pt1, pt2, color, thickness * 3)
        pt1 = pt2                               # 종료 좌표를 시작 좌표로 지정

    elif draw_mode == ERASE:                        # 지우개
        cv2.line(image, pt1, pt2, (255, 255, 255), thickness * 5)
        pt1 = pt2

    elif draw_mode == DRAW_CIRCLE or draw_mode == DRAW_ECLIPSE:

        if (fkey&cv2.EVENT_FLAG_ALTKEY) >0:

            center = np.abs(np.add(pt1, pt2)) // 2      # 두 좌표의 중심점 구하기
            size = np.abs(np.subtract(pt1, pt2)) // 2   # 두 좌표의 크기의 절반
            size = (max(size),max(size))
            cv2.ellipse(image, tuple(center), tuple(size), 0, 0, 360, color, thickness)
        else :
            center = np.abs(np.add(pt1, pt2)) // 2      # 두 좌표의 중심점 구하기
            size = np.abs(np.subtract(pt1, pt2)) // 2   # 두 좌표의 크기의 절반
            cv2.ellipse(image, tuple(center), tuple(size), 0, 0, 360, color, thickness)

    cv2.imshow("PaintCV", image)

def command(mode):
    global icons, image, canvas, Color, hue, mouse_mode

    if mode == PALETTE:  # 색상팔레트 영역 클릭 시
        pixel = image[pt2[::-1]]
        x, y, w, h = icons[COLOR]
        image[y:y + h - 1, x:x + w - 1] = pixel
        Color = tuple(map(int, pixel))

    elif mode == HUE_IDX:  # 색상인텍스 클릭 시
        create_colorPlatte(image, pt2[0], icons[PALETTE])  # 팔레트 새로 그리기

    elif mode == OPEN:                                   # 영상 파일 열기
        tmp = cv2.imread("images/my_picture.jpg", cv2.IMREAD_COLOR)
        cv2.resize(tmp, canvas.shape[1::-1], canvas)

    elif mode == SAVE:                                  # 캔버스 영역 저장
        cv2.imwrite("images/my_save.jpg", canvas)

    elif mode == PLUS:                                  # 캔버스 영상 밝게 변경
        val = np.full(canvas.shape, 10, np.uint8)     # 증가 화소값 행렬 생성
        cv2.add(canvas, val, canvas)

    elif mode == MINUS:                                 # 캔버스 영상 어둡게 변경
        val = np.full(canvas.shape, 10, np.uint8)     # 증가 화소값 행렬 생성
        cv2.subtract(canvas, val, canvas)

    elif mode == CREAR:                                 # 캔버스 영역 전체 지우기
        canvas[:] = (255, 255, 255)                     # 캔버스를 흰색으로
        mouse_mode = 0                                  # 마우스 상태 초기화

##----------------------------------------------------------------------
    elif mode == SCALEUP:
        tmp = cv2.resize(canvas, (0,0), fx=1.1, fy=1.1)
        h0, w0 = np.subtract(tmp.shape[:2], canvas.shape[:2])//2
        h, w = tmp.shape[:2]
        val = np.zeros(canvas.shape, np.uint8)
        cv2.add(tmp[h0:h-h0, w0:w-w0], val, canvas)

    elif mode == SCALEDOWN:
        tmp = cv2.resize(canvas, (0,0), fx=0.9, fy=0.9)
        h0, w0 = np.subtract(canvas.shape[:2], tmp.shape[:2])//2
        h, w = canvas.shape[:2]
        canvas[:] = (255, 255, 255)
        canvas[h0:h - h0, w0:w - w0] = tmp
##----------------------------------------------------------------------

    cv2.imshow("PaintCV", image)

def onTrackbar(value):                                   # 트랙바 콜백 함수
    global mouse_mode, thickness
    mouse_mode = 0                                       # 마우스 상태 초기화
    thickness = value

fkey = 0
image = np.full((600, 800, 3), 255, np.uint8)         # 연습문제 수정
icons = place_icons(image, (60, 60))
x, y, w, h = icons[-1]

icons.append((0, y + h + 2  , 120, 120) )      # 팔레트 사각형 추가
icons.append((0, y + h + 124, 120, 15))  # 색상인덱스 사각형 추가
create_colorPlatte(image, 0, icons[PALETTE])    # 팔레트 생성
create_hueIndex(image, icons[HUE_IDX])                      # 색상인텍스 생성

cv2.imshow("PaintCV", image)
cv2.setMouseCallback("PaintCV", onMouse)                 # 마우스 콜백 함수
cv2.createTrackbar("Thickness", "PaintCV", thickness, 255, onTrackbar)

canvas = image[:, w*2:image.shape[1]]                  # 메뉴를 제외한 캔버스 영역

while True:
    if mouse_mode == 1:                                # 마우스 버튼 떼기
        draw(image, Color)                             # 원본에 그림
    elif mouse_mode == 3:                              # 마우스 드래그
        if draw_mode == DRAW_BRUSH or draw_mode == ERASE:
            draw(image, Color)                         # 원본에 그림
        else:
            draw(np.copy(image), (200, 200, 200))      # 복사본에 회색으로 그림
    if cv2.waitKey(30) == 27:                          # ESC 키를 누르면 종료
        break