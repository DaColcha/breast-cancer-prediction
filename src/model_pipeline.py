def build_model():
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA

    # Escalamos los datos
    scaler = StandardScaler()
    columns = 