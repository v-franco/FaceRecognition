from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import Isomap
from matplotlib import pyplot
from matrixRecognition import Image2Vector, Similiarity
import pandas
import numpy
from sklearn.preprocessing import StandardScaler
import glob

DF = pandas.read_csv("Faces.csv")
# print("DATAFRAME:")
DF = DF.iloc[:,1:]

# X = numpy.asarray(DF.iloc[:,1:])
# print(X)
# print(DF)

scalar = StandardScaler()
scaled_data = pandas.DataFrame(scalar.fit_transform(DF)) #scaling the data
# print("SCALED DATA")
# print(scaled_data)

pca = PCA(n_components = 2)
pca.fit(scaled_data)
data_pca = pca.transform(scaled_data)
data_pca = pandas.DataFrame(data_pca,columns=['PC1','PC2'])
print(data_pca)

class Opt:
        pass

Options = Opt

Options.SPath = "photos/TC3002B_Faces/"
Options.OutFile = "Faces2.csv"

Files = glob.glob("photos/TC3002B_Faces/*/*.jpg")
L = []
for file in Files:
        newName = file[21:]
        finalName = newName.split("/")
        
        L.append(finalName[0])


data_pca.insert(0,"File",L)
data_pca.to_csv(Options.OutFile, index = False)


# Models = {
#     "PCA":PCA(n_components = 2),
#     "SVD":TruncatedSVD(n_components = 2),
#     "ISOmap":Isomap(n_components = 2)
#     }


# fig, ax = pyplot.subplots(1,3, figsize = [16,6] );

# for k, Model in enumerate(Models.keys()):
#   ax[k].set_title(Model)
#   Model = Models.get(Model)
#   X_hat = Model.fit_transform(X)
#   for var in DF.File.unique():
#     ax[k].plot(X_hat[DF.File == var,0], X_hat[DF.File == var,1], linestyle = "None", marker = ".", label = var)
  

# pyplot.show()