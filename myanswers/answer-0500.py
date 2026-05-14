import pandas as pd
import numpy as np
from sklearn.feature_selection import VarianceThreshold

def eliminar_baja_varianza(df, umbral):
    
    # 1. Seleccionar solo columnas numéricas
    df_numerico = df.select_dtypes(include=[np.number]).copy()

    # 2. Aplicar VarianceThreshold
    selector = VarianceThreshold(threshold=umbral)
    X_sel = selector.fit_transform(df_numerico)

    # 3. Obtener columnas seleccionadas
    columnas_seleccionadas = df_numerico.columns[selector.get_support()]

    # 4. Reconstruir DataFrame con índice original
    df_resultado = pd.DataFrame(
        X_sel,
        columns=columnas_seleccionadas,
        index=df.index
    )

    return df_resultado