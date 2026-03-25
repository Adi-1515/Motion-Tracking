import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(model_asset_path=r"H:\Programming Files\Python fies\Motion Tracking\hand_landmarker.task")
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2, min_hand_detection_confidence=0.8, 
            min_hand_presence_confidence=0.8, min_tracking_confidence=0.8)

detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    results = detector.detect(mp_image)

    if results.hand_landmarks:
        for hand_landmarks in results.hand_landmarks:
            
            # --- Fingertips ---
            fingertips = [4, 8, 12, 16, 20]
            for tip in fingertips:
                lm = hand_landmarks[tip]
                x, y = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

            # --- Skeleton (optional) ---
            HAND_CONNECTIONS = [(0,1),(1,2),(2,3),(3,4),
                                (0,5),(5,6),(6,7),(7,8),
                                (5,9),(9,10),(10,11),(11,12),
                                (9,13),(13,14),(14,15),(15,16),
                                (13,17),(17,18),(18,19),(19,20),(0,17) ]
            for connection in HAND_CONNECTIONS:
                start = hand_landmarks[connection[0]]
                end = hand_landmarks[connection[1]]

                x1, y1 = int(start.x * w), int(start.y * h)
                x2, y2 = int(end.x * w), int(end.y * h)
                cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    # Display the frame
    cv2.imshow('index finger track', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()