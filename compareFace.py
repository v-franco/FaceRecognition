import pandas
import numpy
from matrixReduction import recoverNewFace
from matrixRecognition import Image2Vector, Image2VectorReduced, Similiarity

def original(similarityMethod):

    # Leemos el dataset ya codificado
    DF = pandas.read_csv("Faces.csv")



    # Demostracion la cara de el renglon 9
    #print(DF.loc[[9], "File"])

    xq = Image2Vector('instance/photos/NewFace.jpg')

    #print(xq)

    # Demostracion el vector de la cara 8
    #xq = numpy.asarray(DF.iloc[[9],1:])[0]

    # Elimino de la base de datos la cara a buscar
    #DF = DF.drop([9]) # Quita la cara de la persona a buscar

    # Extraer la matriz de diseño del dataframe
    X = numpy.asarray(DF.iloc[:,1:])

    # Reset a los indices
    #DF = DF.reset_index(drop =True)

    Sim = [] # Arreglo de similitud

    # Tarea quitar este ciclo for de las lineas 24 - 31 (Participacion)

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
        

    #print(DF.iloc[Idx[0:5]])
    # print(DF.iloc[Idx[0:1],[0]] )
    # print(DF.loc[Idx[0:1],['File']] )
    for i in range(0,4):
        j = i+1
        print('FACE NUMBER: ',j)
        faceFound = str(DF.iloc[Idx[i:j],[0]])
        faceFoundS = faceFound.split()
        user = faceFoundS[2].split("\\")
        print("ORIGINAL:")
        if similarityMethod == 'L2':
            print("ACCURACY USING L2: ",    abs(((Sim[Idx[i]]))-1)*100, "%")
        if similarityMethod == 'CosineSimilarity':
            print("ACCURACY USING COSINE SIMILARITY: ",    abs(((Sim[Idx[i]])))*100, "%")
        if similarityMethod == 'Manhattan':
            print("ACCURACY USING Manhattan: ",    abs(((SimNorm[Idx[i]]))-1)*100, "%")
        print("User: ", user[1])
        print("File: "+user[0]+"/"+user[1]+"/"+user[2])
        print("-----------------------------------------")


def reduced(ModelType, similarityMethod):
    xq = recoverNewFace(1, ModelType)
    # Leemos el dataset ya codificado
    if(ModelType==1):
        DF = pandas.read_csv("PCA.csv")

    if(ModelType==2):
        DF = pandas.read_csv("SVD.csv")

    # Demostracion la cara de el renglon 9
    #print(DF.loc[[9], "File"])


    #xq = Image2Vector('instance/photos/NewFace.jpg')

    #print(xq)

    # Demostracion el vector de la cara 8
    #xq = numpy.asarray(DF.iloc[[9],1:])[0]

    # Elimino de la base de datos la cara a buscar
    #DF = DF.drop([9]) # Quita la cara de la persona a buscar

    # Extraer la matriz de diseño del dataframe
    X = numpy.asarray(DF.iloc[:,1:])

    # Reset a los indices
    #DF = DF.reset_index(drop =True)

    Sim = [] # Arreglo de similitud

    # Tarea quitar este ciclo for de las lineas 24 - 31 (Participacion)

    

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
        

    # print(DF.iloc[Idx[0:1],[0]] )
    # print(DF.loc[Idx[0:1],['File']] )

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
        if similarityMethod == 'CosineSimilarity':
            print("ACCURACY USING COSINE SIMILARITY: ",    abs(((Sim[Idx[i]])))*100, "%")
        if similarityMethod == 'Manhattan':
            print("ACCURACY USING Manhattan: ",    abs(((SimNorm[Idx[i]]))-1)*100, "%")
        print("User found", user[0])
        print("File: ", "photos/TC3002B_Faces/"+user[0]+"/"+user[1])
        print("-----------------------------------------")


def main():
    original('L2')
    reduced(1, 'L2')
    reduced(2, 'L2')
    original('CosineSimilarity')
    reduced(1, 'CosineSimilarity')
    reduced(2, 'CosineSimilarity')
    original('Manhattan')
    reduced(1, 'Manhattan')
    reduced(2, 'Manhattan')


if __name__ == "__main__":
   main()