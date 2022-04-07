from flask import Flask, render_template, Response
from camera import Video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def generate(cam):
    while True:
        frame = cam.getFrame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@app.route('/video')

def video():
    return Response(generate(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)