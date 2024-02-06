## Análisis y procesamiento de datos

<a href = "https://github.com/DaColcha/breast-cancer-prediction/blob/49bca5189337c7642cdfa4296c849642444e1b5b/notebooks/data-preparation.ipynb"> *Notebook Análisis y procesamiento de datos* </a> 

Para empezar, se extrajeron los datos y se inició la exploración donde inicialmente se tenían 32 features y 569 observaciones, todas las features estaban en tipo `float64` y no existían valores nulos ni duplicados. 
Después de la descripción de los datos, se visualizó la correlación entre las variables donde algunas de las features no parecían tener una relación que impacte en la variable objetivo. 
Junto con esto se hizo una evaluación de características importantes con ayuda de `KGBClassifier`, de esto se notó que existían muchas caracerísticas que no presentaban relevancia significativa. Se realizaron evaluaciones simplemente eliminando la mitad de las variables, pero por supuesto esto no resulta efectivo dado que muchas de las características eliminadas pudieron presentar puntos cruciales para diferenciar una observación. De hecho, algo interesante fue que el modelo presentó los mismos resultados con y sin la mitad de las features.  
Lo propio, se aplicó `PCA` para redimensionar los datos de tal manera que todas las variables sean tomadas en cuenta y se determinó que la mejor opción sería evaluar los modelos utilizando 2 y 15 componentes. 

[Volver al inicio](https://github.com/DaColcha/breast-cancer-prediction/blob/46bcfee97eb212c329361f0c4327c39bf4cc4597/README.md)