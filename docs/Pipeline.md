## Implementación de un pipeline

<a href = "https://github.com/DaColcha/breast-cancer-prediction/blob/e1c77ba57b64ac373abbb37675f545cab42e6ed6/src/breast_cancer_flow.py"> *Pipeline completo* </a> 

<a href = "https://github.com/DaColcha/breast-cancer-prediction/blob/e1c77ba57b64ac373abbb37675f545cab42e6ed6/src/model_pipeline.py"> *Pipeline con transformación de datos y creación del modelo* </a> 


Hemos utilizado un pipeline completo con `MetaFlow` y registro en `MLflow` donde incluimos los pasos fundamentales como: cargar los datos, separar los datos, entrenamiento del modelo, validación del modelo y registro del modelo. Dado el tamaño de nuestro dataset, simplemente se utilizaron 2 conjuntos de datos: entrenamiento y validación. 

En esta parte se ejecutaron 5 pruebas, dado que como se puede visualizar en la imagen, inicialmente existió mucho overfitting hasta que la última de nuestras ejecuciones resultó tener un desempeño más adecuado. 

<img src="https://github.com/DaColcha/breast-cancer-prediction/blob/116035f56cb179cd7364541aefa3644e2671b56e/docs/images/chart-mlflow.png" width = 700px>
<br><br>
De esta manera, el modelo selecionado tiene las siguientes características: 

<img src="https://github.com/DaColcha/breast-cancer-prediction/blob/116035f56cb179cd7364541aefa3644e2671b56e/docs/images/final-model-metrics.png" width = 700px>
<br><br>
