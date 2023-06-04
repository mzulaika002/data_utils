################################################################################
# Este script "visualization.py" proporciona la definición de varias funciones #
# de visualización de las métricas utilizando la biblioteca Matplotlib         #
# *****************************************************************************#
# Autora:   Muitze Zulaika Gallastegi                                          #
# Fecha:    02/06/2023                                                         #
################################################################################


# CARGAR LIBRERIAS -------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# CARGAR FUNCIONES DE OTROS FICHEROS -------------------------------------------
from dataset_utils.dataset import Dataset
from dataset_utils.metrics import  *

# FUNCIONES --------------------------------------------------------------------
def plot_entropy(entropy_values, attribute_names):
    """
    Genera un gráfico de barras para visualizar los valores de entropía.

    Parámetros:
    - entropy_values (list): Lista de valores de entropía.
    - attribute_names (list): Lista de nombres de atributos.
    """
    plt.figure()
    plt.bar(range(len(entropy_values)), entropy_values)
    plt.xlabel('Atributo')
    plt.ylabel('Entropía')
    plt.title('Valores de Entropía')

    plt.xticks(range(len(entropy_values)), attribute_names, rotation='vertical')
    plt.subplots_adjust(bottom=0.3) 

    plt.show()

def plot_variance(variance_values,attribute_names):
    """
    Genera un gráfico de barras para visualizar los valores de varianza.

    Parámetros:
    - variance_values (list): Lista de valores de varianza.
    - attribute_names (list): Lista de nombres de atributos.
    """
    plt.figure()
    plt.bar(range(len(variance_values)), variance_values)
    plt.xlabel('Atributo')
    plt.ylabel('Varianza')
    plt.title('Valores de Varianza')
    plt.xticks(range(len(variance_values)))
    plt.xticks(range(len(entropy_values)), attribute_names, rotation='vertical')
    plt.subplots_adjust(bottom=0.3) 

    plt.show()


def plot_auc(auc_values):
    """
    Genera un gráfico de barras para visualizar los valores de AUC.

    Parámetros:
    - auc_values (list): Lista de valores de AUC.
    """
    plt.figure()
    plt.bar(range(len(auc_values)), auc_values)
    plt.xlabel('Atributo')
    plt.ylabel('AUC')
    plt.title('Valores de AUC')
    plt.xticks(range(len(auc_values)))
    plt.show()

def plot_correlation_matrix(correlation_matrix):
    """
    Genera un mapa de calor para visualizar la matriz de correlación.

    Parámetros:
    - correlation_matrix (np.ndarray): Matriz de correlación.
    """
    plt.figure()
    plt.imshow(correlation_matrix, cmap='YlOrBr', interpolation='nearest')
    plt.colorbar()
    plt.title('Matriz de Correlación')
    plt.show()

def plot_roc_auc(dataset, attribute, class_attribute):
    """
    Visualiza el plot de AUC y ROC de un atributo específico del conjunto de datos en relación al atributo de clase.

    Parámetros:
    - dataset (Dataset): Objeto Dataset que contiene los datos.
    - attribute (str): Nombre del atributo a calcular el AUC.
    - class_attribute (str): Nombre del atributo de clase binario.

    Excepciones:
    - ValueError: Si el atributo no existe en el conjunto de datos, no es continuo o el atributo de clase no existe.
    """
    try:
        attribute_values = dataset.get_attribute(attribute)
        class_labels = dataset.get_attribute(class_attribute)
        if attribute_values.dtype != 'object' and class_labels.dtype != 'object':
            tpr_values, fpr_values, auc = calculate_auc(attribute_values, class_labels)

            plt.figure(figsize=(8, 6))
            plt.plot(fpr_values, tpr_values, label=f'AUC = {auc:.2f}')
            plt.plot([0, 1], [0, 1], 'k--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title(f'ROC Curve - Attribute: {attribute}, Class Attribute: {class_attribute}')
            plt.legend(loc="lower right")
            plt.show()
        else:
            raise ValueError(f"El atributo '{attribute}' o el atributo de clase '{class_attribute}' no son continuos.")
    except ValueError as e:
        print(e)

