import numpy as np, cv2

def median_filter(image, ksize):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize // 2  # 마스크 절반 크기

    for i in range(center, rows - center):  # 입력 영상 순회
        for j in range(center, cols - center):
            y1, y2 = i - center, i + center + 1  # 마스크 높이 범위
            x1, x2 = j - center, j + center + 1  # 마스크 너비 범위
            mask = image[y1:y2, x1:x2].flatten()  # 마스크 영역

            sort_mask = cv2.sort(mask, cv2.SORT_EVERY_COLUMN)  # 정렬 수행
            dst[i, j] = sort_mask[sort_mask.size // 2]  # 출력화소로 지정
    return dst

image = cv2.imread("images/noise.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

med_img1 = median_filter(image, 3)  # 사용자 정의 함수
cv2.imshow("image", image),
cv2.imshow("median - User", med_img1)
cv2.waitKey(0)