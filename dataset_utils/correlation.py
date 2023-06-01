

import numpy as np
from math import log2

def pearson_correlation(x, y):
    """
    Calcula la correlación de Pearson entre dos variables numéricas.

    Parámetros:
    - x (list): Una lista de valores numéricos para la variable X.
    - y (list): Una lista de valores numéricos para la variable Y.

    Devoluciones:
    - correlation (float): El valor de la correlación de Pearson entre X e Y.
    """
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator = np.sqrt(sum((xi - mean_x) ** 2 for xi in x)) * np.sqrt(sum((yi - mean_y) ** 2 for yi in y))
    correlation = numerator / denominator if denominator != 0 else 0
    return correlation

def mutual_information(x, y):
    """
    Calcula la información mutua entre dos variables categóricas.

    Parámetros:
    - x (list): Una lista de valores categóricos para la variable X.
    - y (list): Una lista de valores categóricos para la variable Y.

    Devoluciones:
    - mutual_info (float): El valor de la información mutua entre X e Y.
    """
    joint_prob = {}
    x_prob = {}
    y_prob = {}
    n = len(x)

    for xi, yi in zip(x, y):
        joint_prob[(xi, yi)] = joint_prob.get((xi, yi), 0) + 1
        x_prob[xi] = x_prob.get(xi, 0) + 1
        y_prob[yi] = y_prob.get(yi, 0) + 1

    mutual_info = 0.0
    for xi, yi in joint_prob:
        prob_xy = joint_prob[(xi, yi)] / n
        prob_x = x_prob[xi] / n
        prob_y = y_prob[yi] / n
        mutual_info += prob_xy * log2(prob_xy / (prob_x * prob_y))

    return mutual_info

def calculate_correlation(dataset):
    """
    Calcula la correlación (o información mutua para variables categóricas) por pares entre variables de un dataset.

    Parámetros:
    - dataset (list): Un dataset representado como una lista de listas, donde cada lista interna representa una columna o atributo del dataset.

    Devoluciones:
    - correlation_matrix (np.ndarray): Una matriz cuadrada que contiene las correlaciones (o información mutua) por pares entre las variables del dataset.
    """
    num_attributes = len(dataset[0])
    correlation_matrix = np.zeros((num_attributes, num_attributes))

    for i in range(num_attributes):
        for j in range(num_attributes):
            attribute_i = dataset[i]
            attribute_j = dataset[j]

            if isinstance(attribute_i[0], (int, float)) and isinstance(attribute_j[0], (int, float)):
                # Variables numéricas: calcular correlación de Pearson
                correlation = pearson_correlation(attribute_i, attribute_j)
            elif isinstance(attribute_i[0], str) and isinstance(attribute_j[0], str):
                # Variables categóricas: calcular información mutua
                correlation = mutual_information(attribute_i, attribute_j)
            else:
                raise ValueError("Tipos de variables incompatibles. Las variables deben ser numéricas o categóricas.")

            correlation_matrix[i, j] = correlation

    return correlation_matrix


