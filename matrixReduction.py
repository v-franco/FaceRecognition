from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import Isomap
from matplotlib import pyplot
from matrixRecognition import Image2Vector, Similiarity
import pandas
import numpy
from sklearn.preprocessing import StandardScaler
import glob


def recoverNewFace(bandera_error):
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

    # print(DF)
    # print(DF2)
    X = numpy.asarray(DF.iloc[:,1:])
    # print(X)
    # print(DF)
    # print(X)
    Model = PCA(n_components=2)
    Model.fit(X)

    data_pca = Model.transform(X)
    data_pca = pandas.DataFrame(data_pca,columns=['PC1','PC2'])
    #print(data_pca)


    xqFinal = Model.transform(xqFinal.reshape(1, -1))

    if(bandera_error == 1):
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


    return xqFinal

