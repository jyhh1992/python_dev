import numpy as np, cv2
image = np.full((300, 400), 100, np.uint8)

cv2.imshow("position", image)
cv2.resizeWindow("position", 500, 600)
cv2.waitKey(0)
cv2.destroyAllWindows()
