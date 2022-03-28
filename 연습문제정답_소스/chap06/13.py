import numpy as np, cv2

def calc_ycc(bgr):
    B, G, R = float(bgr[0]), float(bgr[1]), float(bgr[2])       # 속도면에 유리
    Y = 0.299* R + 0.587 * G + 0.114 * B
    Cr = (R - Y) * 0.564 + 128
    Cb = (B - Y) * 0.713 + 128
    return (Y, Cr, Cb)

def bgr2ycc(image):
    ycc = [[calc_ycc(pixel) for pixel in row] for row in image ]   # 2차원 배열 순회
    return (np.array(ycc)).astype('uint8')

BGR_img = cv2.imread("images/color_space.jpg", cv2.IMREAD_COLOR) # 컬러 영상 읽기
if BGR_img is None: raise Exception("영상 파일 읽기 오류")

YCC_img = bgr2ycc(BGR_img)                  # BGR를 HSI로 변환
YCC_img2 = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2YCrCb) # OpenCV 함수
Y, Cr, Cb = cv2.split(YCC_img)                    # 채널 분리
Y2, Cr2, Cb2 = cv2.split(YCC_img2) 					# 채널 분리

titles = ['BGR_img','Y','Cr','Cb']
for t in titles: cv2.imshow(t, eval(t))
for t in titles[1:]: cv2.imshow('OpenCV_'+t, eval(t+'2'))
cv2.waitKey(0)

