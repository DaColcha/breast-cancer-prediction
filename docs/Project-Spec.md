# Predicción de cáncer de mama

- [Introducción](#contexto)
- [Objetivo](#objetivo)
- [Impacto](#impacto)
- [Alcance](#alcance)
- [Métricas de evaluación](#métricas)

## Introducción 
Se busca poder colaborar con clínicas que trabajen en la especialidad de oncología para poder mejorar su exactitud en la toma de decisiones en el momento de tratar tumores sospechosos. 

<hr>

### Objetivo 
Desarrollar un modelo de machine Learning que permita analizar las características de la imagen digitalizada de un tumor para poder determinar si este es maligno o benigno. 


### Impacto
En el ámbito de la medicina es crucial poder tomar decisiones correctas y existen detalles que como humanos solemos no tomar en cuenta ocasionando errores en estas decisiones. 
Con el modelo propuesto se busca menorar la carga de trabajo al doctor otorgando datos que sirvan como soporte en su toma de decisiones, asimismo, se espera detectar y tratar a tiempo tumores que resulten malignos. 

### Alcance
- **Recopilación** de datos de imágenes digitalizadas de tumores con etiquetas: maligno, benigno.
- **Exploración** de datos para entender relaciones.
- **Desarrollo** de un modelo de clasificación que utilice las características de las imágenes para predecir su impacto.
- **Validación** del modelo mediante el ajuste de hiperparámetros.
- **Despliegue** del modelo con una API que permita la integración en sistemas específicos. 

### Métricas
- **Recall:** proporción de los tumores malignos que fueron correctamente identificados. 
- **Tiempo de diagnóstico:** reducción en el tiempo necesario para obtener resultados del diagnóstico
- **Tratamientos efectivos:** tratamientos con resultados positivos iniciados a raíz de la detección temprana de un tumor maligno

### Stakeholders
Los stakeholders para este proyecto están en clínicas y hospitales que busquen mejorar sus métodos de diagnóstico en la especialidad de oncología que trabajen ya con biopsia por aspiración con aguja fina (FNA).
