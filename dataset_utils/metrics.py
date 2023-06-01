################################################################################
# #
# #
##
# *****************************************************************************#
# Autora:   Muitze Zulaika Gallastegi                                          #
# Fecha:    02/06/2023                                                         #
################################################################################


# CARGAR LIBRERIAS -------------------------------------------------------------
from math import log2
import numpy as np
import pandas as pd

# CARGAR FUNCIONES DE OTROS FICHEROS -------------------------------------------
from dataset_utils.dataset import Dataset

# FUNCIONES ENTROPIA -----------------------------------------------------------
def entropy(x):
    """
    Calcular la entropía de una variable discreta.
    
    Parámetros:
     - x (lista): una lista de valores discretos
    
    Devoluciones:
     - ent (float): la entropía de x
    """
    
    # Verificar si la lista está vacía
    if len(x) == 0:
        raise ValueError("La lista 'x' no puede estar vacía.")
    
    # Calcular la probabilidad de cada valor
    values, counts = np.unique(x, return_counts=True)
    prob = counts / len(x)

    # Calcular la entropía
    ent = -sum(p * log2(p) for p in prob)
    
    return round(ent, 3)

def get_entropies(dataframe):
    """
    Obtener el vector que contiene la entropía asociada a cada columna en el dataframe de valores discretos.
    
    Parámetros:
     - dataframe (pandas DataFrame): El dataframe de valores discretos.
    
    Devoluciones:
     - entropies (pandas Series): Una serie que contiene la entropía asociada a cada columna en el dataframe.
    """
    
    # Verificar si el dataframe está vacío
    if dataframe.empty:
        raise ValueError("El dataframe no puede estar vacío.")
    
    entropies = []
    
    # Iterar sobre cada columna en el dataframe
    for column in dataframe.columns:
        entropy_value = entropy(dataframe[column])
        entropies.append(entropy_value)
    
    # Crear una serie con los valores de entropía y los nombres de las columnas
    entropies = pd.Series(entropies, index=dataframe.columns)
    
    return entropies

# FUNCIONES VARIANZA -----------------------------------------------------------
def get_variances(matrix):
    """
    Calcular la varianza de cada columna en la matriz de entrada.

     Parámetros:
      - matriz (numpy array): la matriz de entrada.

     Devoluciones:
      - varianzas (numpy array): una matriz de varianzas para cada columna en la matriz de entrada.
     """  

    matrix = np.array(matrix)
    variances = []

    for i in range(matrix.shape[1]):
        # Obtener la columna actual
        column = matrix[:, i]
    
        # Calcular la media de la columna
        mean = np.mean(column)
        
        # Calcular la varianza
        variance = sum((x - mean)**2 for x in column) / (column.size-1)
        
        # Añadir la varianza a la lista de varianzas
        variances.append(variance)

    # Convertir la lista de varianzas en un array de numpy y devolverlo
    return np.array(variances)

def get_variances_pd(df):
    """
    Calcular la varianza de cada columna en el dataframe de entrada.

    Parámetros:
     - df (pandas DataFrame): El dataframe de entrada.

    Devoluciones:
     - variances (pandas Series): Una Serie de varianzas para cada columna en el dataframe de entrada.
    """

    # Inizializar lista de varianzas
    variances = []

    for column in df.columns:
        # Calcular la media de la columna
        mean = df[column].mean()

        # Calcular la varianza sumando el cuadrado de la diferencia entre cada valor y la media
        variance = sum((x - mean)**2 for x in df[column]) / (df[column].count()-1)

        # Añadir la varianza a la lista de varianzas
        variances.append(variance)
    return variances


def get_column_variances(data):
    """
    Calcular las varianzas de las columnas en los datos de entrada.

    Parámetros:
     - data (numpy array, list o pandas DataFrame): Los datos de entrada.

    Devoluciones:
     - variances (numpy array o pandas Series): Un array o Serie de varianzas para cada columna en los datos de entrada.
    """
  
    if isinstance(data, np.ndarray) or isinstance(data, list):
        # Si los datos son un array de NumPy o una lista, llamar a la función get_variances
        return get_variances(data)
    elif isinstance(data, pd.DataFrame):
        # Si los datos son un dataframe de Pandas, llamar a la función get_variances_pd
        return get_variances_pd(data)
    else:
        # Si los datos no son ninguno de los tipos aceptados, lanzar una excepción de TypeError
        raise TypeError("Input must be a Pandas dataframe, a NumPy array, or a list")


# FUNCIONES AUC ----------------------------------------------------------------
def ROC_AUC(df):
    """
    Calcula los puntos de la curva ROC y el área bajo la curva ROC (AUC) para un dataframe dado.

    Parámetros:
     - df (pandas DataFrame): El dataframe que contiene dos columnas, la primera es un vector numérico y la segunda es un vector lógico.

    Devoluciones:
     - TPR_list (lista): Una lista que contiene los valores del True Positive Rate (TPR) para cada posible valor de corte.
     - FPR_list (lista): Una lista que contiene los valores del False Positive Rate (FPR) para cada posible valor de corte.
     - cut_offs (lista): Una lista que contiene los valores de corte correspondientes a cada punto de la curva ROC.
     - AUC (float): El valor del área bajo la curva ROC (AUC).
    """

    # Verificar si el dataframe tiene al menos dos columnas
    if df.shape[1] < 2:
        raise ValueError("El dataframe debe tener al menos dos columnas.")

    # Verificar si el primer vector es numérico y el segundo vector es lógico
    if not np.issubdtype(df[df.columns[0]].dtype, np.number) or not np.issubdtype(df[df.columns[1]].dtype, np.bool_):
        raise ValueError("La primera columna debe ser numérica y la segunda columna debe ser lógica (booleana).")

    # Verificar si el dataframe no está vacío
    if df.empty:
        raise ValueError("El dataframe no puede estar vacío.")

    # Ordenar las filas por la primera columna (valores de la variable)
    df = df.sort_values(by=[df.columns[0]])

    # Inicializar listas para TPR, FPR y puntos de corte
    TPR_list = []
    FPR_list = []
    cut_offs = []

    # Iterar sobre cada posible valor de corte
    for i in range(len(df)):

        # Definir los valores predichos como Verdadero (True) por encima del valor de corte, Falso (False) en caso contrario
        pred = df[df.columns[0]] > df[df.columns[0]].iloc[i]

        # Calcular TP, TN, FP, FN
        TP = sum((pred == True) & (df[df.columns[1]] == True))
        TN = sum((pred == False) & (df[df.columns[1]] == False))
        FP = sum((pred == True) & (df[df.columns[1]] == False))
        FN = sum((pred == False) & (df[df.columns[1]] == True))

        # Agregar TPR, FPR y punto de corte a las listas correspondientes
        TPR_list.append(TP / (TP + FN))
        FPR_list.append(FP / (FP + TN))
        cut_offs.append(df[df.columns[0]].iloc[i])

    # Calcular el AUC
    AUC = 0
    for i in range(len(TPR_list) - 1):
        delta_fpr = FPR_list[i+1] - FPR_list[i]
        avg_tpr = (TPR_list[i+1] + TPR_list[i]) / 2
        AUC += delta_fpr * avg_tpr

    return TPR_list, FPR_list, cut_offs, AUC



