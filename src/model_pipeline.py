def build_model():
    import mlflow
    import tensorflow as tf
    from sklearn.preprocessing import StandardScaler
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    from sklearn.decomposition import PCA

    # Eliminamos información que no aporta al aprendizaje
    data = data.drop(['id'], axis=1)

    # Escalamos los datos
    scaler = ColumnTransformer([("scaler", StandardScaler(),slice(None))])

    # Reducimos la dimensionalidad
    pca_transformer = ColumnTransformer([("pca", PCA(n_components=2, random_state=40),slice(None))])

    feature_transformer = Pipeline(
        [
            ("scaler", scaler),
            ("pca", pca_transformer)
        ]
    )

    # Creamos el modelo
    model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(15, activation='relu', input_shape=(15,)),
    tf.keras.layers.Dense(15, activation='relu'),
    tf.keras.layers.Dense(15, activation='relu'),
    tf.keras.layers.Dense(15, activation='relu'),
    tf.keras.layers.Dense(15, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(
        optimizer=tf.optimizers.SGD(learning_rate=0.0032),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    model_params = model.get_config()

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