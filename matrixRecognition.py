from IPython.lib.display import FileLinks
import pandas
import numpy
import cv2
import face_recognition
import glob
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# Esto solo se hace una vez en el BackEnd

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

def Image2VectorReduced(File):
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
  XM = []
  XM.append(x)
  XM.append(x)
  L = 'newFace'
  DF = pandas.DataFrame(XM)
  DF.insert(0,"File",L)
  #print(DF)
  DF = DF.iloc[:,1:]
  scalar = StandardScaler()
  scaled_data = pandas.DataFrame(scalar.fit_transform(DF)) #scaling the data
 # print("SCALED DATA")
 # print(scaled_data)
  pca = PCA(n_components = 2)
  pca.fit(scaled_data)
  data_pca = pca.transform(scaled_data)
  data_pca = pandas.DataFrame(data_pca,columns=['PC1','PC2'])
  print(data_pca)
  return x

def Similiarity(a,b):
  # metrica de similitud
  # depende de la naturaleza del manifold
  # puede ser que se haga pequeña (caso L2) o se haga grande (caso Producto interno)
  # Tarea: tener varias metricas en esta funcion para seleccionar una
  return numpy.linalg.norm(a-b)


def runOnce():
    class Opt:
        pass

    Options = Opt

    Options.SPath = "photos/TC3002B_Faces/"
    Options.OutFile = "Faces.csv"

    DesignMatrix(Options)


