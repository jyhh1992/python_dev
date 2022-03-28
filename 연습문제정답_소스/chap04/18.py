import numpy as np, cv2

c = 200
r, sr, c2, c4 = c//2, c//4 , c*2, c*4
img = np.full((c4,c4,3), 255, np.uint8)
blue, red = (255,0,0), (0,0,255)

cv2.ellipse(img, (c2,c2), (r,r),   0,0, 180, blue, -1)
cv2.ellipse(img, (c2,c2), (r,r), 180,0, 180, red, -1)
cv2.ellipse(img, (c2+r-sr,c2), (sr,sr), 180,0, 180, blue, -1)
cv2.ellipse(img, (c2  -sr,c2), (sr,sr),   0,0, 180, red, -1)

left  = (c2 - int((c2/2) * (18+8)/24) , c2 -sr)
right = (c2 + int((c2/2) * (18+0)/24) , c2 -sr)

cv2.imshow('ex18', img[c2-c:c2+c, c2-r*3:c2+r*3])
cv2.waitKey(0)