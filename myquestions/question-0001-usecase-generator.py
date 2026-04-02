import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_calcular_costo_total_por_material():
    materiales = ['cemento', 'arena', 'acero']
    n = random.randint(5, 15)

    df = pd.DataFrame({
        'material': np.random.choice(materiales, n),
        'costo_unitario': np.random.randint(10000, 50000, n),
        'cantidad': np.random.randint(1, 20, n)
    })

    input_data = {'df': df.copy()}

    df['costo_total'] = df['costo_unitario'] * df['cantidad']
    resultado = df.groupby('material')['costo_total'].sum().to_dict()

    return input_data, resultado