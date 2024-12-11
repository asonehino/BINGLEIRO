import cv2
import torch

# YOLOv5 모델 로드 (PyTorch 모델)
model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # 'yolov5s' 모델을 로드

# 카메라 설정 (0번 내장 카메라)
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 800)  # 가로 크기 설정
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 세로 크기 설정

while True:
  ret, frame = capture.read()
  if not ret:
    break  # 카메라 연결 실패 시 루프 종료

  # YOLOv5 모델을 통해 객체 탐지
  results = model(frame)  # 이미지에서 객체 탐지

  # 결과에서 객체 탐지된 좌표 및 클래스 가져오기
  for *box, conf, cls in results.xyxy[0]:  # results.xyxy는 객체마다 경계 상자 좌표를 포함한 배열
    x1, y1, x2, y2 = map(int, box)  # 좌표를 정수로 변환

    # 클래스 이름
    class_name = results.names[int(cls)]

    # 경계 상자 그리기
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 텍스트 출력 (클래스, 신뢰도, 좌표)
    label = f"{class_name} {conf:.2f} ({x1}, {y1}, {x2}, {y2})"
    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 영상 출력
    cv2.imshow("VideoFrame", frame)

  # q를 누르면 종료
  if cv2.waitKey(33) & 0xFF == ord('q'):
    break

# 종료 처리
capture.release()  # 카메라 리소스 해제
cv2.destroyAllWindows()  # 모든 창 닫기
