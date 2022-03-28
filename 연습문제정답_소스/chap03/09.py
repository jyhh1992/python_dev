import numpy as np

m = np.array([22, 11, 4, 6, 8, 10, 15.15, 20, 40, 50 ], np.float32)
s = sum(m)
a = s / len(m)

print ('합: ' , int(s * 100) / 100)
print ('평균: ' , int(a * 100) / 100)
