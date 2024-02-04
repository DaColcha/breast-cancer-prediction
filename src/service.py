import bentoml
from bentoml.io import PandasDataFrame

from runner import BreastCancerModelRunner

MODEL_TAG = "breast-cancer-predictor"


breast_cancer_model = bentoml.sklearn.get(MODEL_TAG)

breast_cancer_model_runner = bentoml.Runner(
    #Le enviamos la clase y asignamos el parámetro de inicialización al modelo que se carga
    BreastCancerModelRunner,
    models=[breast_cancer_model],
    runnable_init_params={"model": breast_cancer_model},
)

breast_cancer_predictor_service = bentoml.Service(
    "breast_cancer_predictor_service", 
    runners=[breast_cancer_model_runner]
)


@breast_cancer_predictor_service.api(input=PandasDataFrame(), output=PandasDataFrame())
def predict(input_df):
    return breast_cancer_model_runner.is_cancer.run(input_df)