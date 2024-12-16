import cv2
import torch

# YOLOv5 모델 로드
model = torch.hub.load("ultralytics/yolov5", "yolov5s")

# 웹캠 설정
capture = cv2.VideoCapture(0)  # 0번 카메라 (필요시 번호 변경)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
  ret, frame = capture.read()
  if not ret:
    print("Failed to grab frame")
    break

  # YOLOv5로 객체 탐지
  results = model(frame)
  objects = results.xyxy[0]  # 탐지된 객체 리스트

  # 첫 번째 탐지된 객체만 처리
  if len(objects) > 0:
    x1, y1, x2, y2, conf, cls = map(int, objects[0][:6])  # 첫 번째 객체
    class_name = results.names[int(cls)]  # 클래스 이름

    # 경계 상자 그리기
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    label = f"{class_name} {conf:.2f}"
    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

  cv2.imshow("VideoFrame", frame)

  # 키 입력 처리
  key = cv2.waitKey(1) & 0xFF
  if key == ord('q') and len(objects) > 0:
    # 탐지된 첫 번째 객체의 영역을 크롭하여 저장
    cropped = frame[y1:y2, x1:x2]
    cv2.imwrite("C:/project/Bingleiro/AI/photo/cropped_object.jpg", cropped)
    print("Cropped image saved!")
  elif key == ord('w'):
    break

# 리소스 해제
capture.release()
cv2.destroyAllWindows()
