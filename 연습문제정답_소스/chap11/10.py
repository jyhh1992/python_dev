import cv2,  numpy as np
import matplotlib.pyplot as plt
from haar_utils import preprocessing, correct_image, detect_object
from haar_classify import classify10
from haar_histogram import make_masks, calc_histo

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")  # 정면 검출기
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")  # 눈 검출기

datas = []
groups = np.full(60, -1 )

for no in range(len(groups)):
    image, gray = preprocessing(no)                             # 전처리 수행
    if image is None:
        print("%02d.jpg: 영상 파일 없음" % no)
        continue

    faces = face_cascade.detectMultiScale(gray, 1.1, 2, 0, (100, 100))
    if faces.any():
        x, y, w, h = faces[0]
        face_image = image[y:y + h, x:x + w]  # 얼굴 영역 영상 가져오기
        eyes = eye_cascade.detectMultiScale(face_image, 1.15, 7, 0, (35, 35))

        if len(eyes) == 2:
            face_center = (x + w // 2, y + h // 2)
            eye_centers = [(x + ex + ew // 2, y + ey + eh // 2) for ex, ey, ew, eh in eyes]
            corr_image, corr_centers = correct_image(image, face_center, eye_centers)  # 기울기 보정

            sub_roi = detect_object(face_center, faces[0])  # 머리 및 입술영역 검출
            masks = make_masks(sub_roi, corr_image.shape[:2])  # 4개 마스크 생성
            sims = calc_histo(corr_image, sub_roi, masks)  # 4개 히스토그램 생성

            datas.append(sims)
            groups[no] = classify10(corr_image, sims, no)  # 성별 분류 및 표시

        else:
            print("%02d.jpg: 눈 미검출" % no)
    else:
        print("%02d.jpg: 얼굴 미검출" % no)

man = sum(groups[:30]==0)
woman = sum(groups[30:]==1)
miss = sum(groups[:]==-1)

x = np.arange(0, len(datas))
datas = np.transpose(datas)

means = np.zeros((4, len(x)), np.float32)
means[0, :30] = np.mean(datas[0,:30])
means[0, 30:] = np.mean(datas[0,30:])
means[1, :30] = np.mean(datas[1,:30])
means[1, 30:] = np.mean(datas[1,30:])

plt.figure(num='similarity', figsize=(15,6))
plt.plot(x, datas[0], 'ro', label='lip-face')
plt.plot(x, datas[1], 'bv', label='hair')
plt.plot(x, means[0], 'r-', label='mean sim1')
plt.plot(x, means[1], 'b-', label='mean sim2')

plt.legend(loc='upper left')
plt.tight_layout()
plt.show()