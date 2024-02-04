import bentoml
import pandas as pd


class BreastCancerModelRunner(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("cpu",)
    SUPPORTS_CPU_MULTI_THREADING = True

    def __init__(self, model: bentoml.Model) -> None:
        self.classifier = bentoml.sklearn.load_model(model)

    @bentoml.Runnable.method()
    def is_cancer(self, input_data: pd.DataFrame) -> pd.DataFrame:
        #Redondeamos los valores de salida para tener la probabilidad de que sea cancer
        resultado = input_data[["id"]]
        predictions = self.classifier.predict(input_data)
        resultado["is_cancer"] = predictions[:, 1]
        return resultado
