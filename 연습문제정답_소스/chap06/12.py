import numpy as np, cv2

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 0, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1] / hist.shape[0]  # 한 계급 너비

    for i, h in enumerate(hist):
        x = int(round(i * gap))  # 막대 사각형 시작 x 좌표
        w = int(round(gap))
        roi = (x, 0, w, int(h))
        cv2.rectangle(hist_img, roi, 255, cv2.FILLED)
    return hist_img

image = cv2.imread("images/affine_test1.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")

project1 = cv2.reduce(image, 0, cv2.REDUCE_AVG).ravel().astype(int)
project2 = cv2.reduce(image, 1, cv2.REDUCE_AVG).ravel().astype(int)

hist_ver = draw_histo(project1, image.shape)
hist_hor = draw_histo(project2, (image.shape[0],image.shape[0]) )

cv2.imshow("image", image)
cv2.imshow("hist_ver", cv2.flip(hist_ver, 0))
cv2.imshow("hist_hor", hist_hor.T)
cv2.waitKey(0)