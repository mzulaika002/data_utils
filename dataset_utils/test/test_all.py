# Importar los módulos
from dataset_utils.dataset import Dataset
from dataset_utils.discretization import discretize_dataset
from dataset_utils.metrics import get_entropies, get_variances_pd, ROC_AUC
from dataset_utils.preprocessing import normalize_dataframe
from dataset_utils.filtering import filter_variables
from dataset_utils.correlation import calculate_correlation
from dataset_utils.visualization import plot_auc, plot_correlation_matrix, plot_entropy

# Crear un objeto Dataset
data = [
    [1, 2, 'A'],
    [2, 4, 'B'],
    [3, 6, 'A'],
    [4, 8, 'B'],
    [5, 10, 'A'],
]

data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
    }
dataset = Dataset(data)

# Escribir datos en un archivo
dataset.write_data('data_output.csv')

# Leer datos desde un archivo
dataset.read_data('data_output.csv')

# Obtener los valores de un atributo específico
attribute_values = dataset.get_attribute('Name')

# Establecer los valores de un atributo específico
dataset.set_attribute('3', attribute_values)

# Obtener la lista de nombres de atributos
attribute_names = dataset.get_attributes()

# Obtener el DataFrame de pandas que representa los datos del conjunto de datos
dataframe = dataset.get_data()

# Discretizar el dataset utilizando el método de igual frecuencia
discretized_dataset = discretize_dataset(dataset, num_bins=5, method='equal_frequency')

# Calcular las entropías de las columnas en el dataset
entropies = get_entropies(dataframe)

# Calcular las varianzas de las columnas en el dataset
variances = get_variances_pd(dataframe)

# Calcular los puntos de la curva ROC y el AUC
fpr, tpr, cut_offs, auc_score = ROC_AUC(dataframe)

# Normalizar el DataFrame
normalized_df = normalize_dataframe(dataframe)

# Filtrar las variables del dataset basado en la métrica y umbral
filtered_dataset = filter_variables(data, metric='entropy', threshold=0.5)

# Calcular la matriz de correlación
correlation_matrix = calculate_correlation(data)

# Graficar la curva ROC y el AUC
plot_auc(fpr, tpr, auc_score)

# Graficar la matriz de correlación
plot_correlation_matrix(correlation_matrix)

# Graficar los valores de entropía
entropy_values = [0.1, 0.5, 0.3]
labels = ['A', 'B', 'C']
plot_entropy(entropy_values, labels)
