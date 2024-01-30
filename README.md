# Predicción de cáncer de mama

- [Análisis y procesamiento de datos](#análisis-y-procesamiento-de-datos)
- [Modelado y evaluación](#modelado-y-evaluación)
- [Implementación Pipelines](#implementación-de-un-pipeline)
- [Despliegue del modelo](#despliegue-del-modelo)

<hr>

Proyecto propuesta con el que se busca poder colaborar con clínicas que trabajen en la especialidad de oncología para poder mejorar su exactitud en la toma de decisiones en el momento de tratar tumores sospechosos. 

<a href = "https://github.com/DaColcha/breast-cancer-prediction/blob/main/docs/Proyect-Spec.md"> *Especificaciones proyecto* </a> 

*Tecnologías utilizadas*
<br/><br/>
 <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" height=30px> <img src="https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white" height=30px>  <img src="https://img.shields.io/badge/Keras-FF0000?style=for-the-badge&logo=keras&logoColor=white" height=30px> <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" height=30px> <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" height=30px>


## Análisis y procesamiento de datos

<a href = "https://github.com/DaColcha/breast-cancer-prediction/blob/49bca5189337c7642cdfa4296c849642444e1b5b/notebooks/data-preparation.ipynb"> *Notebook Análisis y procesamiento de datos* </a> 

Para empezar, se extrajeron los datos y se inició la exploración donde inicialmente se tenían 32 features y 569 observaciones, todas las features estaban en tipo `float64` y no existían valores nulos ni duplicados. 
Después de la descripción de los datos, se visualizó la correlación entre las variables donde algunas de las features no parecían tener una relación que impacte en la variable objetivo. 
Junto con esto se hizo una evaluación de características importantes con ayuda de `KGBClassifier`, de esto se notó que existían muchas caracerísticas que no presentaban relevancia significativa. Se realizaron evaluaciones simplemente eliminando la mitad de las variables, pero por supuesto esto no resulta efectivo dado que muchas de las características eliminadas pudieron presentar puntos cruciales para diferenciar una observación. De hecho, algo interesante fue que el modelo presentó los mismos resultados con y sin la mitad de las features.  
Lo propio, se aplicó `PCA` para redimensionar los datos de tal manera que todas las variables sean tomadas en cuenta y se determinó que la mejor opción sería evaluar los modelos utilizando 2 y 15 componentes. 

## Modelado y evaluación 
Como se estableció en el análisis inicial, se inició el entrenamiento de modelos con diferente número de componentes principales.

<a href = "https://github.com/DaColcha/breast-cancer-prediction/blob/49bca5189337c7642cdfa4296c849642444e1b5b/notebooks/training-2pca.ipynb"> *Notebook Entreamiento utilizando 2 componentes principales* </a> 

<a href = "https://github.com/DaColcha/breast-cancer-prediction/blob/49bca5189337c7642cdfa4296c849642444e1b5b/notebooks/training-15pca.ipynb"> *Notebook Entreamiento utilizando 15 componentes principales* </a> 

Se utilizó un modelo de `Random Forests Classifier` donde con la ayuda de la técnica de `cross_validation` se pudieron evaluar y comparar las métricas donde de cierta manera para nuestro propósito el valor del recall era más valioso, por lo cual en esta primera parte los 15 componentes funcionaron solamente un poco mejor a diferencia de usar 2 componentes. 

Por otro lado, se creó una red neuronal con `Keras`. Para ambos casos se crearon con poca diferencia en el número de capas *(en consideración al número de entradas)*, radio de aprendizaje, función de pérdida, métrica de evaluación y número de épocas.
De esto se pudo concluir que generar una red neuronal que tenga como entrada un dataset de 15 features sería más factible según el propósito de nuestro proyecto, siendo la métrica decisiva el valor de F1 score teniendo *94.12% vs 95.12.*

## Implementación de un pipeline

## Despliegue del modelo

## Referencias
<a href="https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic"><img src="https://img.shields.io/badge/UC%20Irvine-blue?style=for-the-badge" height=20px /></a> <br/>
Wolberg,William, Mangasarian,Olvi, Street,Nick, and Street,W.. (1995). Breast Cancer Wisconsin (Diagnostic). UCI Machine Learning Repository. https://doi.org/10.24432/C5DW2B.