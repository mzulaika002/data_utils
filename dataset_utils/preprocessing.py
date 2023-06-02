################################################################################
# El módulo `preprocessing` proporciona funciones para realizar tareas comunes #
# de preprocesamiento, como la normalización y estandarización de variables en #
# un conjunto de datos.                                                       #
# *****************************************************************************#
# Autora:   Muitze Zulaika Gallastegi                                          #
# Fecha:    02/06/2023                                                         #
################################################################################

# CARGAR LIBRERIAS -------------------------------------------------------------
import pandas as pd
import numpy as np

# CARGAR FUNCIONES DE OTROS FICHEROS -------------------------------------------
from dataset_utils.dataset import Dataset

# FUNCIONES --------------------------------------------------------------------
def normalize_variable(x):
    """
    Normaliza una variable numérica 'x' utilizando la normalización min-max.

    Parámetros:
    - x (list o Numpy array): Una lista o Numpy array de valores numéricos.

    Devoluciones:
    - x_normalized (Numpy array): Una array con los valores normalizados de 'x'.
    """
    try:
        if isinstance(x, pd.Series):
            x = x.values
        if not isinstance(x, (list, np.ndarray)):
            raise TypeError("El argumento 'x' debe ser una lista o un array numpy.")
        
        if len(x) == 0:
            raise ValueError("La lista 'x' no puede estar vacía.")

        unique_values = np.unique(x)
        if np.array_equal(unique_values, [0, 1]):
            return x  # return el mismo valor        
        
        min_val = np.min(x)
        max_val = np.max(x)
        
        x_normalized = [(val - min_val) / (max_val - min_val) for val in x]
        
        return x_normalized
    except ValueError as e:
        print("Error:", e)
        return None

def standardize_variable(x):
    """
    Estandariza una variable numérica 'x' utilizando la estandarización z-score.

    Parámetros:
    - x (list o Numpy array): Una lista o Numpy array de valores numéricos.

    Devoluciones:
    - x_standardized (Numpy array): Una array con los valores estandarizados de 'x'.
    """
    try:
        if isinstance(x, pd.Series):
            x = x.values
        if not isinstance(x, (list, np.ndarray)):
            raise TypeError("El argumento 'x' debe ser una lista o un arreglo numpy.")
        
        if len(x) == 0:
            raise ValueError("La lista 'x' no puede estar vacía.")
    
        unique_values = np.unique(x)
        if np.array_equal(unique_values, [0, 1]):
            return x

        mean_val = sum(x) / len(x)
        std_dev = (sum((val - mean_val) ** 2 for val in x) / len(x)) ** 0.5
        
        x_standardized = [(val - mean_val) / std_dev for val in x]
        
        return x_standardized

    except ValueError as e:
        print("Error:", e)
        return None

def normalize_dataset(dataset):
    """
    Realiza la normalización de todas las variables numéricas en un dataset.

    Parámetros:
    - dataset (Dataset): Un dataset.

    Devoluciones:
    - normalized_dataset (Dataset): Un nuevo dataset con las variables numéricas normalizadas.
    """
    if not isinstance(dataset, (Dataset, pd.DataFrame)):
        raise TypeError("El argumento 'dataset' debe ser un Dataset  de pandas.")
    
    normalized_dataset = dataset.copy()
    
    for attribute in normalized_dataset.get_attributes():
        values = normalized_dataset.get_attribute(attribute)
        if np.issubdtype(values.dtype, np.number):
            normalized_values = normalize_variable(values)
            normalized_dataset.set_attribute(attribute, normalized_values)
    
    return normalized_dataset

def standardize_dataset(dataset):
    """
    Realiza la estandarización de todas las variables numéricas en un dataset.

    Parámetros:
    - dataset (Dataset): Un dataset.

    Devoluciones:
    - standardized_dataset (Dataset): Un nuevo dataset con las variables numéricas estandarizadas.
    """
    if not isinstance(dataset, (Dataset, pd.DataFrame)):
        raise TypeError("El argumento 'dataset' debe ser un Dataset  de pandas.")
    
    standardized_dataset = dataset.copy()
    
    for attribute in standardized_dataset.get_attributes():
        values = standardized_dataset.get_attribute(attribute)
        if np.issubdtype(values.dtype, np.number):
            standardized_values = standardize_variable(values)
            standardized_dataset.set_attribute(attribute, standardized_values)
    
    return standardized_dataset

















