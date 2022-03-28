import cv2
from haar_utils import preprocessing,correct_image, detect_object
from haar_classify import classify, display
from haar_histogram import make_masks, calc_histo

face_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")  # 정면 검출기

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
    if len(faces):
        cv2.rectangle(image,faces[0], (0,255,0), 2 )
        cv2.imshow('image', image)
        print("%02d.jpg: 얼굴 검출" % no)

    else: print("%02d.jpg: 얼굴 미검출" % no)

    key = cv2.waitKeyEx()                          # 키 이벤트 대기
    if key == 0x270000: cnt =  1                # 윗쪽 화살표 키이면 다음 영상
    elif key == 0x250000: cnt = -1                  # 아래쪽 화살표 키이면 이전 영상
    elif key == 32 or key == 27: break              # 프로그램 종료 조건
