################################################################################
# El script 'metrics.py' incluye diferentes funciones relacionadas con la      #
# entropía, la varianza y el cálculo del área bajo la curva ROC (AUC).         #
# *****************************************************************************#
# Autora:   Muitze Zulaika Gallastegi                                          #
# Fecha:    02/06/2023                                                         #
################################################################################


# CARGAR LIBRERIAS -------------------------------------------------------------
import numpy as np

# CARGAR FUNCIONES DE OTROS FICHEROS -------------------------------------------
from dataset_utils.dataset import Dataset

def calculate_entropy(attribute_values):
    """
    Calcula la entropía de un atributo discreto.

    Parámetros:
    - attribute_values (pd.Series): Serie de pandas que contiene los valores del atributo discreto.

    Devoluciones:
    - Valor de la entropía del atributo (float).
    """
    value_counts = attribute_values.value_counts()
    probabilities = value_counts / len(attribute_values)
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

def calculate_variance(attribute_values):
    """
    Calcula la varianza de un atributo continuo.

    Parámetros:
    - attribute_values (pd.Series): Serie de pandas que contiene los valores del atributo continuo.

    Devoluciones:
    - Valor de la varianza del atributo (float).
    """
    mean = attribute_values.mean()
    variance = ((attribute_values - mean) ** 2).mean()
    return variance

def calculate_auc(attribute_values, class_labels):
    """
    Calcula el área bajo la curva ROC (AUC) de un atributo continuo en relación a las etiquetas de clase.

    Parámetros:
    - attribute_values (pd.Series): Serie de pandas que contiene los valores del atributo continuo.
    - class_labels (pd.Series): Serie de pandas que contiene las etiquetas de clase binarias (0 o 1).

    Devoluciones:
    - Valor del AUC del atributo (float).
    """
    sorted_indices = np.argsort(attribute_values)
    sorted_attribute = attribute_values[sorted_indices]
    sorted_labels = class_labels[sorted_indices]

    n_positives = np.sum(sorted_labels == 1)
    n_negatives = np.sum(sorted_labels == 0)

    if n_positives == 0 or n_negatives == 0:
        return np.nan

    tpr_values = []
    fpr_values = []
    tpr = 0
    fpr = 0
    last_label = sorted_labels[0]

    for i in range(len(sorted_labels)):
        if sorted_labels[i] != last_label:
            tpr_values.append(tpr)
            fpr_values.append(fpr)
            last_label = sorted_labels[i]

        if sorted_labels[i] == 1:
            tpr += 1
        else:
            fpr += 1

    tpr_values.append(tpr)
    fpr_values.append(fpr)

    tpr_values = np.array(tpr_values) / n_positives
    fpr_values = np.array(fpr_values) / n_negatives

    auc = np.trapz(tpr_values, fpr_values)

    return tpr_values, fpr_values, auc

def calculate_attribute_entropy(dataset, attribute):
    """
    Calcula la entropía de un atributo específico del conjunto de datos.

    Parámetros:
    - dataset (Dataset): Objeto Dataset que contiene los datos.
    - attribute (str): Nombre del atributo a calcular la entropía.

    Devoluciones:
    - Valor de la entropía del atributo (float).

    Excepciones:
    - ValueError: Si el atributo no existe en el conjunto de datos o no es discreto.
    """
    try:
        attribute_values = dataset.get_attribute(attribute)
        attribute_values = dataset.get_attribute(attribute)
        if attribute_values.dtype == 'object':
            return calculate_entropy(attribute_values)
        elif attribute_values.dtype == np.dtype('int64') and (attribute_values % 1 == 0).all():
            return calculate_entropy(attribute_values)
        else:
            raise ValueError(f"El atributo '{attribute}' no es discreto.")
    except ValueError as e:
        print(e)

def calculate_attribute_variance(dataset, attribute):
    """
    Calcula la varianza de un atributo específico del conjunto de datos.

    Parámetros:
    - dataset (Dataset): Objeto Dataset que contiene los datos.
    - attribute (str): Nombre del atributo a calcular la varianza.

    Devoluciones:
    - Valor de la varianza del atributo (float).

    Excepciones:
    - ValueError: Si el atributo no existe en el conjunto de datos o no es continuo.
    """
    try:
        attribute_values = dataset.get_attribute(attribute)
        if np.issubdtype(attribute_values.dtype, np.number) and np.any(attribute_values % 1 != 0):
            return calculate_variance(attribute_values)
        else:
            raise ValueError(f"El atributo '{attribute}' no es continuo.")
    except ValueError as e:
        print(e)

def calculate_attribute_auc(dataset, attribute, class_attribute):
    """
    Calcula el AUC de un atributo específico del conjunto de datos en relación al atributo de clase.

    Parámetros:
    - dataset (Dataset): Objeto Dataset que contiene los datos.
    - attribute (str): Nombre del atributo a calcular el AUC.
    - class_attribute (str): Nombre del atributo de clase binario.

    Devoluciones:
    - Valor del AUC del atributo (float).

    Excepciones:
    - ValueError: Si el atributo no existe en el conjunto de datos, no es continuo o el atributo de clase no existe.
    """
    try:
        attribute_values = dataset.get_attribute(attribute)
        class_labels = dataset.get_attribute(class_attribute)
        if attribute_values.dtype != 'object' and class_labels.dtype != 'object':
            tpr_values, fpr_values, auc = calculate_auc(attribute_values, class_labels)
            return auc
        else:
            raise ValueError(f"El atributo '{attribute}' o el atributo de clase '{class_attribute}' no son continuos.")
    except ValueError as e:
        print(e)



