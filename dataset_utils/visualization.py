################################################################################
# #
# #
##
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

# FUNCIONES --------------------------------------------------------------------
'''
def plot_auc(fpr, tpr, auc_score):
    """
    Función para graficar la curva ROC y el AUC.
    
    Args:
        fpr (array): Valores de tasa de falsos positivos.
        tpr (array): Valores de tasa de verdaderos positivos.
        auc_score (float): Valor del AUC.
    """
    plt.figure(figsize=(6, 6))
    plt.plot(fpr, tpr, label='ROC curve (AUC = %0.2f)' % auc_score)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.show()

def plot_correlation_matrix(matrix):
    """
    Función para graficar la matriz de correlación.
    
    Args:
        matrix (array): Matriz de correlación.
    """
    plt.figure(figsize=(8, 8))
    sns.heatmap(matrix, annot=True, fmt=".2f", cmap='coolwarm',
                cbar=True, square=True, linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()

def plot_entropy(entropy_values, labels):
    """
    Función para graficar los valores de entropía.
    
    Args:
        entropy_values (array): Valores de entropía.
        labels (list): Etiquetas para cada valor de entropía.
    """
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(entropy_values)), entropy_values)
    plt.xticks(range(len(entropy_values)), labels, rotation='vertical')
    plt.xlabel('Variable')
    plt.ylabel('Entropy')
    plt.title('Entropy of Variables')
    plt.show()
'''



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

def plot_auc_roc(dataset, attribute, class_attribute):
    try:
        attribute_values = dataset.get_attribute(attribute)
        class_labels = dataset.get_attribute(class_attribute)
        if attribute_values.dtype != 'object' and class_labels.dtype != 'object':
            auc, tpr_values, fpr_values = calculate_auc(attribute_values, class_labels)
            plt.plot(fpr_values, tpr_values, label=f"AUC = {auc:.2f}")
            plt.plot([0, 1], [0, 1], 'k--')
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title('Receiver Operating Characteristic (ROC)')
            plt.legend(loc='lower right')
            plt.show()
        else:
            raise ValueError(f"El atributo '{attribute}' o el atributo de clase '{class_attribute}' no son continuos.")
    except ValueError as e:
        print(e)
