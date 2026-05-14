import numpy as np
from sklearn.decomposition import PCA

def angulo_primeras_componentes(df1, df2):
    """
    Calcula el ángulo (en radianes) entre las primeras componentes principales
    de dos DataFrames.
    """

    # 1. Ajustar PCA para df1
    pca1 = PCA(n_components=1)
    pca1.fit(df1)
    v1 = pca1.components_[0]

    # 2. Ajustar PCA para df2
    pca2 = PCA(n_components=1)
    pca2.fit(df2)
    v2 = pca2.components_[0]

    # 3. Calcular coseno del ángulo
    cos_angle = np.abs(np.dot(v1, v2)) / (np.linalg.norm(v1) * np.linalg.norm(v2))

    cos_angle = np.clip(cos_angle, -1.0, 1.0)

    # 4. Calcular ángulo
    angulo = np.arccos(cos_angle)

    return angulo