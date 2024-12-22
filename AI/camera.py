import cv2
import torch
import numpy as np

# YOLOv5 모델 로드
model = torch.hub.load("ultralytics/yolov5", "yolov5s")

# 웹캠 설정
capture = cv2.VideoCapture(0)  # 0번 카메라 (필요시 번호 변경)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 딕셔너리 초기화
saved_images = {}

# 이미지 식별자
image_count = 0

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
    
    # 클래스 이름, 신뢰도, 좌표 표시
    label = f"{class_name} {conf:.2f} ({x1}, {y1}, {x2}, {y2})"
    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 좌표 콘솔에 출력
    print(f"Detected {class_name} with confidence {conf:.2f}")
    print(f"Coordinates: ({x1}, {y1}), ({x2}, {y2})")

  cv2.imshow("VideoFrame", frame)

  # 키 입력 처리
  key = cv2.waitKey(1) & 0xFF
  if key == ord('q') and len(objects) > 0:
    # 탐지된 첫 번째 객체의 영역을 크롭하여 저장
    cropped = frame[y1:y2, x1:x2]

    # 딕셔너리에 이미지와 좌표 저장
    image_count += 1
    image_key = f"image_{image_count}"
    saved_images[image_key] = {
      "coordinates": (x1, y1, x2, y2),
      "image": cropped
    }

    # 이미지 저장
    file_path = f"C:/project/Bingleiro/AI/photo/cropped_object_{image_count}.jpg"
    cv2.imwrite(file_path, cropped)
    print(f"Image {image_key} saved with coordinates {saved_images[image_key]['coordinates']}")

  elif key == ord('w'):
    break

# 리소스 해제
capture.release()
cv2.destroyAllWindows()
