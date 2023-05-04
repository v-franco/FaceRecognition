from IPython.lib.display import FileLinks
import pandas
import numpy
import cv2
import face_recognition
import glob
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
from itertools import chain
from numpy.linalg import norm


def DesignMatrix(Options):
  Files = glob.glob("photos/TC3002B_Faces/*/*.jpg")
  OutFile = Options.OutFile # Nombre del archivo de salida en CSV
  X = [] # Matriz de diseño vacia
  L = [] # Etiquetas de a quien pertenece la fotografia
  for File in Files:
    # Leer la imagen de la cara y guardala en la matrix X como un vector
    #x = numpy.random.rand(512);
    x = Image2Vector(File)
    X.append(x)
    L.append(File)
    print(File)

  DF = pandas.DataFrame(X)
  DF.insert(0,"File",L)
  DF.to_csv(Options.OutFile, index = False)

def Image2Vector(File):
  I = cv2.imread(File) # Leer la imagen de la foto
  AR = 480 / I.shape[1] # Aspect Ratio
  width = int(I.shape[1] * AR)
  height = int(I.shape[0] * AR)
  # Reescalamiento
  I = cv2.resize(I, (width,height), interpolation = cv2.INTER_AREA)
  cv2.imwrite("temp.jpg", I)
  # Guardar archivo temporal de la imagen guardada
  FID = face_recognition.load_image_file("temp.jpg") # carga de imagen reescalada
  Locations = face_recognition.face_locations(FID)
  FaceVectors = face_recognition.face_encodings(FID, Locations)
  x = FaceVectors[0]
  return x


# función Similarity recibe los vectores de los rostros a comparar y el método de comparación a usar
# Contiene 3 métodos de comparación: Distancia Euclidiana L2, similaridad de cosenos, y método Manhattan
def Similiarity(a,b, compareMethod):
  if compareMethod == 'L2':
    return numpy.linalg.norm(a-b)
  if compareMethod == 'CosineSimilarity':
    numpyA = numpy.array([a])
    numpyB = numpy.array([b])
    cosSim = (cosine_similarity(numpyA,numpyB))
    return cosSim[0][0]
  if compareMethod == 'Manhattan':
        distance = 0
        for x1, x2 in zip(a, b):
            difference = x2 - x1
            absolute_difference = abs(difference)
            distance += absolute_difference
  return distance

#runOnce genera la matriz de 128 dimensiones
def runOnce():
    class Opt:
        pass

    Options = Opt

    Options.SPath = "photos/TC3002B_Faces/"
    Options.OutFile = "Faces.csv"

    DesignMatrix(Options)


