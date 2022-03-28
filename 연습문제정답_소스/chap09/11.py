import numpy as np, cv2, math
from Common.dft2d import exp, calc_spectrum, fftshift
from Common.fft2d import zeropadding, fft, ifft

def fft2(image):
    pad_img = zeropadding(image)  # 영삽입
    tmp = [fft(row) for row in pad_img]
    dst = [fft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)                        # 전치 환원 후 반환

def ifft2(image):
    tmp = [ifft(row) for row in image]
    dst = [ifft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)                        # 전치 환원 후 반환

image = cv2.imread('images/dft_240.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

dft1 = fft2(image)                                # 2차원 DFT 수행
spectrum1 = calc_spectrum(fftshift(dft1))           # 셔플링후 주파수 스펙트럼 영상 생성

print("원본 영상 행렬 크기:", image.shape)
print("fft 영상 행렬 크기:", dft1.shape)

cv2.imshow("image", image)
cv2.imshow("spectrum1", spectrum1)
cv2.waitKey(0)

