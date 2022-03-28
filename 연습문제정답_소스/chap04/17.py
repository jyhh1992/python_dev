import cv2

capture = cv2.VideoCapture(0)  # 0번 카메라 연결
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

fps = 15                                         # 초당 프레임 수
delay = round(1000/ fps)                            # 프레임 간 지연 시간
size  = (640, 480)                                  # 동영상 파일 해상도
fourcc = cv2.VideoWriter_fourcc(*'DIVX')            # 압축 코덱 설정

writer = cv2.VideoWriter("images/video_file.avi", fourcc, fps, size)
if writer.isOpened() == False: raise Exception("동영상 파일 개방 안됨")

while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받기
    frame = cv2.flip(frame, 1)                 # y축 기준 좌우 뒤집기
    if not ret: break
    if cv2.waitKey(delay) >= 0: break
    writer.write(frame)                 # 프레임을 동영상으로 저장
    cv2.imshow("ex17", frame)  # 윈도우에 영상 띄우기
capture.release()