from dataset_utils.dataset import Dataset
from dataset_utils.metrics import *
'''
# Crear un dataset de ejemplo
dataset = Dataset()
dataset.add_attribute("A", [1, 2, 3, 4, 5])
dataset.add_attribute("B", [1, 2, 3, 4, 5])
dataset.add_attribute("C", [1, 2, 3, 4, 5])
dataset.add_attribute("D", [1, 2, 3, 4, 5])
dataset.add_attribute("E", ["x", "y", "z", "w", "v"])
dataset.add_attribute("Class", [0, 1, 1, 0, 1])

# Aplicar el filtrado de variables con diferentes métricas y umbrales
filtered_dataset_entropy = filter_variables(dataset, 'entropy', 0.5)
filtered_dataset_variance = filter_variables(dataset, 'variance', 2)
filtered_dataset_auc = filter_variables(dataset, 'auc', 0.7)

# Imprimir los atributos filtrados
print("Atributos filtrados por entropía:")
for attribute in filtered_dataset_entropy.get_attributes():
    print(attribute)
print()

print("Atributos filtrados por varianza:")
for attribute in filtered_dataset_variance.get_attributes():
    print(attribute)
print()

print("Atributos filtrados por AUC:")
for attribute in filtered_dataset_auc.get_attributes():
    print(attribute)
print()

'''


def filter_variables(self, threshold, metric):
        """
        Filtra las variables del conjunto de datos en base a una métrica y un umbral.

        Parámetros:
        - threshold: Umbral para la métrica. Las variables cuya métrica sea superior al umbral se mantendrán.
        - metric: Función de métrica a utilizar. Debe ser una de las funciones definidas en el archivo metrics.py.

        Devoluciones:
        - Nuevo objeto Dataset con las variables filtradas.
        """
        filtered_data = self.data.copy()  # Copiar los datos para mantener el conjunto original intacto

        for attribute in self.get_attributes():
            attribute_values = self.get_attribute(attribute)
            try:
                metric_value = metric(attribute_values, self.data['class'])  # Suponiendo que el atributo de clase se llama 'class'
                if np.isnan(metric_value) or metric_value <= threshold:
                    filtered_data.drop(columns=[attribute], inplace=True)  # Eliminar la variable del DataFrame
            except ValueError as e:
                print(e)

        return Dataset(filtered_data)

dataset = Dataset()
dataset.read_data('datos.csv')  # Suponiendo que los datos se cargan desde un archivo CSV

filtered_dataset = dataset.filter_variables(0.5, calculate_attribute_entropy)

filtered_dataset.write_data('datos_filtrados.csv')  # Guardar los datos filtrados en un nuevo archivo CSV
