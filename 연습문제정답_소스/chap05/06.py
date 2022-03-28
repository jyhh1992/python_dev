import numpy as np, cv2

m1 = [1, 2, 3, 1, 2, 3]
m2 = [3, 3, 4, 2, 2, 3]
m3 = np.add(m1, m2)
m4 = np.subtract(m1, m2)
# m3 = np.array(m1) + np.array(m2)
# m4 = np.array(m1) - np.array(m2)

print("[m1] = %s" %m1 )
print("[m2] = %s" %m2 )
print("[m3] = %s" %m3 )
print("[m4] = %s" %m4 )