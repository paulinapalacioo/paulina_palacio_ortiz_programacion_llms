import numpy as np
import pandas as pd

def codificar_ciclo_temporal(df, col_hora):
    
    df = df.copy()
    
    # extraer columna
    horas = df[col_hora]
    
    # transformación cíclica
    df["hora_sin"] = np.sin(2 * np.pi * horas / 24)
    df["hora_cos"] = np.cos(2 * np.pi * horas / 24)
    
    # eliminar columna original
    df = df.drop(columns=[col_hora])
    
    return df