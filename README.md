# Real-Time Hand Landmark Tracking

This repository contains a real-time computer vision application for hand tracking using OpenCV and the MediaPipe Tasks API. The system captures video input, processes frames sequentially, and applies a pre-trained machine learning model to extract 21 distinct 3D hand landmarks per hand.

## Key Features
- **Real-Time Inference:** Frame-by-frame processing of standard video input streams using a synchronized MediaPipe pipeline.
- **Landmark Extraction:** Detection and spatial coordinate mapping of hand joints and fingertips.
- **Visualization:** Synchronous rendering of topology connections (skeleton) and specific keypoints (fingertips) over the origin frame.
- **Resilient Execution:** Automated environment path resolution and structural validations, preventing runtime exceptions on missing peripherals or model dependencies.

## System Architecture
The application leverages the `MediaPipe vision HandLandmarker` module passing standard RGB frames into a lightweight Convolutional Neural Network (CNN). The inference pipeline outputs normalized coordinates corresponding to hand topology, which are denormalized and overlaid back onto the BGR frame buffer via OpenCV before rendering.

## Project Structure
```text
.
├── models/
│   └── hand_landmarker.task   # Pre-trained CNN weights
├── src/
│   └── main.py                # Pipeline execution and rendering logic
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

1. Clone the repository to the local environment.
2. Install the necessary Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the pre-trained model file (`hand_landmarker.task`) is located in the `models/` directory.

## Usage

Execute the main pipeline directly from the repository root:
```bash
python src/main.py
```

- Operational Metrics: The system expects uncontested access to system video device index `0`.
- Termination: Send `q` to the active window context to safely release hardware hooks and terminate the application.

## Constraints and Considerations
- **Hardware Access:** The current implementation hard-binds to video device index `0`. Execution will fail if the peripheral is in use by another process.
- **Model Dependency:** Execution strictly requires the MediaPipe task bundle.
- **Computation:** The inference pipeline operates on the host CPU. Performance variance is expected based on hardware clock speeds and concurrency.

## Future Improvements
- Migration to asynchronous frame fetching to unblock the main processing thread.
- Hardware acceleration (GPU delegate) integration via TensorFlow Lite.
- Configuration parameterization for detection confidence thresholds and input device indices via command-line arguments.
