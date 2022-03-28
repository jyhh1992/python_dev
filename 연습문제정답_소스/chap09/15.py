import numpy as np, cv2
from Common.fft2d import FFT, IFFT, calc_spectrum
import matplotlib.pyplot as plt

def get_butterworthFilter(shape, R, n):
    u = np.array(shape)//2
    y = np.arange(-u[0], u[0], 1)
    x = np.arange(-u[1], u[1], 1)
    x, y = np.meshgrid(x, y)
    dist = np.sqrt(x** 2 + y** 2)
    filter = 1 / (1 + np.power(dist / R, 2 * n))
    return x, y, filter if len(shape) < 3 else cv2.merge([filter, filter])

image = cv2.imread('images/filter.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")

dft, spectrum = FFT(image, 2)                    # FFT 수행 및 셔플링
x2, y2, butter_filter = get_butterworthFilter(dft.shape, 30, 10)

filtered_dft2 = dft * butter_filter
butter_img= IFFT(filtered_dft2, image.shape, 2)
spectrum2 = calc_spectrum(filtered_dft2)

fig = plt.figure(figsize=(10,10))                   # 그래프3 생성
ax2 = plt.subplot(222, projection='3d')
ax2.plot_surface(x2, y2, butter_filter,cmap='RdPu'), plt.title('butter_filter')

plt.gray()                                          # 명암도 영상으로 표시
plt.subplot(2,2,1), plt.imshow(image), plt.title('input image')
plt.subplot(2,2,3), plt.imshow(butter_img), plt.title('butter_lowpassed_image')
plt.subplot(2,2,4), plt.imshow(spectrum2), plt.title('butter_lowpassed_spectrum')

plt.tight_layout(), plt.show()