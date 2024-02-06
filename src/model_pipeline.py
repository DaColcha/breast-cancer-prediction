
def build_model():
    import mlflow
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    from sklearn.decomposition import PCA
    from sklearn.ensemble import RandomForestClassifier

    # Creamos el transformador de características
    feature_transformer = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("pca", PCA(n_components=15, random_state=40))
        ]
    )

    # Creamos el modelo
    model = RandomForestClassifier(n_estimators=100, max_depth=20, min_samples_split=11, min_impurity_decrease=0.0001)
    
    model_params = model.get_params()

    # Registrar los parámetros en MLflow
    mlflow.log_params({f"model__{key}": value for key, value in model_params.items()})

    # Creamos el pipeline
    train_model_pipeline = Pipeline(
        [
            ("feature_transformer", feature_transformer),
            ("model", model,)
        ]
    )

    return train_model_pipeline