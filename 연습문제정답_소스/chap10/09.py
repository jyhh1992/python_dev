import numpy as np, cv2, pickle

def accumulate(image, rho, theta):
    h, w = image.shape[:2]
    rows, cols = (h + w) * 2 // rho, int( np.pi/theta)  # 누적행렬 너비, 높이
    accumulate = np.zeros((rows, cols), np.int32)    # 직선 누적행렬

    sin_cos = [(np.sin(t * theta), np.cos(t * theta)) for t in range(cols)]  # 삼각 함수값 미리 저장
    pts = np.where(image > 0)
    polars = np.dot(sin_cos, pts).T            # 행렬곱으로 허프 변환 수식 계산
    polars = (polars/ rho + rows / 2).astype("uint")        # 해상도 변경 및 위치 조정

    for row in polars:
        for t, r in enumerate(row):
           accumulate[r, t] += 1  # 좌표 누적

    return accumulate

image = cv2.imread('images/hough.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")
blur  = cv2.GaussianBlur(image, (5, 5), 2, 2)
canny = cv2.Canny(blur, 100, 200, 5)

rho, theta = 1,  np.pi / 180
acc_mat = accumulate(canny, rho, theta)  # 허프 누적 행렬 계산
with open('data.pickle', 'wb') as f:
    pickle.dump(acc_mat, f, pickle.HIGHEST_PROTOCOL)

cv2.imshow("image", image)
cv2.waitKey(0)