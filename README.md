
                            El sistema toma una foto e identifica a la persona comparando con el set de entrenamiento de alumnos de la materia TC3002B.2
							Se desarrollaron scripts de Python que permiten realizar 
                            identificación facial utilizando distintos métodos de preparación de datos
                            y de comparación facial
                            El script MatrixRecogntion vectoriza las caras del dataset por medio de la librería face_recognition,
                                 generando una matriz de 128 dimensiones. También contiene la función implementada que permite la comparación de rostros.

                            El script MatrixReduction reduce la dimensionalidad de la matriz generada anteriormente utilizando dos modelos:
                                PCA y SVD.
 
                           <La función implementada en MatrixRecogntion cuenta con tres métodos de comparación vectorial: Distancia euclidiana L2, similaridad de cosenos,
                            y método Manhattan.

                            <El script CompareFace utiliza las matrices generadas en MatrixRecogntion y MatrixReduction junto con el método de comparación seleccionado
                                para generar las cuatro caras en el dataset con mayor probabilidad de ser la persona de la foto tomada por el sistema.
