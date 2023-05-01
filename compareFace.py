import pandas
import numpy
from matrixReduction import recoverNewFace
from matrixRecognition import Image2Vector, Image2VectorReduced, Similiarity

def original():

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
        sim = Similiarity(xq, xi)
        Sim.append(sim)

    Sim = numpy.asarray(Sim)

    Idx = numpy.argsort(Sim)

    # print(DF.iloc[Idx[0:1],[0]] )
    # print(DF.loc[Idx[0:1],['File']] )
    faceFound = str(DF.iloc[Idx[0:1],[0]])
    faceFoundS = faceFound.split()
    user = faceFoundS[2].split("\\")
    print("ORIGINAL:")
    print("User: ", user[1])
    print("File: "+user[0]+"/"+user[1]+"/"+user[2])


def reduced():

    # Leemos el dataset ya codificado
    DF = pandas.read_csv("Faces2.csv")

    # Demostracion la cara de el renglon 9
    #print(DF.loc[[9], "File"])

    xq = recoverNewFace(0)

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
        sim = Similiarity(xq, xi)
        Sim.append(sim)

    Sim = numpy.asarray(Sim)

    Idx = numpy.argsort(Sim)

    # print(DF.iloc[Idx[0:1],[0]] )
    # print(DF.loc[Idx[0:1],['File']] )
    faceFound = str(DF.iloc[Idx[0:1],[0]])
    faceFoundS = faceFound.split()
    user = faceFoundS[2].split("\\")
    print("REDUCED:")
    print("User found", user[0])
    print("File: ", "photos/TC3002B_Faces/"+user[0]+"/"+user[1])

def main():
    original()
    reduced()


if __name__ == "__main__":
   main()