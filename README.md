# Hand Tracking using MediaPipe

This Python script utilizes the MediaPipe library to perform hand tracking in real-time using your webcam. It detects hand landmarks and draws connections between them, allowing you to visualize hand movements.

## Sample Output

![Hand Tracking Output](Screenshot.png)

---
## Prerequisites

Before running the script, ensure you have the following installed:

- Python (version 3.7 or higher)
- OpenCV (`opencv-python` package)
- MediaPipe (`mediapipe` package)

You can install the required packages using pip:

```
pip install opencv-python mediapipe
```

## Usage

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python:

```
python hand_tracking.py
```

4. A window will pop up displaying your webcam feed with hand tracking overlay.
5. Press 'q' to exit the program.

## Code Explanation

- The script captures video input from your webcam (`cv2.VideoCapture`).
- It utilizes MediaPipe's `Hands` model to detect hand landmarks in each frame.
- Detected landmarks are used to draw circles at specific key points on the hand (e.g., fingertips, base).
- Hand connections are drawn between landmarks to visualize hand structure.
- The script calculates and displays frames per second (FPS) to monitor performance.
- Pressing 'q' quits the application.

## Mediapipe Hand Landmarks

![Hand Tracking Output](hand-landmarks.png)

---
