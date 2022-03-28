import numpy as np, cv2
from Common.fft2d import FFT, IFFT, calc_spectrum, fftshift

def filtering():
    filter = np.zeros(image.shape, np.float32)
    cv2.circle(filter, (cx, cy), high, (1,1), -1)
    cv2.circle(filter, (cx, cy), low, (0,0), -1)
    remv_dft = dft * filter
    dst[:, image.shape[1]:image.shape[1]*2] = calc_spectrum(remv_dft)
    dst[:, image.shape[1]*2:] = IFFT(remv_dft, image.shape, mode)
    cv2.imshow(title, dst)

def high_bar(value):
    global high
    high = value
    filtering()

def low_bar(value):
    global low
    low = value
    filtering()

image = cv2.imread('images/dft_256.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")

mode = 2
low, high = 10, 100
cy, cx = np.divmod(image.shape, 2)[0]
dft, spectrum =  FFT(image)
dst = cv2.repeat(image, 1, 3)

size = np.divmod(spectrum.shape[::-1],2)[0]

title = "ex14"              # 윈도우 이름 지정
cv2.imshow(title, dst)
cv2.createTrackbar("v1", title, 10, size[0], low_bar)
cv2.createTrackbar("v2", title, 50, size[0], high_bar)
low_bar(10)
high_bar(50)
cv2.waitKey()