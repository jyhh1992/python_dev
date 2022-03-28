import numpy as np

m = np.array([22, 11, 4, 6, 8, 10, 15.15, 20, 40, 50 ], np.float32)
s = sum(m)
a = s / len(m)

print ('합: ' , int(s * 100) / 100)
print ('평균: ' , int(a * 100) / 100)







# import numpy as np, cv2
#
# mat = np.zeros((500, 600), 100, np.uint8)
#
# cv2.imshow('mat', mat)
# cv2.waitKey()
#
# import numpy as np
# import cv2
#
# image = np.zeros((300, 400), np.uint8)
# image[:] = 100
#
# title = "Window"
# cv2.namedWindow(title, cv2.WINDOW_NORMAL)
# cv2.moveWindow(title, 100, 200)
# cv2.imshow(title, image)
# cv2.waitKey(0)
