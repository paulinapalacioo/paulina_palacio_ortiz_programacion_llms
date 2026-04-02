import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import random

def generar_caso_de_uso_predecir_resistencia_concreto():
    n = random.randint(10, 20)

    df = pd.DataFrame({
        'cemento': np.random.uniform(200, 500, n),
        'agua': np.random.uniform(100, 250, n),
        'aditivos': np.random.uniform(0, 50, n),
        'resistencia_3d': np.random.uniform(10, 25, n),
        'resistencia_7d': np.random.uniform(20, 40, n)
    })

    # Target (resistencia a 28 días)
    df['resistencia_28d'] = (
        df['resistencia_7d'] * 1.3 +
        np.random.uniform(5, 10, n)
    )

    input_data = {
        'df': df.copy(),
        'target_col': 'resistencia_28d'
    }

    X = df.drop(columns=[input_data['target_col']])
    y = df[input_data['target_col']]

    model = RandomForestRegressor()
    model.fit(X, y)

    return input_data, model
