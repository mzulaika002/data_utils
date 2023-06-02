################################################################################
# #
# #
##
# *****************************************************************************#
# Autora:   Muitze Zulaika Gallastegi                                          #
# Fecha:    02/06/2023                                                         #
################################################################################

# CARGAR FUNCIONES DE OTROS FICHEROS -------------------------------------------
from dataset_utils.dataset import Dataset
from dataset_utils.metrics import *
def filter_variables(dataset, metric, threshold):
    """
    Filtra las variables de un dataset en base a una métrica y un umbral.

    Parámetros:
    - dataset (Dataset): Un objeto Dataset que contiene los datos.
    - metric (str): La métrica a utilizar para el filtrado. Puede ser 'entropy', 'variance' o 'auc'.
    - threshold (float): El umbral a aplicar en la métrica. Solo se mantendrán las variables que superen este umbral.

    Devoluciones:
    - filtered_dataset (Dataset): Un nuevo objeto Dataset que contiene únicamente las variables que cumplen el requisito de la métrica y umbral indicados.
    """

    filtered_dataset = Dataset()
    if metric == 'entropy':
        for attribute in dataset.get_attributes():
            entropy = calculate_attribute_entropy(dataset, attribute)
            if entropy is not None and entropy > threshold:
                filtered_dataset.add_attribute(dataset.get_attribute(attribute).tolist(), attribute)
    elif metric == 'variance':
        for attribute in dataset.get_attributes():
            variance = calculate_attribute_variance(dataset, attribute)
            if variance is not None and variance > threshold:
                filtered_dataset.set_attribute(dataset.get_attribute(attribute).tolist(), attribute)
    elif metric == 'auc':
        class_attribute = dataset.get_attributes()
        for attribute in dataset.get_attributes():
            auc = calculate_attribute_auc(dataset, attribute, class_attribute)
            if auc is not None and auc > threshold:
                filtered_dataset.add_attribute(dataset.get_attribute(attribute).tolist(), attribute)
    else:
        raise ValueError("Métrica inválida. Use 'entropy', 'variance' o 'auc'.")

    return filtered_dataset




























