import cv2
import mediapipe as mp
import time

# Start webcam capture
cap = cv2.VideoCapture(0)

# Initialize MediaPipe Hands module
mpHands = mp.solutions.hands
hands = mpHands.Hands()

# For drawing hand landmarks
mpDraw = mp.solutions.drawing_utils

# Variables for calculating FPS
pTime = 0
cTime = 0

while True:
    # Read frame from webcam
    success, img = cap.read()
    
    # Flip the image horizontally (mirror view)
    img = cv2.flip(img, 1)
    
    # Convert BGR image to RGB (required by MediaPipe)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Process the image and detect hands
    results = hands.process(imgRGB)

    # Check if any hand is detected
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            
            # Loop through each landmark (21 points of hand)
            for id, lm in enumerate(handLms.landmark):
                
                # Get image height, width
                h, w, c = img.shape
                
                # Convert normalized coordinates to pixel values
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                # Print landmark id and coordinates
                print(id, cx, cy)

                # Draw circles on fingertip landmarks
                # 4 = thumb tip
                # 8 = index finger tip
                # 12 = middle finger tip
                # 16 = ring finger tip
                # 20 = pinky tip
                if id == 4:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                if id == 8:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                if id == 12:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                if id == 16:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                if id == 20:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            # Draw full hand connections (skeleton)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # Calculate Frames Per Second (FPS)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display FPS on screen
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    # Show the output window
    cv2.imshow("Image", img)

    # Press 'q' to exit the program
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Release camera and close all windows
cap.release()
cv2.destroyAllWindows()