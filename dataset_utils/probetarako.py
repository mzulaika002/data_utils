import matplotlib.pyplot as plt
import numpy as np

def plot_entropy(entropy_values):
    """
    Genera un gráfico de barras para visualizar los valores de entropía.

    Parámetros:
    - entropy_values (list): Lista de valores de entropía.
    """
    plt.figure()
    plt.bar(range(len(entropy_values)), entropy_values)
    plt.xlabel('Atributo')
    plt.ylabel('Entropía')
    plt.title('Valores de Entropía')
    plt.xticks(range(len(entropy_values)))
    plt.show()

def plot_variance(variance_values):
    """
    Genera un gráfico de barras para visualizar los valores de varianza.

    Parámetros:
    - variance_values (list): Lista de valores de varianza.
    """
    plt.figure()
    plt.bar(range(len(variance_values)), variance_values)
    plt.xlabel('Atributo')
    plt.ylabel('Varianza')
    plt.title('Valores de Varianza')
    plt.xticks(range(len(variance_values)))
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


