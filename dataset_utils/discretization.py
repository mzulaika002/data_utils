from dataset_utils.dataset import Dataset

def discretizeEW(x, num_bins):
  """
  Discretizar un atributo de entrada `x` en `num_bins` intervalos usando la discretización Equal Width.

  Parámetros:
   - x (lista): una lista de valores numéricos
   - num_bins (int): el número de intervalos para discretizar en `x` 

  Devoluciones:
    - x_discretitizado: lista de valores discretizados, representados como string en la forma "I<n>", 
                        donde <n> es el índice de intervalo.
    - Lista de puntos:  lista de puntos de corte entre intervalos.   
  """
  if num_bins <= 0:
    raise ValueError("El número de intervalos debe ser mayor que cero.")
  
  if not x:
    raise ValueError("La lista de valores está vacía.")

  # Determinar los valores máximo y mínimo de la lista
  max_val = max(x)
  min_val = min(x)

  # Calcular el tamaño de cada intervalo
  bin_size = (max_val - min_val) / num_bins

  # Cree una lista de los puntos de corte para cada intervalo
  cut_points = [min_val + (i * bin_size) for i in range(num_bins)]

  # Crear una lista vacía para almacenar los valores agrupados
  x_discretized = []

  # Iterar sobre los valores en la lista y asignarlos a un intervalo
  for val in x:
    for i, cut_point in enumerate(cut_points):
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
    if not x:
        raise ValueError("La lista de valores está vacía.")

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
        for i, cut_point in enumerate(cut_points):
            if element <= cut_point:
                x_discretized.append(f"I{i+1}")
                break
        else:
            x_discretized.append(f"I{num_bins}")

    return x_discretized, cut_points


def discretize(x, cut_points):
    """
    Discretiza los valores de entrada `x` en los intervalos definidos por los puntos de corte.

    Parámetros:
    - x (list): Una lista de valores numéricos a discretizar.
    - cut_points (list): Una lista de puntos de corte que definen los intervalos.

    Devoluciones:
    - x_discretized (list): Una lista de valores discretizados, representados como string en la forma "I<n>",
                            donde <n> es el índice de intervalo.
    - cut_points (list): La lista de puntos de corte original, sin cambios.
    """

    # Validar los argumentos de entrada
    if not isinstance(x, list):
        raise TypeError("El argumento 'x' debe ser una lista.")
    if not isinstance(cut_points, list):
        raise TypeError("El argumento 'cut_points' debe ser una lista.")

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
    - atrinuto (list): Un atributo representado como una lista.
    - num_bins (int): El número de intervalos para discretizar cada atributo del dataset.
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


def discretize_dataset(dataset, num_bins, method):
    """
    Discretiza un dataset utilizando el método especificado.

    Parámetros:
    - dataset (Dataset): Un dataset representado como el objeto Dataset.
    - num_bins (int): El número de intervalos para discretizar cada atributo del dataset.
    - method (str): El método de discretización a utilizar. Puede ser 'equal_width' (ancho igual) o 'equal_frequency'
                    (frecuencia igual).

    Devoluciones:
    - discretized_dataset (Dataset): Un nuevo dataset con los atributos discretizados.
    """
    if method != 'equal_width' and method != 'equal_frequency':
        raise ValueError("Método de discretización inválido. Use 'equal_width' o 'equal_frequency'.")

    # Crear un nuevo objeto Dataset para almacenar el dataset discretizado
    discretized_dataset = Dataset()

    # Iterar sobre cada atributo en el dataset original
    for attribute in dataset.get_attributes():
        if method == 'equal_width':
            x_discretized, cut_points = discretizeEW(attribute, num_bins)
        elif method == 'equal_frequency':
            x_discretized, cut_points = discretizeEF(attribute, num_bins)

        # Agregar el atributo discretizado al nuevo dataset
        discretized_dataset.set_attribute(attribute, x_discretized)

    return discretized_dataset


''''
def discretizeUW(x, bin_widths):
    """
    Discretiza un atributo de entrada `x` en intervalos con anchuras desiguales definidas por `bin_widths`.

    Parámetros:
    - x (list): Una lista de valores numéricos.
    - bin_widths (list): Una lista de anchuras de intervalo para la discretización.

    Devoluciones:
    - x_discretized (list): Lista de valores discretizados, representados como strings en la forma "I<n>",
                            donde <n> es el índice de intervalo.
    - cut_points (list): Lista de puntos de corte entre intervalos.
    """
    if not x:
        raise ValueError("La lista de valores está vacía.")

    if len(x) != len(bin_widths):
        raise ValueError("La cantidad de anchuras de intervalo debe ser igual a la cantidad de valores en x.")

    # Crear una lista de los puntos de corte para cada intervalo
    cut_points = [sum(bin_widths[:i]) for i in range(1, len(bin_widths))]

    # Inicializar lista para valores discretizados
    x_discretized = []

    # Iterar sobre los valores en la lista y asignarlos a un intervalo
    for val in x:
        for i, cut_point in enumerate(cut_points):
            if val < cut_point:
                x_discretized.append(f'I{i}')
                break
        else:
            x_discretized.append(f'I{len(bin_widths)}')

    return x_discretized, cut_points


def discretizeUF(x, num_bins):
    """
    Discretiza un atributo de entrada `x` en `num_bins` intervalos con frecuencias desiguales.

    Parámetros:
    - x (list): Una lista de valores numéricos.
    - num_bins (int): El número de intervalos para dividir en `x`.

    Devoluciones:
    - x_discretized (list): Lista de valores discretizados, representados como strings en la forma "I<n>",
                            donde <n> es el índice de intervalo.
    - cut_points (list): Lista de puntos de corte entre intervalos.
    """
    if num_bins <= 0:
        raise ValueError("El número de intervalos debe ser mayor que cero.")

    if not x:
        raise ValueError("La lista de valores está vacía.")

    # Ordenar x en orden ascendente
    x_sorted = sorted(x)

    # Calcular la cantidad de elementos por intervalo
    elements_per_interval = len(x) // num_bins

    # Calcular el residuo para distribuir los elementos adicionales
    remainder = len(x) % num_bins

    # Crear una lista de los puntos de corte para cada intervalo
    cut_points = []
    start = 0
    for i in range(num_bins):
        end = start + elements_per_interval + (1 if i < remainder else 0)
        cut_points.append(x_sorted[end - 1])
        start = end

    # Inicializar lista para valores discretizados
    x_discretized = []

    # Iterar sobre los elementos en x y encontrar el intervalo al que pertenecen
    for element in x:
        for i, cut_point in enumerate(cut_points):
            if element <= cut_point:
                x_discretized.append(f"I{i+1}")
                break
        else:
            x_discretized.append(f"I{num_bins}")

    return x_discretized, cut_points
'''''









