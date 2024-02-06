import bentoml
import pandas as pd


class BreastCancerModelRunner(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("cpu",)
    SUPPORTS_CPU_MULTI_THREADING = True

    def __init__(self, model: bentoml.Model) -> None:
        self.classifier = bentoml.sklearn.load_model(model)

    @bentoml.Runnable.method()
    def is_cancer(self, input_data: pd.DataFrame) -> pd.DataFrame:
        resultado = input_data[["id"]]
        data_to_predict = input_data.drop(["id"], axis=1)
        predictions = self.classifier.predict_proba(data_to_predict)
        is_cancer = predictions[:,1] 
        resultado["is_cancer"] = is_cancer
        return resultado
