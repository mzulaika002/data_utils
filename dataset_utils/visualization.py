import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

def plot_mutual_information_matrix(matrix):
    """
    Función para graficar la matriz de información mutua.
    
    Args:
        matrix (array): Matriz de información mutua.
    """
    plt.figure(figsize=(8, 8))
    sns.heatmap(matrix, annot=True, fmt=".2f", cmap='coolwarm',
                cbar=True, square=True, linewidths=0.5)
    plt.title('Mutual Information Matrix')
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