from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import Isomap
from matplotlib import pyplot
from matrixRecognition import Image2Vector, Similiarity
import pandas
import numpy

DF = pandas.read_csv("Faces.csv")

X = numpy.asarray(DF.iloc[:,1:])
print(X)

Models = {
    "PCA":PCA(n_components = 2),
    "SVD":TruncatedSVD(n_components = 2),
    "ISOmap":Isomap(n_components = 2)
    }


fig, ax = pyplot.subplots(1,3, figsize = [16,6] );

for k, Model in enumerate(Models.keys()):
  ax[k].set_title(Model)
  Model = Models.get(Model)
  X_hat = Model.fit_transform(X)
  for var in DF.File.unique():
    ax[k].plot(X_hat[DF.File == var,0], X_hat[DF.File == var,1], linestyle = "None", marker = ".", label = var)
  

pyplot.show()