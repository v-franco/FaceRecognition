from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import Isomap
from matplotlib import pyplot
from matrixRecognition import Image2Vector, Similiarity
import pandas
import numpy
from sklearn.preprocessing import StandardScaler
import glob

# Función visuals genera gráfica de dispersión de los modelos PCA y SVD.
def visuals():

    DF = pandas.read_csv("FacesReload.csv")

    X = numpy.asarray(DF.iloc[:,1:])

    Models = {
    "PCA":PCA(n_components = 2),
    "SVD":TruncatedSVD(n_components = 2),
    }
    fig, ax = pyplot.subplots(1,3, figsize = [16,6] );

    for k, Model in enumerate(Models.keys()):
        ax[k].set_title(Model)
        Model = Models.get(Model)
        X_hat = Model.fit_transform(X)
        for var in DF.File.unique():
            filename = str(DF.File)
            ax[k].plot(X_hat[DF.File == var,0], X_hat[DF.File == var,1], linestyle = "None", marker = ".", label = var)

    pyplot.show()


# Función recoverNewFace() realiza la reducción de la matriz original y de la cara nueva a comparar.
# Recibe el tipo de modelo 1: PCA, y 2: SVD
def recoverNewFace(bandera_error, modelType):
    DF = pandas.read_csv("Faces.csv")
    # print("DATAFRAME:")
    DF = DF.iloc[:,1:]
    xq = Image2Vector('instance/photos/NewFace.jpg')
    # print(xq)
    L = 'NewFace'
    matrixXq = []
    matrixXq.append(xq)
    DF2= pandas.DataFrame(matrixXq)
    DF2.insert(0,"File",L)
    DF2 = DF2.iloc[:,1:]

    xqFinal = numpy.asarray(DF2.iloc[:,1:])

    X = numpy.asarray(DF.iloc[:,1:])
    if modelType == 1:
        
        Model = PCA(n_components=2)
        Model.fit(X)

        data_pca = Model.transform(X)
        data_pca = pandas.DataFrame(data_pca,columns=['PC1','PC2'])
        #print(data_pca)

        class Opt:
                pass

        Options = Opt

        Options.SPath = "photos/TC3002B_Faces/"
        Options.OutFile = "PCA.csv"

        Files = glob.glob("photos/TC3002B_Faces/*/*.jpg")
        L = []
        for file in Files:
                    newName = file[21:]
                    finalName = newName.split("/")
                    
                    L.append(finalName[0])


        data_pca.insert(0,"File",L)
        data_pca.to_csv(Options.OutFile, index = False)

        xqFinal = Model.transform(xqFinal.reshape(1, -1))




    if modelType == 2:

        Model = TruncatedSVD(n_components=2)
        Model.fit(X)

        data_pca = Model.transform(X)
        data_pca = pandas.DataFrame(data_pca,columns=['PC1','PC2'])
        
        class Opt:
                pass

        Options = Opt

        Options.SPath = "photos/TC3002B_Faces/"
        Options.OutFile = "SVD.csv"

        Files = glob.glob("photos/TC3002B_Faces/*/*.jpg")
        L = []
        for file in Files:
                    newName = file[21:]
                    finalName = newName.split("/")
                    
                    L.append(finalName[0])


        data_pca.insert(0,"File",L)
        data_pca.to_csv(Options.OutFile, index = False)

        xqFinal = Model.transform(xqFinal.reshape(1, -1))



    return xqFinal
