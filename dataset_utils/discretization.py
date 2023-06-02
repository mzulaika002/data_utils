################################################################################
# Este script "discretization.py" proporcion funciones para realizar la        #
# discretización de atributos numéricos en un conjunto de datos. Proporciona   #
# dos métodos de discretización: Equal Width (ancho igual) y Equal Frequency   #
# (frecuencia igual).                                                          #
# *****************************************************************************#
# Autora:   Muitze Zulaika Gallastegi                                          #
# Fecha:    02/06/2023                                                         #
################################################################################

# CARGAR FUNCIONES DE OTROS FICHEROS -------------------------------------------
from dataset_utils.dataset import Dataset

# CARGAR LIBRERIAS -------------------------------------------------------------
import statistics
import numpy as np
import pandas as pd

# FUNCIONES DE DISCRETIZACIÓN --------------------------------------------------
def discretizeEW(x, num_bins):
  """
  Discretizar un atributo de entrada `x` en `num_bins` intervalos usando la discretización Equal Width.

  Parámetros:
   -x (lista o array): una lista o array de valores numéricos
   - num_bins (int): el número de intervalos para discretizar en `x` 

  Devoluciones:
    - x_discretitizado: lista de valores discretizados, representados como string en la forma "I<n>", 
                        donde <n> es el índice de intervalo.
    - Lista de puntos:  lista de puntos de corte entre intervalos.   
  """
  if num_bins <= 0:
    raise ValueError("El número de intervalos debe ser mayor que cero.")
  
  if isinstance(x, list):
    x = np.array(x)
  elif isinstance(x, pd.Series):
    x = x.values
  elif not isinstance(x, np.ndarray):
    raise ValueError("El argumento 'x' debe ser una lista o un array NumPy.")

  if len(x) == 0:
    raise ValueError("La lista de valores está vacía.")

  if not np.issubdtype(x.dtype, np.number):
    raise ValueError("Los valores del atributo deben ser numéricos.")

  # Determinar los valores máximo y mínimo de la lista
  max_val = np.max(x)
  min_val = np.min(x)

  # Calcular el tamaño de cada intervalo
  bin_size = (max_val - min_val) / num_bins

  # Cree una lista de los puntos de corte para cada intervalo
  cut_points = [min_val + (i * bin_size) for i in range(1,num_bins)]

  # Crear una lista vacía para almacenar los valores agrupados
  x_discretized = []

  # Iterar sobre los valores en la lista y asignarlos a un intervalo
  for val in x:
    for i, cut_point in enumerate(cut_points, start=1):
      if val < cut_point:
        x_discretized.append(f'I{i}')
        break
    else:
      x_discretized.append(f'I{num_bins}')

  return x_discretized, cut_points

def discretizeEF(x, num_bins):
    """
    Discretiza un atributo de entrada `x` en `num_bins` intervalos usando la discretización Equal Frequency.

    Parámetros:
    - x (list): Una lista de valores numéricos.
    - num_bins (int): El número de intervalos para dividir en `x` 

    Devoluciones:
    - x_discretitizado (list): lista de valores discretizados, representados como string en la forma "I<n>", 
                        donde <n> es el índice de intervalo.
    - Lista de puntos (list):  lista de puntos de corte entre intervalos.    
    """
    if num_bins <= 0:
        raise ValueError("El número de intervalos debe ser mayor que cero.")
    if num_bins >= len(x):
        raise ValueError("El número de bins debe ser menor al número de valores en el atributo.")
    if isinstance(x, list):
        x = np.array(x)
    elif isinstance(x, pd.Series):
        x = x.values
    elif not isinstance(x, np.ndarray):
        raise ValueError("El argumento 'x' debe ser una lista o un array NumPy.")
    if len(x) == 0:
        raise ValueError("La lista de valores está vacía.")
    if not np.issubdtype(x.dtype, np.number):
     raise ValueError("Los valores del atributo deben ser numéricos.")

    # Ordenar x en orden ascendente
    x_sorted = sorted(x)

    # Calcular el número de elementos por intervalo
    elements_per_interval = len(x) / num_bins

    # Crear lista de puntos de corte
    cut_points = [x_sorted[int(i * elements_per_interval) - 1] for i in range(1, num_bins)]

    # Inicializar lista para valores discretizados
    x_discretized = []

    # Iterar sobre elementos en x y encontrar el intervalo al que pertenecen
    for element in x:
        for i, cut_point in enumerate(cut_points, start=1):
            if element <= cut_point:
                x_discretized.append(f"I{i}")
                break
        else:
            x_discretized.append(f"I{num_bins}")

    return x_discretized, cut_points

def discretize(x, cut_points):
    """
    Discretiza los valores de entrada `x` en los intervalos definidos por los puntos de corte.

    Parámetros:
    - x (list o array): Una lista de valores numéricos a discretizar.
    - cut_points (list o array): Una lista de puntos de corte que definen los intervalos.

    Devoluciones:
    - x_discretized (list): Una lista de valores discretizados, representados como string en la forma "I<n>",
                            donde <n> es el índice de intervalo.
    - cut_points (list): La lista de puntos de corte original, sin cambios.
    """

    # Validar los argumentos de entrada
    if isinstance(x, list):
        x = np.array(x)
    elif isinstance(x, pd.Series):
        x = x.values
    elif not isinstance(x, np.ndarray):
        raise ValueError("El argumento 'x' debe ser una lista o un array NumPy.")
    if isinstance(cut_points, list):
        cut_points = np.array(cut_points)
    elif isinstance(cut_points, pd.Series):
        cut_points = cut_points.values
    elif not isinstance(cut_points, np.ndarray):
        raise ValueError("El argumento 'cut_points' debe ser una lista o un array NumPy.")
    if len(x) == 0:
        raise ValueError("El argumento 'x' está vacía.")
    if len(cut_points) == 0:
        raise ValueError("El argumento 'cut_points' está vacía.")
    if not np.issubdtype(x.dtype, np.number):
        raise ValueError("Los valores del atributo 'x' deben ser numéricos.")
    if not np.issubdtype(cut_points.dtype, np.number):
         raise ValueError("Los valores del atributo 'cut_points' deben ser numéricos.")


    # Verificar que los puntos de corte estén en orden ascendente
    if cut_points != sorted(cut_points):
        raise ValueError("Los puntos de corte deben estar en orden ascendente.")

    # Inicializar lista para valores discretizados
    x_discretized = []

    # Iterar sobre los elementos en `x` y encontrar el intervalo al que pertenecen
    for element in x:
        for i, cut_point in enumerate(cut_points):
            if element <= cut_point:
                x_discretized.append(f"I{i+1}")
                break
        else:
            x_discretized.append(f"I{len(cut_points)+1}")

    return x_discretized, cut_points

def discretize_attribute(attribute, num_bins, method):
    """
    Discretiza un atributo utilizando el método especificado.

    Parámetros:
    - atrinuto (list o array): Un atributo representado como una lista.
    - num_bins (int o array): El número de intervalos para discretizar cada atributo del dataset.
    - method (str): El método de discretización a utilizar. Puede ser 'equal_width' (ancho igual) o 'equal_frequency'
                    (frecuencia igual).

    Devoluciones:
    - discretized_attribute (list): Un nuevo atributo con los atributos discretizados. Una lista
                                  de valores discretizados, representados como string en la forma "I<n>",
                                  donde <n> es el índice de intervalo.
    """
    if method != 'equal_width' and method != 'equal_frequency':
        raise ValueError("Método de discretización inválido. Use 'equal_width' o 'equal_frequency'.")

    if method == 'equal_width':
        x_discretized, cut_points = discretizeEW(attribute, num_bins)
    elif method == 'equal_frequency':
        x_discretized, cut_points = discretizeEF(attribute, num_bins)

    return x_discretized, cut_points

# FUNCIONES DE SUAVIZAR --------------------------------------------------------
def smooth_by_bin_mean(x, num_bins):
    """
    Suaviza los valores en cada intervalo reemplazándolos con el valor medio del intervalo.

    Parámetros:
    - x (lista o array): Una lista de valores numéricos.
    - num_bins (int): El número de intervalos.

    Retorna:
    - x_suavizado (lista): Una lista de valores suavizados.
    """
    if num_bins <= 0:
        raise ValueError("El número de intervalos debe ser mayor que cero.")
    if num_bins >= len(x):
        raise ValueError("El número de bins debe ser menor al número de valores en el atributo.")
    if isinstance(x, list):
        x = np.array(x)
    elif isinstance(x, pd.Series):
        x = x.values
    
    elif not isinstance(x, np.ndarray):
        raise ValueError("El argumento 'x' debe ser una lista o un array NumPy.")
    if len(x) == 0:
        raise ValueError("La lista de valores está vacía.")
    if not np.issubdtype(x.dtype, np.number):
     raise ValueError("Los valores del atributo deben ser numéricos.")

        
    min_val = np.min(x)
    max_val = np.max(x)
    bin_size = (max_val - min_val) / num_bins

    x_smoothed = []
    for i in range(1, num_bins + 1):
        bin_values = [val for val in x if val >= min_val + (i-1) * bin_size and val < min_val + i * bin_size]
        if len(bin_values) > 0:
            bin_mean = sum(bin_values) / len(bin_values)
            bin_mean = round(bin_mean)
            x_smoothed.extend([bin_mean] * len(bin_values))
    return x_smoothed

def smooth_by_bin_median(x, num_bins):
    """
    Suaviza los valores en cada intervalo reemplazándolos con el valor median del intervalo.

    Parámetros:
    - x (lista o array): Una lista de valores numéricos.
    - num_bins (int): El número de intervalos.

    Retorna:
    - x_suavizado (lista): Una lista de valores suavizados.
    """
    if num_bins <= 0:
        raise ValueError("El número de intervalos debe ser mayor que cero.")
    if num_bins >= len(x):
        raise ValueError("El número de bins debe ser menor al número de valores en el atributo.")
    if isinstance(x, list):
        x = np.array(x)
    elif isinstance(x, pd.Series):
        x = x.values
    elif not isinstance(x, np.ndarray):
        raise ValueError("El argumento 'x' debe ser una lista o un array NumPy.")
    if len(x) == 0:
        raise ValueError("La lista de valores está vacía.")
    if not np.issubdtype(x.dtype, np.number):
     raise ValueError("Los valores del atributo deben ser numéricos.")

        
    min_val = np.min(x)
    max_val = np.max(x)
    bin_size = (max_val - min_val) / num_bins

    x_smoothed = []
    for i in range(1, num_bins + 1):
        bin_values = [val for val in x if val >= min_val + (i-1) * bin_size and val < min_val + i * bin_size]
        if len(bin_values) > 0:
            bin_median = statistics.median(bin_values)
            bin_median = round(bin_median)
            x_smoothed.extend([bin_median] * len(bin_values))
    return x_smoothed

def smooth_by_bin_boundaries(x, num_bins):
    """
    Suaviza los valores en cada intervalo reemplazándolos con los límites del intervalo.

    Parámetros:
    - x (lista o array): Una lista de valores numéricos.
    - num_bins (int): El número de intervalos.

    Retorna:
    - x_suavizado (lista): Una lista de valores suavizados.
    """

    if num_bins <= 0:
        raise ValueError("El número de intervalos debe ser mayor que cero.")
    if num_bins >= len(x):
        raise ValueError("El número de bins debe ser menor al número de valores en el atributo.")
    if isinstance(x, list):
        x = np.array(x)
    elif isinstance(x, pd.Series):
        x = x.values
    elif not isinstance(x, np.ndarray):
        raise ValueError("El argumento 'x' debe ser una lista o un array NumPy.")
    if len(x) == 0:
        raise ValueError("La lista de valores está vacía.")
    if not np.issubdtype(x.dtype, np.number):
     raise ValueError("Los valores del atributo deben ser numéricos.")

        
    min_val = np.min(x)
    max_val = np.max(x)
    bin_size = (max_val - min_val) / num_bins

    x_smoothed = []
    for i in range(1, num_bins + 1):
        bin_values = [val for val in x if val >= min_val + (i-1) * bin_size and val < min_val + i * bin_size]
        bin_lower_boundary = min_val + (i-1) * bin_size
        bin_upper_boundary = min_val + i * bin_size
        bin_upper_boundary = round(bin_upper_boundary)
        bin_lower_boundary = round(bin_lower_boundary)
        x_smoothed.extend([bin_lower_boundary] * len(bin_values))
        if i < num_bins:
            x_smoothed.append(bin_upper_boundary)
    return x_smoothed

# FUNCION dataset --------------------------------------------------------------
def discretize_dataset(dataset, num_bins, method, smoothing_method=None):
    """
    Discretiza un conjunto de datos utilizando el método especificado y realiza un suavizado de datos.

    Parámetros:
    - dataset (Dataset): Un conjunto de datos representado como objeto Dataset.
    - num_bins (int): El número de intervalos para discretizar cada atributo del conjunto de datos.
    - method (str): El método de discretización a utilizar. Puede ser 'equal_width' (ancho igual) o 'equal_frequency' (frecuencia igual).
    - smoothing_method (str): El método de suavizado a utilizar. Puede ser 'mean' (media), 'median' (mediana), 'boundaries' (límites) o None (ninguno).

    Devoluciones:
    - discretized_dataset (Dataset): Un nuevo conjunto de datos con los atributos discretizados y suavizados.    
    """
    if method != 'equal_width' and method != 'equal_frequency':
        raise ValueError("Método de discretización inválido. Use 'equal_width' o 'equal_frequency'.")
    
    if smoothing_method not in [None, 'mean', 'median', 'boundaries']:
        raise ValueError("Método de suavizado inválido. Utilice 'mean', 'median', 'boundaries' o None.")


    # Crear un nuevo objeto Dataset para almacenar el conjunto de datos discretizado   
    discretized_dataset = Dataset()

    # Iterar sobre cada atributo en el conjunto de datos original
    for attribute in dataset.get_attributes():
        attribute_values = dataset.get_attribute(attribute)

        # Verificar si el atributo es numérico
        if all(isinstance(val, (int, float)) for val in attribute_values):
            if method == 'equal_width':
                x_discretized, cut_points = discretizeEW(attribute_values, num_bins)
            elif method == 'equal_frequency':
                x_discretized, cut_points = discretizeEF(attribute_values, num_bins)
            
            # Aplica el suavizado si se especifica el método de suavizado
            if smoothing_method:
                if smoothing_method == 'mean':
                    x_smoothed = smooth_by_bin_mean(attribute_values, num_bins)
                elif smoothing_method == 'median':
                    x_smoothed = smooth_by_bin_median(attribute_values, num_bins)
                elif smoothing_method == 'boundaries':
                    x_smoothed = smooth_by_bin_boundaries(attribute_values, num_bins)
                # Actualiza los valores del atributo con los valores suavizados
                discretized_dataset.add_attribute(attribute, x_smoothed)
            else:
                # Agrega el atributo discretizado al nuevo conjunto de datos
                discretized_dataset.add_attribute(attribute, x_discretized) 
        else:
            # Agregar el atributo sin cambios al nuevo conjunto de datos
            discretized_dataset.add_attribute(attribute, attribute_values)

    return discretized_dataset
