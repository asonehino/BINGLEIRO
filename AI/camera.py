import cv2

# 카메라 설정 (0번 내장 카메라, 1번 웹캠)
capture = cv2.VideoCapture(1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 800)  # 가로 크기 설정
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 세로 크기 설정

if capture.isOpened():
  while True:
    ret, frame = capture.read()

    if ret:
      cv2.imshow("VideoFrame", frame) 

      #q 누르면 사진을 저장
      if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("C:\project\Bingleiro\AI\photo\photo.jpg", frame)
        print("Photo saved!")
      #w 누르면 종료
      if cv2.waitKey(1) & 0xFF == ord('w'):
        break
    
    else:
      print("No frame available")
      break
else:
  print("Can't open camera")

#카메라 해제 및 창 닫기
capture.release()
cv2.destroyAllWindows()
