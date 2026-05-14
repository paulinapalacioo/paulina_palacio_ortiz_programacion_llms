import numpy as np

def imputar_temperatura(df, col):
    """
    Imputa valores NaN usando el promedio entre el valor válido anterior
    y el siguiente.
    """

    # Trabajar sobre copia
    df_out = df.copy()
    y = df_out[col].to_numpy().copy()

    for i in range(len(y)):
        if np.isnan(y[i]):

            # buscar anterior válido
            for j in range(i-1, -1, -1):
                if not np.isnan(y[j]):
                    ant = y[j]
                    break

            # buscar siguiente válido
            for j in range(i+1, len(y)):
                if not np.isnan(y[j]):
                    sig = y[j]
                    break

            # promedio 
            y[i] = round((ant + sig) / 2, 1)

    df_out[col] = y

    return df_out