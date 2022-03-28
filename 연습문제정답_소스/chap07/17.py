import numpy as np, cv2

no, max_no, cnt = 0, 20, 1

while True:
    no = no + cnt
    fname = "images/test_car/{0:02d}.jpg".format(no)
    image = cv2.imread(fname, cv2.IMREAD_COLOR)

    if image is None:
        print("%02d.jpg: 영상 파일 없음" % no)
        if no < 0 : no = max_no
        elif no >= max_no: no = 0
        continue

    mask = np.ones((5, 17), np.uint8)  # 닫힘 연산 마스크
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 명암도 영상 변환
    gray = cv2.blur(gray, (5, 5))  # 블러링
    gray = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 5)  # 소벨 에지 검출

    # 이진화 및 닫힘 연산 수행
    _, th_img = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    morph = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations=3)

    cv2.imshow("image " + str(no), image)
    cv2.imshow("binary image", th_img)
    cv2.imshow("opening", morph)

    key = cv2.waitKeyEx(0)                          # 키 이벤트 대기
    if key == 2490368: cnt =  1                # 윗쪽 화살표 키이면 다음 영상
    elif key == 2621440: cnt = -1                  # 아래쪽 화살표 키이면 이전 영상
    elif key == 32 or key == 27: break              # 프로그램 종료 조건
    cv2.destroyWindow("image " + str(no))
