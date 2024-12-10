import cv2

#0번은 내장 카메라, 2번은 웹캠
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 800)  #가로 프레임
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  #세로 프레임

while True:
  ret, frame = capture.read()
  #카메라 연결 실패 시 종료
  if not ret:
    break  #프레임 읽기 실패 시 루프 종료

  cv2.imshow("VideoFrame", frame)  #프레임 출력

  #q 누르면 루프 종료
  if cv2.waitKey(33) & 0xFF == ord('q'):
    break  

#종료 처리
capture.release() #카메라 리소스 해제
cv2.destroyAllWindows() #모든 창 닫기
