
def normalize_variable(x):
    """
    Normaliza una variable numérica 'x' utilizando la normalización min-max.

    Parámetros:
    - x (list): Una lista de valores numéricos.

    Devoluciones:
    - x_normalized (list): Una lista con los valores normalizados de 'x'.
    """
    if not isinstance(x, list):
        raise TypeError("El argumento 'x' debe ser una lista.")
    
    if len(x) == 0:
        raise ValueError("La lista 'x' no puede estar vacía.")
    
    min_val = min(x)
    max_val = max(x)
    
    x_normalized = [(val - min_val) / (max_val - min_val) for val in x]
    
    return x_normalized


def standardize_variable(x):
    """
    Estandariza una variable numérica 'x' utilizando la estandarización z-score.

    Parámetros:
    - x (list): Una lista de valores numéricos.

    Devoluciones:
    - x_standardized (list): Una lista con los valores estandarizados de 'x'.
    """
    if not isinstance(x, list):
        raise TypeError("El argumento 'x' debe ser una lista.")
    
    if len(x) == 0:
        raise ValueError("La lista 'x' no puede estar vacía.")
    
    mean_val = sum(x) / len(x)
    std_dev = (sum((val - mean_val) ** 2 for val in x) / len(x)) ** 0.5
    
    x_standardized = [(val - mean_val) / std_dev for val in x]
    
    return x_standardized


def normalize_dataset(dataset):
    """
    Realiza la normalización de todas las variables numéricas en un dataset.

    Parámetros:
    - dataset (list): Un dataset representado como una lista de listas, donde cada lista interna representa
                      una columna o atributo del dataset.

    Devoluciones:
    - normalized_dataset (list): Un nuevo dataset con las variables numéricas normalizadas.
    """
    if not isinstance(dataset, list):
        raise TypeError("El argumento 'dataset' debe ser una lista.")
    
    if len(dataset) == 0:
        raise ValueError("El dataset no puede estar vacío.")
    
    normalized_dataset = []
    
    for attribute in dataset:
        if not isinstance(attribute, list):
            raise TypeError("Cada atributo en el dataset debe ser una lista.")
        
        if len(attribute) == 0:
            raise ValueError("Los atributos en el dataset no pueden estar vacíos.")
        
        if all(isinstance(val, (int, float)) for val in attribute):
            normalized_attribute = normalize_variable(attribute)
        else:
            normalized_attribute = attribute
        
        normalized_dataset.append(normalized_attribute)
    
    return normalized_dataset


def standardize_dataset(dataset):
    """
    Realiza la estandarización de todas las variables numéricas en un dataset.

    Parámetros:
    - dataset (list): Un dataset representado como una lista de listas, donde cada lista interna representa
                      una columna o atributo del dataset.

    Devoluciones:
    - standardized_dataset (list): Un nuevo dataset con las variables numéricas estandarizadas.
    """
    if not isinstance(dataset, list):
        raise TypeError("El argumento 'dataset' debe ser una lista.")
    
    if len(dataset) == 0:
        raise ValueError("El dataset no puede estar vacío.")
    
    standardized_dataset = []
    
    for attribute in dataset:
        if not isinstance(attribute, list):
            raise TypeError("Cada atributo en el dataset debe ser una lista.")
        
        if len(attribute) == 0:
            raise ValueError("Los atributos en el dataset no pueden estar vacíos.")
        
        if all(isinstance(val, (int, float)) for val in attribute):
            standardized_attribute = standardize_variable(attribute)
        else:
            standardized_attribute = attribute
        
        standardized_dataset.append(standardized_attribute)
    
    return standardized_dataset

import pandas as pd

def normalize_dataframe(df):
    """
    Obtiene un nuevo DataFrame con los valores normalizados para cada columna numérica del DataFrame dado.

    Parámetros:
    - df (pandas.DataFrame): Un DataFrame con valores numéricos.

    Devoluciones:
    - normalized_df (pandas.DataFrame): Un nuevo DataFrame con los valores normalizados para cada columna numérica.
    """
    normalized_data = normalize_dataset(df.values.T.tolist())
    normalized_df = pd.DataFrame(normalized_data).T
    normalized_df.columns = df.columns
    return normalized_df


def standardize_dataframe(df):
    """
    Obtiene un nuevo DataFrame con los valores estandarizados para cada columna numérica del DataFrame dado.

    Parámetros:
    - df (pandas.DataFrame): Un DataFrame con valores numéricos.

    Devoluciones:
    - standardized_df (pandas.DataFrame): Un nuevo DataFrame con los valores estandarizados para cada columna numérica.
    """
    standardized_data = standardize_dataset(df.values.T.tolist())
    standardized_df = pd.DataFrame(standardized_data).T
    standardized_df.columns = df.columns
    return standardized_df




















