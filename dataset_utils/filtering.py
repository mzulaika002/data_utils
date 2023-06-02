################################################################################
# El módulo 'Filtering' tiene una funciones para filtrar las variables de un   #
# conjunto de datos según diferentes métricas y criterios de umbral.          #
# *****************************************************************************#
# Autora:   Muitze Zulaika Gallastegi                                          #
# Fecha:    02/06/2023                                                         #
################################################################################

# CARGAR FUNCIONES DE OTROS FICHEROS -------------------------------------------
from dataset_utils.dataset import Dataset
from dataset_utils.metrics import *

def filter_variables(dataset, metric, threshold, operator, class_attribute=None):
    """
    Filtra las variables del conjunto de datos según la métrica especificada y los criterios de umbral.

    Parámetros:
    - dataset (Dataset): Objeto Dataset que contiene los datos.
    - metric (str): Métrica a utilizar para filtrar las variables. Puede ser 'entropy', 'variance' o 'auc'.
    - threshold (float): Valor de umbral para comparar con la métrica.
    - operator (str): Operador a utilizar para comparar la métrica con el umbral. Puede ser '>', '<', '=='.

    Devoluciones:
    - Nuevo objeto Dataset que contiene las variables filtradas.
    """
    attributes = dataset.get_attributes()
    filtered_data = Dataset()

    for attribute in attributes:
        if metric == 'entropy':
            metric_value = calculate_attribute_entropy(dataset, attribute)
        elif metric == 'variance':
            metric_value = calculate_attribute_variance(dataset, attribute)
        elif metric == 'auc':
            metric_value = calculate_attribute_auc(dataset, attribute, class_attribute)
        else:
            print(f"Métrica '{metric}' no válida.")
            return None

        if metric_value is not None: # Comprobar si la métrica se ha podido calcular
            if operator == '>' and metric_value > threshold:
                filtered_data.add_attribute(attribute, dataset.get_attribute(attribute))
            elif operator == '<' and metric_value < threshold:
                filtered_data.add_attribute(attribute, dataset.get_attribute(attribute))
            elif operator == '==' and metric_value == threshold:
                filtered_data.add_attribute(attribute, dataset.get_attribute(attribute))

    if filtered_data.empty():
       print("No hay atributos que cumplan con las condiciones especificadas.")

    return filtered_data


























