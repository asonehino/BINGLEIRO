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

      #q 누르면 사진을 저장하고 종료
      if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("C:\project\Bingleiro\AI\photo\photo.jpg", frame) #사진 저장
        print("Photo saved!")
        break
    else:
      print("No frame available")
      break
else:
  print("Can't open camera")

#종료
capture.release()
cv2.destroyAllWindows()
