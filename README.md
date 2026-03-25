# Hand & Finger Tracking using MediaPipe (Python)

## Overview
This project implements real-time hand tracking using MediaPipe Tasks API and OpenCV. It detects hand landmarks from webcam input, tracks all five fingertips, and optionally visualizes the full hand skeleton.

---

## Features
- Real-time webcam-based hand tracking
- Tracks all 5 fingertips (thumb, index, middle, ring, pinky)
- Supports multiple hands
- Hand skeleton visualization
- Uses MediaPipe Tasks (modern API)

---

## Tech Stack
- Python 3.11
- OpenCV
- MediaPipe Tasks API

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/hand-tracking.git
cd hand-tracking
```
### 2. Create virtual dependencies
```bash
python -m venv myenv
myenv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install opencv-python mediapipe
```
---

## Model Setup
Download the MediaPipe hand landmarker model:
```bash
https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task
```
Place it in the project directory and update the path in code if needed:
```bash
model_asset_path = "hand_landmarker.task"
```
---

## Usage
Run the script :
```bash
python finger_detection.py
```
Press ```q``` to exit

---

## Project Structure
hand-tracking/
│
├── src/
│   └── finger_detection.py
│
├── models/
│   └── hand_landmarker.task
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

---

## How it Works

- Captures webcam frames using OpenCV
- Converts frames to RGB format
- Uses MediaPipe HandLandmarker to detect 21 hand landmarks
- Extracts fingertip coordinates
- Draws points and connections on the frame

---

## Landmark Index Reference

```
Thumb:   1-4
Index:   5-8
Middle:  9-12
Ring:   13-16
Pinky:  17-20
Wrist:   0
```

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

MIT License

---
