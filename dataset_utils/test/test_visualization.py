from dataset_utils.visualization import *
from dataset_utils.metrics import *
from dataset_utils.correlation import *

# Crear un DataFrame de ejemplo
data = pd.DataFrame({
    'edad': [25, 32, 41, 35, 28, 46, 38, 29, 33, 27, 31, 37, 39, 44, 30],
    'ingresos': [50000, 60000, 75000, 80000, 55000, 90000, 65000, 70000, 62000, 48000, 58000, 62000, 78000, 85000, 54000],
    'altura':[165.2, 170.5, 182.1, 175.7, 168.9, 190.3, 174.6, 169.8, 171.2, 167.5, 170.1, 178.6, 179.4, 185.0, 172.8],
    'color_de_pelo': ['rubio', 'negro','negro','rubio','rubio', 'negro','moreno', 'negro','rubio', 'negro','rubio','negro','rubio','negro','moreno'],
    'estado_civil': ['soltero', 'casado', 'casado', 'soltero', 'soltero', 'casado', 'divorciado', 'casado', 'soltero', 'casado', 'soltero', 'casado', 'soltero', 'casado', 'divorciado'],
    'fuma': [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
})

# Crear un objeto Dataset
dataset = Dataset(data)

# Graficar la matriz de correlación
matrix = calculate_correlation_matrix(dataset)
plot_correlation_matrix(matrix)

# Graficar la entropia de Age y  Marks, 
entropy_values = []

entropy_values.append(calculate_attribute_entropy(dataset,'edad'))
entropy_values.append(calculate_attribute_entropy(dataset,'ingresos'))
plot_entropy(entropy_values, ['edad', 'ingresos'])

# Graficar la entropia de Age
variance_values = []
variance_values.append(calculate_attribute_variance(dataset,'altura'))
variance_values.append(calculate_attribute_variance(dataset,'altura'))
plot_entropy(variance_values, ['altura', 'altura'])

#Gracicar el AUC del atributo 'edad' en relación al atributo de clase 'Bin'
plot_roc_auc(dataset, 'edad', 'fuma')













