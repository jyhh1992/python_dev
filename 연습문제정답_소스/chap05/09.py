import numpy as np, cv2

data = [3, 5, 4, 2, 9, 7,
        12, 15, 19, 30 ,40, 13,
        25, 77, 36, 44, 22, 66]

m = np.array(data, np.int).reshape(3,6).astype(float)

result1 = cv2.reduce(m, dim=0, rtype = cv2.REDUCE_AVG)
result2 = cv2.reduce(m, dim=1, rtype = cv2.REDUCE_AVG)

print('세로(열) 방향 감축:\n', result1)
print('가로(행) 방향 감축:\n', result2)