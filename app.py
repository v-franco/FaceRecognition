import os
import io
from werkzeug.utils import secure_filename
from faceRecognition import plotA
from camera_func import *
import pprint

from flask import *
from compareFace import FrontEndArray, arrayAppendSVD, arrayAppendOg, arrayAppendPCA, original, reduced

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
def camera_shot():
    OriginalArray = []
    FinalPCA = []
    FinalSVD = []
    global camera
    if request.method == 'POST':
        if request.form.get('click') == 'Capturar':
            variables.capture = 1
            original('L2')
            OriginalArray.append(arrayAppendOg)
            original('CosineSimilarity')
            OriginalArray.append(arrayAppendOg)
            original('Manhattan')
            OriginalArray.append(arrayAppendOg)
            reduced(1, 'L2')

            FinalPCA.append(arrayAppendPCA)
            reduced(1, 'CosineSimilarity')
            FinalPCA.append(arrayAppendPCA)
            reduced(1, 'Manhattan')
            FinalPCA.append(arrayAppendPCA)

            reduced(2, 'L2')
            FinalSVD.append(arrayAppendSVD)
            reduced(2, 'CosineSimilarity')
            FinalSVD.append(arrayAppendSVD)
            reduced(2, 'Manhattan')
            FinalSVD.append(arrayAppendSVD)

            FrontEndArray.append(OriginalArray)
            FrontEndArray.append(FinalPCA)
            FrontEndArray.append(FinalSVD)
            backEndresults = []
            backEndresults = FrontEndArray
            pprint.pprint(backEndresults)
            # results = [
            #    [ # Original 128dim
            #       [ # L2
            #         'photos/TC3002B_Faces/A01365726/0.jpg',
            #         '0.00',
            #         'photos/TC3002B_Faces/A01365726/1.jpg',
            #         '0.11',
            #         'photos/TC3002B_Faces/A01365726/2.jpg',
            #         '0.22',
            #         'photos/TC3002B_Faces/A01365726/3.jpg',
            #         '0.33',
            #       ],
            #       [ # Cosenos
            #         'photos/TC3002B_Faces/A01365726/0.jpg',
            #         '0.00',
            #         'photos/TC3002B_Faces/A01365726/1.jpg',
            #         '0.11',
            #         'photos/TC3002B_Faces/A01365726/2.jpg',
            #         '0.22',
            #         'photos/TC3002B_Faces/A01365726/3.jpg',
            #         '0.33',
            #       ],
            #       [ # Manhattan
            #         'photos/TC3002B_Faces/A01365726/0.jpg',
            #         '0.00',
            #         'photos/TC3002B_Faces/A01365726/1.jpg',
            #         '0.11',
            #         'photos/TC3002B_Faces/A01365726/2.jpg',
            #         '0.22',
            #         'photos/TC3002B_Faces/A01365726/3.jpg',
            #         '0.33',
            #       ] 
            #    ],
            #    [ # PCA 2dim
            #       [ # L2
            #         'photos/TC3002B_Faces/A01366686/selfie_1.jpg',
            #         '0.00',
            #         'photos/TC3002B_Faces/A01366686/Selfie_2.jpg',
            #         '0.11',
            #         'photos/TC3002B_Faces/A01366686/selfie_1.jpg',
            #         '0.22',
            #         'photos/TC3002B_Faces/A01366686/selfie_4.jpg',
            #         '0.33',
            #       ],
            #       [ # Cosenos
            #         'photos/TC3002B_Faces/A01366686/selfie_1.jpg',
            #         '0.00',
            #         'photos/TC3002B_Faces/A01366686/Selfie_2.jpg',
            #         '0.11',
            #         'photos/TC3002B_Faces/A01366686/selfie_1.jpg',
            #         '0.22',
            #         'photos/TC3002B_Faces/A01366686/selfie_4.jpg',
            #         '0.33',
            #       ],
            #       [ # Manhattan
            #         'photos/TC3002B_Faces/A01366686/selfie_1.jpg',
            #         '0.00',
            #         'photos/TC3002B_Faces/A01366686/Selfie_2.jpg',
            #         '0.11',
            #         'photos/TC3002B_Faces/A01366686/selfie_1.jpg',
            #         '0.22',
            #         'photos/TC3002B_Faces/A01366686/selfie_4.jpg',
            #         '0.33',
            #       ]
                  
            #    ],
            #    [ # SVD 2dim
            #       [ # L2
            #         'photos/TC3002B_Faces/A01369422/jordi_1.jpg', # 0
            #         '0.00',
            #         'photos/TC3002B_Faces/A01369422/jordi_2.jpg',
            #         '0.11',
            #         'photos/TC3002B_Faces/A01369422/Jordi_3.jpg',
            #         '0.22',
            #         'photos/TC3002B_Faces/A01369422/Jordi_4.jpg',
            #         '0.33',
            #       ],
            #       [ # Cosenos
            #         'photos/TC3002B_Faces/A01369422/jordi_1.jpg',
            #         '0.00',
            #         'photos/TC3002B_Faces/A01369422/jordi_2.jpg',
            #         '0.11',
            #         'photos/TC3002B_Faces/A01369422/Jordi_3.jpg',
            #         '0.22',
            #         'photos/TC3002B_Faces/A01369422/Jordi_4.jpg',
            #         '0.33',
            #       ],
            #       [ # Manhattan
            #         'photos/TC3002B_Faces/A01369422/jordi_1.jpg',
            #         '0.00',
            #         'photos/TC3002B_Faces/A01369422/jordi_2.jpg',
            #         '0.11',
            #         'photos/TC3002B_Faces/A01369422/Jordi_3.jpg',
            #         '0.22',
            #         'photos/TC3002B_Faces/A01369422/Jordi_4.jpg',
            #         '0.33',
            #       ]
            #    ]
            # ]
            
			# change path names
            for matrix in backEndresults:
                for i in range(0, len(matrix)):
                    model = matrix[i]
                    for j in range(0, len(model), 2):
                        path = model[j]
                        new_path = "/".join(path.split("/")[1:])
                        new_path = "static/img/" + new_path 
                        model[j] = new_path
                        print(model[j])

            return render_template('models-selection.html', results=backEndresults)
   
    elif request.method == 'GET':
      return render_template('camera.html')
    
    return render_template('camera.html')

if __name__ == '__main__':
   app.run()
