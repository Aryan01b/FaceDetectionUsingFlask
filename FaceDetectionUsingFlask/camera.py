import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class Video(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def getFrame(self):
        _, frame = self.video.read()
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        for x,y,w,h in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        _, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()