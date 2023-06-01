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

# FUNCIONES --------------------------------------------------------------------
def filter_variables(dataset, metric, threshold):
    """
    Filtra las variables de un dataset en base a una métrica y un umbral.

    Parámetros:
    - dataset (list): Un dataset representado como una lista de listas, donde cada lista interna representa una columna o atributo del dataset.
    - metric (str): La métrica a utilizar para el filtrado. Puede ser 'entropy', 'variance' o 'auc'.
    - threshold (float): El umbral a aplicar en la métrica. Solo se mantendrán las variables que superen este umbral.

    Devoluciones:
    - filtered_dataset (list): Un nuevo dataset que contiene únicamente las variables que cumplen el requisito de la métrica y umbral indicados.
    """
    filtered_dataset = []

    if metric == 'entropy':
        # Calcular las entropías de cada variable en el dataset
        entropies = get_entropies(dataset)
        # Filtrar las variables basadas en el umbral de entropía
        for i, entropy_val in enumerate(entropies):
            if entropy_val > threshold:
                filtered_dataset.append(dataset[i])
    elif metric == 'variance':
        # Calcular las varianzas de cada variable en el dataset
        variances = get_variances(dataset)
        # Filtrar las variables basadas en el umbral de varianza
        for i, variance_val in enumerate(variances):
            if variance_val > threshold:
                filtered_dataset.append(dataset[i])
    elif metric == 'auc':
        # Calcular el AUC de cada variable en el dataset
        aucs = ROC_AUC(dataset)
        # Filtrar las variables basadas en el umbral de AUC
        for i, auc_val in enumerate(aucs):
            if auc_val > threshold:
                filtered_dataset.append(dataset[i])
    else:
        raise ValueError("Métrica inválida. Use 'entropy', 'variance' o 'auc'.")

    return filtered_dataset




























