import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import os
import sys

# Define constants
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "hand_landmarker.task")
FINGERTIPS = [4, 8, 12, 16, 20]
HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (17, 18), (18, 19), (19, 20), (0, 17)
]

def create_hand_landmarker(model_path: str) -> vision.HandLandmarker:
    """Initializes and returns the MediaPipe Hand Landmarker."""
    if not os.path.exists(model_path):
        print(f"Error: Model file not found at {model_path}.")
        print("Please ensure the model file exists in the 'models' directory.")
        sys.exit(1)

    base_options = python.BaseOptions(model_asset_path=model_path)
    options = vision.HandLandmarkerOptions(
        base_options=base_options,
        num_hands=2,
        min_hand_detection_confidence=0.8,
        min_hand_presence_confidence=0.8,
        min_tracking_confidence=0.8
    )
    return vision.HandLandmarker.create_from_options(options)

def draw_landmarks(frame, hand_landmarks):
    """Draws fingertips and hand skeleton on the given frame."""
    h, w, _ = frame.shape
    
    # Draw skeleton lines
    for connection in HAND_CONNECTIONS:
        start = hand_landmarks[connection[0]]
        end = hand_landmarks[connection[1]]

        x1, y1 = int(start.x * w), int(start.y * h)
        x2, y2 = int(end.x * w), int(end.y * h)
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    # Draw fingertips
    for tip in FINGERTIPS:
        lm = hand_landmarks[tip]
        x, y = int(lm.x * w), int(lm.y * h)
        cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

def main():
    detector = create_hand_landmarker(MODEL_PATH)
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open the webcam.")
        sys.exit(1)

    print("Starting webcam... Press 'q' to quit.")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to grab frame.")
                break

            # Process frame
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            
            # Detect hand landmarks
            results = detector.detect(mp_image)

            # Draw results
            if results.hand_landmarks:
                for hand_landmarks in results.hand_landmarks:
                    draw_landmarks(frame, hand_landmarks)

            # Display output
            cv2.imshow('Hand Tracking', frame)

            # Exit condition
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
