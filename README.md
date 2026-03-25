# Hand & Finger Tracking using MediaPipe (Python)

## Overview
This project implements real-time hand tracking using MediaPipe Tasks API and OpenCV. It detects up to two hands from a webcam feed, visualizes hand landmarks, highlights fingertips, and draws a skeletal structure over detected hands.

The system is optimized for high-confidence tracking and stable real-time performance.

---

## Features
- Real-time hand detection via webcam
- Tracks up to 2 hands simultaneously
- Highlights fingertips (thumb → pinky)
- Draws full hand skeleton connections
- Adjustable confidence thresholds for detection and tracking
- Lightweight and runs locally (no cloud dependency)

---

## Tech Stack
- Python 3.11
- OpenCV
- MediaPipe Tasks API

---

## Project Structure
hand-tracking/
│── hand_tracking.py          # Main script
│── hand_landmarker.task      # Pre-trained MediaPipe model (included)
│── README.md                 # Documentation
│── requirements.txt          # Dependencies (optional)

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/hand-tracking.git
cd hand-tracking
```

### 2. Install dependencies
```bash
pip install opencv-python mediapipe
```
---


## Usage
1. Ensure the model file ```hand_landmarker.task``` is in the project directory.
2. Update the model path in the script if needed:
```bash
model_asset_path = "hand_landmarker.task"
```
3. Run the script
```bash
python hand_tracking.py
```
4. Controls
- Press ```q``` to exit

---

## How it Works

1. Frame Capture
    - Captures video using OpenCV (``cv2.VideoCapture(0)``)
2. Preprocessing
    - Flips frame horizontally
    - Converts BGR → RGB (required by MediaPipe)
3. Hand Detection
    - Uses ``HandLandmarker`` from MediaPipe Tasks API
    - Detects 21 landmarks per hand
4. Visualization
    - Fingertips:
      - Indices: ``[4, 8, 12, 16, 20]``
      - Drawn as green circles
    - Skeleton:
      - Predefined connections between landmarks
      - Drawn as blue lines

---

## Configuration

You can tweak detection behavior via:

```bash
num_hands=2
min_hand_detection_confidence=0.8
min_hand_presence_confidence=0.8
min_tracking_confidence=0.8
```
Higher values → more accuracy, less sensitivity
Lower values → more detections, more noise

---

## Output
  - Live webcam window showing:
      -  Detected hands
      - Highlighted fingertips
      - Skeleton overlay
---

## Known Limitations
  -  Performance depends on camera quality and lighting
  -  Occlusions reduce tracking accuracy
  -  CPU-based inference may lag on low-end systems

---

## Notes

- Ensure the ```.task``` model file is correctly placed
- Python 3.11 is recommended for compatibility
- Avoid mixing MediaPipe Solutions API with Tasks API

---

## Future Improvements

- Gesture recognition (e.g., counting fingers)
- Mouse control using hand tracking
- Multi-hand interaction logic

---

## License

``LICENSE``

---
