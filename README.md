# Predicción de cáncer de mama

Proyecto propuesta con el que se busca poder colaborar con clínicas que trabajen en la especialidad de oncología para poder mejorar su exactitud en la toma de decisiones en el momento de tratar tumores sospechosos. 

### *Tecnologías utilizadas*
 <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" height=30px> <img src="https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white" height=30px>  <img src="https://img.shields.io/badge/Keras-FF0000?style=for-the-badge&logo=keras&logoColor=white" height=30px> <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" height=30px> <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" height=30px>

## Prueba el modelo desde Docker

Entra a docker hub dando clic aquí:<br><br>
<a href = "https://hub.docker.com/repository/docker/dacolcha/cancer_predictor/general"> <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" height=30px> </a>

*Importante: utilizar la última versión 3.0*

#### - Comando docker sugerido 
docker run -p 3000:3000 dacolcha/cancer_predictor:3.0

#### - Puedes guiarte del notebook:
*(Recuerda cambiar la url del endpoint)* <br>
<a href = "https://github.com/DaColcha/breast-cancer-prediction/blob/c56aeee0ca0f84168899cfe0996ec4c00b428802/notebooks/service-test.ipynb"> *Prueba del servicio* </a> 

## Documentación
- [Especificaciones del Proyecto](https://github.com/DaColcha/breast-cancer-prediction/blob/e1c77ba57b64ac373abbb37675f545cab42e6ed6/docs/Project-Spec.md)
- [Análisis y procesamiento de datos](https://github.com/DaColcha/breast-cancer-prediction/blob/fc7f9c5bba7e12072acbc7ad39a36244bbd2b21a/docs/Data-preprocessing.md)
- [Modelado y evaluación](https://github.com/DaColcha/breast-cancer-prediction/blob/fc7f9c5bba7e12072acbc7ad39a36244bbd2b21a/docs/Model-evaluation.md)
- [Implementación Pipelines](https://github.com/DaColcha/breast-cancer-prediction/blob/75559f00ef7c137ae485ac466ef82ca0b6818e51/docs/Pipeline.md)
- [Despliegue del modelo](https://github.com/DaColcha/breast-cancer-prediction/blob/fc7f9c5bba7e12072acbc7ad39a36244bbd2b21a/docs/Despliegue.md)


## Referencias
<a href="https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic"><img src="https://img.shields.io/badge/UC%20Irvine-blue?style=for-the-badge" height=20px /></a> <br/>
Wolberg,William, Mangasarian,Olvi, Street,Nick, and Street,W.. (1995). Breast Cancer Wisconsin (Diagnostic). UCI Machine Learning Repository. https://doi.org/10.24432/C5DW2B.