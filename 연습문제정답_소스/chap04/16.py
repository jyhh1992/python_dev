import cv2

capture = cv2.VideoCapture(0)  # 0번 카메라 연결
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

fps = 30                                         # 초당 프레임 수
delay = round(1000/ fps)                            # 프레임 간 지연 시간
size  = (640, 480)                                  # 동영상 파일 해상도
fourcc = cv2.VideoWriter_fourcc(*'DIVX')            # 압축 코덱 설정

while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받기
    if not ret: break
    x, y, w, h = (200,100, 100,200)
    cv2.rectangle(frame, (x,y,w,h) , (0,0,255), 3 )

    blue, green, red = cv2.split(frame)
    tmp = green[y:y+h, x:x+w]
    cv2.add(tmp, 50, tmp)
    frame = cv2.merge([blue, green, red])

    if cv2.waitKey(delay) >= 0: break
    cv2.imshow("ex16", frame)  # 윈도우에 영상 띄우기
capture.release()