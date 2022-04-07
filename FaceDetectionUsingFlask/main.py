# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

import cv2

window_name = "WebCamPreview"

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier( cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

while cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE):
    _, frame = video.read()

    face = face_cascade.detectMultiScale(frame, 1.3, 5)
    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow(window_name, frame)
    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:    # 27 for Esc key
        break
video.release()
cv2.destroyAllWindows()
