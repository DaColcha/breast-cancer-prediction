
## Despliegue del modelo

Para iniciar hemos descargado nuestro modelo registrado en MLflow para almacenarlo en BentoML

<a href = "https://github.com/DaColcha/breast-cancer-prediction/blob/116035f56cb179cd7364541aefa3644e2671b56e/service/download_model.py"> *Descarga del modelo* </a> 

Después, hemos diseñano un runner personalizado para poder entregar los datos enlazados con su id correspondiente.

<a href = "https://github.com/DaColcha/breast-cancer-prediction/blob/116035f56cb179cd7364541aefa3644e2671b56e/service/service.py"> *Servicio* </a> <br>
<a href = "https://github.com/DaColcha/breast-cancer-prediction/blob/116035f56cb179cd7364541aefa3644e2671b56e/service/runner.py"> *Runner personalizado* </a> 

Finalmente hemos probado este servicio en el siguiente notebook, entregamos las predicciones como probabilidades pues al decisión final del diagnóstico la debe dar el doctor después del análisis adecuado. 

<a href = "https://github.com/DaColcha/breast-cancer-prediction/blob/c56aeee0ca0f84168899cfe0996ec4c00b428802/notebooks/service-test.ipynb"> *Prueba del servicio* </a> 

Recordemos que la herramienta creada es un apoyo para tomar acciones preventivas, más no para tomar decisiones finales. 

El servicio puede ser probado utilizando la imagen de docker creada y publicada, clic aquí: 

<a href = "https://hub.docker.com/repository/docker/dacolcha/cancer_predictor/general"> <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" height=30px> </a>

*Importante: utilizar la última versión 3.0*

#### - Comando docker sugerido 
docker run -p 3000:3000 dacolcha/cancer_predictor:3.0

