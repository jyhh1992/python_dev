import numpy as np, cv2

def morphology(img, mask=None, mode=0):
    dst = np.zeros(img.shape, np.uint8)
    if mask is None: mask = np.ones((3, 3), np.uint8)
    ycenter, xcenter = np.divmod(mask.shape[:2], 2)[0]

    mcnt = cv2.countNonZero(mask)
    for i in range(ycenter, img.shape[0] - ycenter):           # 입력 행렬 반복 순회
        for j in range(xcenter, img.shape[1] - xcenter):
            # 마스크 영역
            y1, y2 = i - ycenter, i + ycenter + 1              # 마스크 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1              # 마스크 너비 범위
            roi = img[y1:y2, x1:x2]                            # 마스크 영역
            temp = cv2.bitwise_and(roi, mask)
            cnt  =  cv2.countNonZero(temp)                     # 일치한 화소수 계산

            if mode == cv2.MORPH_ERODE :
                dst[i, j] = 255 if (cnt == mcnt) else 0    # 침식
            elif mode == cv2.MORPH_DILATE :
                dst[i, j] = 0 if (cnt == 0) else 255  # 팽창

    return dst

image = cv2.imread("images/morph.jpg", 0) # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]  # 영상 이진화

mask = np.array([0, 1, 0,                                             # 마스크 선언 및 초기화
                 1, 1, 1,
                 0, 1, 0], np.uint8).reshape(3, 3)

morph1 = morphology(th_img, mask, mode=cv2.MORPH_ERODE)
morph2 = morphology(th_img, mask, mode=cv2.MORPH_DILATE)

cv2.imshow("MORPH_ERODE", morph1)
cv2.imshow("MORPH_DILATE", morph2)

cv2.waitKey(0)