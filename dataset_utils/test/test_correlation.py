# Importar las librerías necesarias
import pandas as pd
from dataset_utils.dataset import Dataset
from dataset_utils.correlation import calculate_correlation

# Crear un DataFrame de ejemplo
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': ['x', 'y', 'z', 'x', 'y']
}

# Crear un objeto Dataset 
dataset = Dataset(data)

# Calcular la correlación entre las variables del dataset
correlation_matrix = calculate_correlation(dataset)

# Imprimir la matriz de correlación
print("Matriz de correlación:")
print(correlation_matrix)
