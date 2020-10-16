import numpy as np
import time
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

img = cv2.imread('Notif.jpeg')
img2 = cv2.imread('NotifCloning.jpeg')

eye_flag = True
show_count = True
blink_count = True
blink_count = 0

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in face:
        eye_flag = False
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eye = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

        for (mx, my, mw, mh) in eye:
            eye_flag = True
            cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (255, 255, 0), 2)
    if eye_flag:
        show_count = True

    if show_count and not (eye_flag):
        show_count = False
        blink_count += 1

    if blink_count >= 10:
        font = cv2.FONT_HERSHEY_SIMPLEX

        img = cv2.putText(img, 'Mata Lelah. Berhenti sejenak ',
                          (10, 150), font, 1, (0, 0, 255), 2)

        cv2.imshow('Notif', img)

    if blink_count >= 5:
        font = cv2.FONT_HERSHEY_SIMPLEX

        img2 = cv2.putText(img2, 'Mata Kering. Berkedip lagi ',
                           (10, 150), font, 1, (0, 0, 255), 2)

        cv2.imshow('NotifCloning', img2)
    font = cv2.FONT_HERSHEY_SIMPLEX

    frame = cv2.putText(frame, 'Blink count = ' + str(blink_count),
                        (25, 50), font, 1, (0, 255, 0), 2)

    cv2.imshow('Blink detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
