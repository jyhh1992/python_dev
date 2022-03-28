import numpy as np, cv2

def print_rects(rects):
    print("-" * 46)                             	# 라인 출력
    print("사각형 원소\t\t랜덤 사각형 정보\t\t  크기")
    print("-" * 46)
    for i, (x,y, w,h, a) in enumerate(rects):		# 저장 데이터 출력
         print("rects[%i] = [(%3d,%3d) from (%3d,%3d)] %5d" %(i, x, y, w, h, a))
    print()

rands = np.zeros((5, 5), np.uint16)        		    # 5행 4열 행렬 생성
starts = cv2.randn(rands[:, :2 ], 100, 50)     		# 0~4행까지 시작좌표 랜덤 생성
ends = cv2.randn(rands[:, 2:-1], 300, 50)       		# 5~9행까지 종료좌표 랜덤 생성

sizes = cv2.absdiff(starts, ends)					# 시작좌표와 종료좌표간 차분 절대값
areas = sizes[:, 0] * sizes[:, 1]
rects = rands.copy()
rects[:, 2:-1] = sizes
rects[:,-1] = areas

idx = cv2.sortIdx(areas, cv2.SORT_EVERY_COLUMN).flatten()

print_rects(rects)
print_rects(rects[idx.astype('int')])