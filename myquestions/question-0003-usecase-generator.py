import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import random

def generar_caso_de_uso_escalar_datos_concreto():
    n = random.randint(5, 15)

    df = pd.DataFrame({
        'humedad': np.random.uniform(2, 10, n),
        'temperatura': np.random.uniform(15, 35, n),
        'volumen': np.random.uniform(50, 500, n)
    })

    input_data = {'df': df.copy()}

    scaler_std = StandardScaler()
    data_std = scaler_std.fit_transform(df)

    scaler_minmax = MinMaxScaler()
    resultado = scaler_minmax.fit_transform(data_std)

    return input_data, resultado
