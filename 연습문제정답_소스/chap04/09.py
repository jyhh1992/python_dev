import numpy as np, cv2

image = np.full((600, 400,3 ), (255,255,255) , np.uint8)
cv2.rectangle(image, (100,100, 200,300) , (0,0,255), 2)
cv2.imshow('ex09', image)
cv2.waitKey()
