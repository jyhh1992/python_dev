import numpy as np, cv2

def draw_histo2(hist):
    if hist.ndim != 2: print('2차원 히스토그램 아님')
    h, w = hist.shape[:2]

    graph = [[(i, j, hist[i,j]) for j in range(w)] for i in range(h)]
    ratios = (180/h, 256/w, 256 )
    graph= np.multiply(graph, ratios).astype('uint8')

    bgr = cv2.cvtColor(graph, cv2.COLOR_HSV2BGR)
    bgr = cv2.resize(bgr, None, fx=10, fy=10, interpolation=cv2.INTER_AREA)
    return bgr

image = cv2.imread("images/10.jpg")  # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # OpenCV 함수

ch, bsize, ranges = [0, 1], [30, 48], [0, 180, 0, 256]  # 히스토그램 간격수, 값 범위
hist = cv2.calcHist([hsv], ch, None, bsize, ranges)  # OpenCV 함수
cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)

dst = draw_histo2(hist)
cv2.imshow("image", image)
cv2.imshow("dst", dst)
cv2.waitKey(0)


