import numpy as np, cv2
from Common.dct2d import *

def dct2d(img, M, N):
    dst = np.empty(img.shape, np.float32)
    for i in range(0, img.shape[0], M):
        for j in range(0, img.shape[1], N):
            block = img[i:i+M, j:j+N].astype('float32')
            dst[i:i+M, j:j+N] = cv2.dct(block)
    return dst

def idct2d(img, M, N):
    dst = np.empty(img.shape, np.float32)
    for i in range(0, img.shape[0], M):
        for j in range(0, img.shape[1], N):
            block = img[i:i+M, j:j+N]
            dst[i:i+M, j:j+N] = cv2.dct(block, flags=cv2.DCT_INVERSE)
    return dst.astype('uint8')

image = cv2.imread('images/dct.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일을 읽기 에러")

M, N = 8, 8
dct = dct2d(image, M, N)
idct = idct2d(dct, M, N)

cv2.imshow("image", image)
cv2.imshow("dct", dct)
cv2.imshow("idct", idct)
cv2.waitKey(0)