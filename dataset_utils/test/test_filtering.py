# Importar las bibliotecas necesarias
from dataset_utils.dataset import Dataset
from dataset_utils.metrics import calculate_attribute_entropy, calculate_attribute_variance, calculate_attribute_auc
from dataset_utils.filtering import filter_variables


data = {
    'attribute1': [1, 2, 3, 4, 5],
    'attribute2': ['A', 'B', 'C', 'D', 'E'],
    'attribute3': [0.1, 0.2, 0.3, 0.4, 0.5],
    'target': [0, 1, 0, 1, 0]
}
dataset = Dataset(data)


# Filtrar variables basado en la entropía mayor que 1
filtered_dataset = filter_variables(dataset, 'entropy', 1, '<')
# Mostrar las variables filtradas
print(filtered_dataset.get_attributes())

# Filtrar variables basado en la varianza mayor que 1
filtered_dataset = filter_variables(dataset, 'variance', 1, '<')
# Mostrar las variables filtradas
print(filtered_dataset.get_attributes())

# Filtrar variables basado en la auc mayor que 1
filtered_dataset = filter_variables(dataset, 'auc', 1, '<','target' )
# Mostrar las variables filtradas
print(filtered_dataset.get_attributes())
