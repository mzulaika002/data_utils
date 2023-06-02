import math
import numpy as np

def calculate_correlation(dataset, variable1, variable2):
    """
    Calcula la correlación entre dos variables en un conjunto de datos.

    Parámetros:
    - dataset: Objeto Dataset que contiene los datos.
    - variable1: Nombre de la primera variable.
    - variable2: Nombre de la segunda variable.

    Devoluciones:
    - Coeficiente de correlación entre las dos variables.
    """
    data = dataset.get_data()
    values1 = dataset.get_attribute(variable1)
    values2 = dataset.get_attribute(variable2)

    try:
        # Comprobar el tipo de las variables
        if isinstance(values1[0], (int, float,np.int64)) and isinstance(values2[0], (int, float,np.int64)):
            # Calcular la correlación para variables numéricas
            return calculate_numeric_correlation(values1, values2)
        elif isinstance(values1[0], str) and isinstance(values2[0], str):
            # Calcular la información mutua para variables categóricas
            return calculate_categorical_mutual_information(values1, values2, data)
        else:
            raise ValueError("Las variables deben ser numéricas o categóricas.")
    except (IndexError, ValueError) as e:
        print("Error:", str(e))
        return None

def calculate_numeric_correlation(values1, values2):
    """
    Calcula el coeficiente de correlación entre dos variables numéricas.

    Parámetros:
    - values1: Valores de la primera variable.
    - values2: Valores de la segunda variable.

    Devoluciones:
    - Coeficiente de correlación entre las dos variables.
    """
    n = len(values1)
    mean1 = sum(values1) / n
    mean2 = sum(values2) / n
    cov = sum((x - mean1) * (y - mean2) for x, y in zip(values1, values2)) / n
    std1 = math.sqrt(sum((x - mean1) ** 2 for x in values1) / n)
    std2 = math.sqrt(sum((x - mean2) ** 2 for x in values2) / n)
    correlation = cov / (std1 * std2)
    return correlation

def calculate_categorical_mutual_information(values1, values2, data):
    """
    Calcula la información mutua entre dos variables categóricas.

    Parámetros:
    - values1: Valores de la primera variable.
    - values2: Valores de la segunda variable.
    - data: DataFrame de pandas que contiene los datos.

    Devoluciones:
    - Información mutua entre las dos variables.
    """
    n = len(values1)
    unique_values1 = set(values1)
    unique_values2 = set(values2)
    mutual_information = 0.0

    for value1 in unique_values1:
        p1 = len(data[data[values1] == value1]) / n
        for value2 in unique_values2:
            p2 = len(data[data[values2] == value2]) / n
            p12 = len(data[(data[values1] == value1) & (data[values2] == value2)]) / n
            if p12 > 0:
                mutual_information += p12 * math.log(p12 / (p1 * p2))

    return mutual_information
