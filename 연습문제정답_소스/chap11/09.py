import cv2, numpy as np
from haar_utils import preprocessing,correct_image, detect_object
from haar_classify import classify, display
from haar_histogram import make_masks, calc_histo

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")  # 정면 검출기
reye_cascade = cv2.CascadeClassifier("haarcascade_righteye_2splits.xml")  # 눈 검출기
leye_cascade = cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")  # 눈 검출기

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")  # 눈 검출기


def draw(image, eyes, color):
    if len(eyes)==2:
        eye_centers1 = [(x + ex + ew // 2, y + ey + eh // 2) for ex, ey, ew, eh in eyes]
        cv2.circle(image, tuple(eye_centers1[0]), 10, color, 1)  # 눈 표시
        cv2.circle(image, tuple(eye_centers1[1]), 10, color, 1)

no, max_no, cnt = 0, 60, 1
while True:
    no = no + cnt
    image, gray = preprocessing(no)                             # 전처리 수행
    if image is None:
        print("%02d.jpg: 영상 파일 없음" % no)
        if no < 0 : no = max_no
        elif no >= max_no: no = 0
        continue

    faces = face_cascade.detectMultiScale(gray, 1.1, 2, 0, (100, 100))
    if faces.any():
        x, y, w, h = faces[0]
        face_image = image[y:y+h, x:x+w]  # 얼굴 영역 영상 가져오기
        reye = reye_cascade.detectMultiScale(face_image, 1.10, 7, 0, (25, 20))
        leye = leye_cascade.detectMultiScale(face_image, 1.10, 7, 0, (25, 20))

        if len(reye) == 2 and len(leye)==2:
            face_center = (x + w // 2, y + h // 2)

            # 오른쪽 눈 왼쪽눈 구분
            if reye[0][0] > reye[1][0]: reye[0], reye[1] = reye[1] ,reye[0]
            if leye[0][0] > leye[1][0]: leye[0], leye[1] = leye[1], leye[0]

            # 중심점 게산
            reye_centers = [(x + ex + ew // 2, y + ey + eh // 2) for ex, ey, ew, eh in reye]
            leye_centers = [(x + ex + ew // 2, y + ey + eh // 2) for ex, ey, ew, eh in leye]

            # 두개 눈좌표 평균
            eye_centers = np.add(reye_centers, leye_centers)//2

            corr_image, corr_centers = correct_image(image, face_center, eye_centers)  # 기울기 보정

            sub_roi = detect_object(face_center, faces[0])      # 머리 및 입술영역 검출
            masks = make_masks(sub_roi, corr_image.shape[:2])      # 4개 마스크 생성
            sims = calc_histo(corr_image, sub_roi, masks)	    # 4개 히스토그램 생성

            classify(corr_image, sims, no)                        # 성별 분류 및 표시
            display(corr_image, face_center, corr_centers, sub_roi) # 얼굴, 눈 표시

            draw(image, reye, (255,0,0))
            draw(image, leye, (0, 255, 0))
            cv2.imshow('im', image)

        else: print("%02d.jpg: 눈 미검출" % no)
    else: print("%02d.jpg: 얼굴 미검출" % no)

    key = cv2.waitKeyEx(0)                          # 키 이벤트 대기
    if key == 0x270000: cnt =  1                # 윗쪽 화살표 키이면 다음 영상
    elif key == 0x250000: cnt = -1                  # 아래쪽 화살표 키이면 이전 영상
    elif key == 32 or key == 27: break              # 프로그램 종료 조건

    print("%x" %key)
