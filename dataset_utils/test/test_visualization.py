from dataset_utils.visualization import *
from dataset_utils.metrics import *
from dataset_utils.correlation import *

# Calcular las métricas
attribute_names = ['Atributo 1', 'Atributo 2', 'Atributo 3']
entropy_values = [0.5, 0.3, 0.7]
variance_values = [0.2, 0.4, 0.6]
auc_values = [0.8, 0.6, 0.9]
correlation_matrix = np.random.rand(3, 3)
mutual_information_matrix = np.random.rand(3, 3)

print(np.random.rand(3, 3))


# Visualizar las métricas
plot_entropy(entropy_values,attribute_names)
plot_variance(variance_values)
plot_auc(auc_values)
plot_correlation_matrix(correlation_matrix)
