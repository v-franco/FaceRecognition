import pandas
import numpy
from matrixReduction import recoverNewFace
from matrixRecognition import Image2Vector, Similiarity


def original(similarityMethod):

    arrayAux = []
    # Leemos el dataset ya codificado
    DF = pandas.read_csv("Faces.csv")

    xq = Image2Vector('instance/photos/NewFace.jpg')

    # Extraer la matriz de diseño del dataframe
    X = numpy.asarray(DF.iloc[:,1:])

    Sim = [] # Arreglo de similitud

    for xi in X:
        sim = Similiarity(xq, xi, similarityMethod)
        Sim.append(sim)

    Sim = numpy.asarray(Sim)

    if similarityMethod == 'L2':

        Idx = numpy.argsort(Sim)

    if similarityMethod == 'CosineSimilarity':

        Idx = numpy.argsort(Sim)[::-1]

    if similarityMethod == 'Manhattan':

        SimNorm = (Sim-numpy.min(Sim))/(numpy.max(Sim)-numpy.min(Sim))

        Idx = numpy.argsort(SimNorm)
        
    
    for i in range(0,4):
        j = i+1
        print('FACE NUMBER: ',j)
        faceFound = str(DF.iloc[Idx[i:j],[0]])
        faceFoundS = faceFound.split()
        user = faceFoundS[2].split("\\")
        print("ORIGINAL:")
        if similarityMethod == 'L2':
            print("ACCURACY USING L2: ",    abs(((Sim[Idx[i]]))-1)*100, "%")
            value = abs(((Sim[Idx[i]]))-1)*100
        if similarityMethod == 'CosineSimilarity':
            print("ACCURACY USING COSINE SIMILARITY: ",    abs(((Sim[Idx[i]])))*100, "%")
            value = abs(((Sim[Idx[i]])))*100
        if similarityMethod == 'Manhattan':
            print("ACCURACY USING Manhattan: ",    abs(((SimNorm[Idx[i]]))-1)*100, "%")
            value = abs(((SimNorm[Idx[i]]))-1)*100
        print("User: ", user[1])
        print("File: "+user[0]+"/"+user[1]+"/"+user[2])
        userStr = str(user[0]+"/"+user[1]+"/"+user[2])
        arrayAux.append(userStr)
        arrayAux.append(str(value)+'%')
        print("-----------------------------------------")
    return arrayAux



def reduced(ModelType, similarityMethod):
    arrayAux = []
    xq = recoverNewFace(1, ModelType)
    # Leemos el dataset ya codificado
    if(ModelType==1):
        DF = pandas.read_csv("PCA.csv")

    if(ModelType==2):
        DF = pandas.read_csv("SVD.csv")


    # Extraer la matriz de diseño del dataframe
    X = numpy.asarray(DF.iloc[:,1:])

    Sim = [] # Arreglo de similitud


    for xi in X:
        if similarityMethod=='CosineSimilarity' or similarityMethod=='Manhattan':
            sim = Similiarity(xq[0], xi, similarityMethod)
            Sim.append(sim)
        else:
            sim = Similiarity(xq, xi, similarityMethod)
            Sim.append(sim)
  

    if similarityMethod == 'L2':

        Idx = numpy.argsort(Sim)

    if similarityMethod == 'CosineSimilarity':

        Idx = numpy.argsort(Sim)[::-1]

    if similarityMethod == 'Manhattan':

        SimNorm = (Sim-numpy.min(Sim))/(numpy.max(Sim)-numpy.min(Sim))

        Idx = numpy.argsort(SimNorm)
        


    for i in range(0,4):
        j = i+1
        print('FACE NUMBER: ',j)
        faceFound = str(DF.iloc[Idx[i:j],[0]])
        faceFoundS = faceFound.split()
        user = faceFoundS[2].split("\\")
        if ModelType == 1:
            print("REDUCED WITH PCA:")
        if ModelType == 2:
            print("REDUCED WITH SVD:")
        if similarityMethod == 'L2':
            print("ACCURACY USING L2: ",    abs(((Sim[Idx[i]]))-1)*100, "%")
            value = abs(((Sim[Idx[i]]))-1)*100
        if similarityMethod == 'CosineSimilarity':
            print("ACCURACY USING COSINE SIMILARITY: ",    abs(((Sim[Idx[i]])))*100, "%")
            value = abs(((Sim[Idx[i]])))*100
        if similarityMethod == 'Manhattan':
            print("ACCURACY USING Manhattan: ",    abs(((SimNorm[Idx[i]]))-1)*100, "%")
            value = abs(((SimNorm[Idx[i]]))-1)*100
        print("User found", user[0])
        print("File: ", "photos/TC3002B_Faces/"+user[0]+"/"+user[1])
        userStr = str("photos/TC3002B_Faces/"+user[0]+"/"+user[1])

        arrayAux.append(userStr)
        arrayAux.append(str(value)+'%')

        print("-----------------------------------------")
    return arrayAux

