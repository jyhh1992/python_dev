import numpy as np

leng = 50
data = np.random.randint(0, leng, 500)					# 1~100사이 정수 난수 1차원 행렬
cnt = [0] * leng;

for i in data:
    cnt[i] += 1

max = [[0, 0]]*3
for i in range(len(cnt)):
    c = 0
    for j in range(3):
        if cnt[i] >= max[j][0]: c+=1

    if c == 3:
        max[0] = max[1]
        max[1] = max[2]
        max[2] = cnt[i], i
    if c == 2:
        max[0] = max[1]
        max[1] = cnt[i], i
    if c == 1 :
        max[0] = cnt[i], i

print(data)
print(cnt)
print('가장 중복이 많은 횟수: %d 중복원소: %d' % max[2])
print('두번째 중복이 많은 횟수: %d 중복원소: %d'% max[1])
print('세번째 중복이 많은 횟수: %d 중복원소: %d'% max[0])
