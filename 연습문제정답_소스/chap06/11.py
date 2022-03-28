import numpy as np, cv2

def calc_histo(image, channels, bsize, ranges ):

    ch = len(channels)
    shape = bsize if ch >1 else (bsize[0], 1)
    hist = np.zeros(shape, np.float32)         # 히스토그램 누적 행렬
    gap = np.divide(ranges[1::2], bins)                # 계급 간격

    for row in image:  # 2차원 행렬 순회 방식
        for val in row:
            idx = np.divide(val[channels], gap).astype('uint')
            hist[tuple(idx)]+= 1
    return hist

image = cv2.imread("images/pixel.jpg") # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")

ch, bins, ranges =[0,1],  [4, 4], [0, 256, 0, 256]                  # 히스토그램 간격수, 값 범위
hist1 = calc_histo(image, ch ,bins, ranges)                  # 사용자 정의 히스토그램 계산
hist2 = cv2.calcHist([image], ch, None, bins, ranges)  # OpenCV 함수

print("저자 구현 함수: \n", hist1)                           # 행렬을 벡터로 변환하여 출력
print("OpeCV 함수: \n", hist2)
cv2.imshow("image", image)
cv2.waitKey(0)

