import cv2
import mediapipe as mp
import pyautogui
import math

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # mirror effect
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    thumb_x, thumb_y = 0, 0
    index_x, index_y = 0, 0

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                x, y = int(lm.x * w), int(lm.y * h)

                if id == 4:  # thumb tip
                    thumb_x, thumb_y = x, y

                if id == 8:  # index finger tip
                    index_x, index_y = x, y

                    # move mouse
                    screen_x = screen_width * lm.x
                    screen_y = screen_height * lm.y
                    pyautogui.moveTo(screen_x, screen_y)

            # draw hand
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # click detection (distance between thumb & index)
            distance = math.hypot(thumb_x - index_x, thumb_y - index_y)

            if distance < 30:
                pyautogui.click()
                pyautogui.sleep(0.3)  # prevent multiple clicks

    cv2.imshow("Hand Gesture Mouse", img)

    if cv2.waitKey(1) == 27:  # press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()