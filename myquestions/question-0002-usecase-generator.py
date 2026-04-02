import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_completar_monitoreo_asentamiento():
    """
    Genera un caso de uso aleatorio para la función
    completar_monitoreo_asentamiento(df)
    respetando comportamiento físico del asentamiento (no decreciente)
    """

    # 🔹 1. Generar asentamiento acumulado creciente
    n = random.randint(5, 10)
    valores = np.cumsum(np.random.uniform(0.5, 2.0, n))

    # 🔹 2. Introducir errores
    valores_con_errores = valores.copy()
    for i in range(1, n - 1):
        if random.random() < 0.3:
            valores_con_errores[i] = np.nan if random.random() < 0.5 else 0

    df = pd.DataFrame({'asentamiento': valores_con_errores})

    # 🔹 3. INPUT
    input_data = {'df': df.copy()}

    # 🔹 4. OUTPUT esperado (lógica física correcta)
    valores_corregidos = valores_con_errores.copy()

    for i in range(len(valores_corregidos)):

        if np.isnan(valores_corregidos[i]) or valores_corregidos[i] == 0:

            prev = None
            next_ = None

            # Buscar anterior válido
            for j in range(i - 1, -1, -1):
                if not (np.isnan(valores_corregidos[j]) or valores_corregidos[j] == 0):
                    prev = valores_corregidos[j]
                    break

            # Buscar siguiente válido
            for j in range(i + 1, len(valores_corregidos)):
                if not (np.isnan(valores_corregidos[j]) or valores_corregidos[j] == 0):
                    next_ = valores_corregidos[j]
                    break

            # 🔹 CASOS
            if prev is not None and next_ is not None:
                # Interpolación
                valores_corregidos[i] = (prev + next_) / 2

            elif prev is not None:
                # Mantener tendencia (no decrecer)
                valores_corregidos[i] = prev

            elif next_ is not None:
                valores_corregidos[i] = next_

    return input_data, np.array(valores_corregidos)