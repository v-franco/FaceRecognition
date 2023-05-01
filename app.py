import os
import io
from werkzeug.utils import secure_filename
from faceRecognition import plotA
from camera_func import *

from flask import *

app = Flask(__name__)

os.makedirs(os.path.join(app.instance_path, 'photos'), exist_ok=True)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/upload')
def upload():
   return render_template('upload.html')

@app.route('/plot')
def plot():
   plotA()
   return 'plot uploaded successfully'
   #return render_template('plot.html', url='/static/images/plot.png')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.filename = 'NewFace.jpg'
      f.save(os.path.join(app.instance_path, 'photos', secure_filename(f.filename)))
      return 'file uploaded successfully'

#Route to test camera shit
@app.route('/video_feed')
def video_feed():
   return Response(gen_frames(), mimetype = 'multipart/x-mixed-replace; boundary=frame')



@app.route('/camera_shot', methods = ['POST', 'GET'])
def tasks():
   global camera

   if request.method == 'POST':
      if request.form.get('click') == 'Capture':
         variables.capture = 1
   
   elif request.method == 'GET':
      return render_template('camera.html')
   
   return render_template('camera.html')

if __name__ == '__main__':
   app.run()
