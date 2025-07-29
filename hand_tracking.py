import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))
                print(id, cx, cy)
                if id == 4 :
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                if id == 8 :
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                if id == 12 :
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                if id == 16 :
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                if id == 20 :
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

                if len(lmList) >= 9:
                    # Get position of thumb and index tip
                    thumb_tip = lmList[4][1:3]
                    index_tip = lmList[8][1:3]
                    # Calculate thumb and index distance by Euclid Distance
                    distance = ((thumb_tip[0] - index_tip[0]) ** 2 + (thumb_tip[1] - index_tip[1]) ** 2) ** 0.5
                    # If thumb and index close by then it's "OK" gesture
                    if distance < 40:
                        cv2.putText(img, "OK gesture!", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()