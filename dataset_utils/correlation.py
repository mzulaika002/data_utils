################################################################################
# El script "correlation.py" contiene funciones para calcular                  #
# la correlación entre variables numéricas y la información mutua              #
# entre variables categóricas.                                                 #
# *****************************************************************************#
# Autora:   Muitze Zulaika Gallastegi                                          #
# Fecha:    02/06/2023                                                         #
################################################################################


# CARGAR LIBRERIAS -------------------------------------------------------------
import numpy as np
import pandas as pd
import math 

# CARGAR FUNCIONES DE OTROS FICHEROS -------------------------------------------
from dataset_utils.dataset import Dataset

# FUNCIONES --------------------------------------------------------------------
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
    data_types = data.dtypes
    values1 = dataset.get_attribute(variable1)
    values2 = dataset.get_attribute(variable2)

    try:
        # Comprobar el tipo de las variables
            if (data_types[variable1] == 'object' and data_types[variable2] != 'object') or (data_types[variable2] == 'object' and data_types[variable1] != 'object') :
                raise ValueError("Las variables deben ser numéricas o categóricas.")
            elif data_types[variable1] == 'object' and data_types[variable2] == 'object':
                # Calcular la información mutua para variables categóricas
                return calculate_categorical_mutual_information(variable1, variable2, data)
            else:
                # Calcular la correlación para variables numéricas
                return calculate_numeric_correlation(values1, values2)
    except (IndexError, ValueError) as e:
        print("Error:", str(e))
        return None


def calculate_correlation_matrix(dataset):
    """
    Calcula la correlación (información mutua para variables categóricas) por pares entre las variables del dataset.
    
    Parámetros:
        - dataset: Objeto Dataset que contiene los datos.

    Devoluciones:
    - correlation_matrix: DataFrame de pandas que contiene la matriz de correlación.
    """
    correlation_matrix = pd.DataFrame()
    data = dataset.get_data()
    data_types = data.dtypes
    attributes = dataset.get_attributes()

    for column1 in attributes:
        correlation_row = []
        for column2 in attributes:
            if column1 == column2:
                correlation_row.append(1.0)  # La correlación de una variable consigo misma es 1.0
            else:
                if (data_types[column1] == 'object' and data_types[column2] != 'object') or (data_types[column2] == 'object' and data_types[column1] != 'object') :
                    correlation=0.0
                elif data_types[column1] == 'object' and data_types[column2] == 'object':
                    # Variables categóricas, calculamos la información mutua
                    correlation = calculate_categorical_mutual_information(column1, column2, data)
                else:
                    # Variables numéricas, calculamos la correlación
                   correlation = calculate_numeric_correlation(data[column1], data[column2])                    
                correlation_row.append(correlation)
        correlation_matrix[column1] = correlation_row

    return correlation_matrix

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


def calculate_categorical_mutual_information(variable1, variable2, data):
    """
    Calcula la información mutua entre dos variables categóricas.

    Parámetros:
    - variable1: Nombre de la primera variable.
    - variable2: Nombre de la segunda variable.
    - data: DataFrame de pandas que contiene los datos.

    Devoluciones:
    - Información mutua entre las dos variables.
    """
    n = len(data)
    unique_values1 = set(data[variable1].unique())
    unique_values2 = set(data[variable2].unique())
    mutual_information = 0.0

    for value1 in unique_values1:
        p1 = len(data[data[variable1] == value1]) / n
        for value2 in unique_values2:
            p2 = len(data[data[variable2] == value2]) / n
            p12 = len(data[(data[variable1] == value1) & (data[variable2] == value2)]) / n
            if p12 > 0:
                mutual_information += p12 * math.log(p12 / (p1 * p2))

    return mutual_information