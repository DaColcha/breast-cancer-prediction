## Modelado y evaluación 
Como se estableció en el análisis inicial, se inició el entrenamiento de modelos con diferente número de componentes principales.

<a href = "https://github.com/DaColcha/breast-cancer-prediction/blob/49bca5189337c7642cdfa4296c849642444e1b5b/notebooks/training-2pca.ipynb"> *Notebook Entreamiento utilizando 2 componentes principales* </a> 

<a href = "https://github.com/DaColcha/breast-cancer-prediction/blob/49bca5189337c7642cdfa4296c849642444e1b5b/notebooks/training-15pca.ipynb"> *Notebook Entreamiento utilizando 15 componentes principales* </a> 

Se utilizó un modelo de `Random Forests Classifier` donde con la ayuda de la técnica de `grid_search` junto con`cross_validation` se pudieron evaluar y comparar las métricas de nuestro interés `accuracy y recall`. Cabre recalcar que solamente se utilizó el `grid_search` para el modelo que tilizaba los datos con 15 componentes, pues para aquel que solamente utilizaba 2 no existía mucha variación con los hiperparámetros. 

Por otro lado, se creó una red neuronal con `Keras`. Para ambos casos se crearon con poca diferencia en el número de capas *(en consideración al número de entradas)*, radio de aprendizaje, función de pérdida, métrica de evaluación y número de épocas.
De esto se pudo concluir que generar una red neuronal que tenga como entrada un dataset de 15 features sería más factible según el propósito de nuestro proyecto, siendo la métrica decisiva el valor de F1 score teniendo *94.12% vs 95.12.* 

Sin embargo, los resultados de la aplicación de la red neuronal no difireron de aquellos que obtuvimos con `RandomForestClassifier()`, es por ello que este último lo hemos elegido para la creación del pipeline y la puesta en producción. 


[Volver al inicio](https://github.com/DaColcha/breast-cancer-prediction/blob/46bcfee97eb212c329361f0c4327c39bf4cc4597/README.md)