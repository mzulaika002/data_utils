################################################################################
# Este script "dataset.py" proporciona una clase Dataset para trabajar         #
# con conjuntos de datos: cargar, modificar y analizar conjuntos de datos      #
# de forma sencilla                                                            #
# *****************************************************************************#
# Autora:   Muitze Zulaika Gallastegi                                          #
# Fecha:    02/06/2023                                                         #
################################################################################


# CARGAR LIBRERIAS -------------------------------------------------------------
import pandas as pd

# GUÍA DE USUARIO --------------------------------------------------------------
"""
Este script proporciona una clase Dataset para trabajar con conjuntos de datos.
A continuación, se enumeran las funciones disponibles:

1. read_data(file_path): Lee los datos desde un archivo y los carga en el objeto Dataset.
2. write_data(file_path): Escribe los datos del objeto Dataset en un archivo.
3. get_attribute(attribute): Obtiene los valores de un atributo específico del conjunto de datos.
4. new_attribute(attribute, values): Establece los valores de un nuevo atributo específico en el conjunto de datos.
5. set_attribute(attribute, values): Establece los valores de un atributo específico en el conjunto de datos.
6. get_attributes(): Obtiene una lista de los nombres de los atributos en el conjunto de datos.
7. get_data(): Obtiene el DataFrame de pandas que representa los datos del conjunto de datos.

Utilice esta clase para cargar, modificar y analizar conjuntos de datos de forma sencilla.

Ejemplo de uso:

# Crear un objeto Dataset
dataset = Dataset()

# Leer datos desde un archivo
dataset.read_data('data.csv')

# Obtener los nombres de los atributos
attributes = dataset.get_attributes()
print("Nombres de atributos:", attributes)

# Obtener los valores de un atributo específico
attribute_values = dataset.get_attribute('attribute_name')
print("Valores del atributo:", attribute_values)

# Establecer valores para un nuevo atributo
new_attribute_values = [1, 2, 3, 4, 5]
dataset.new_attribute('new_attribute', new_attribute_values)

# Establecer valores para un atributo existente
existing_attribute_values = [10, 20, 30, 40, 50]
dataset.set_attribute('existing_attribute', existing_attribute_values)

# Guardar los datos en un archivo
dataset.write_data('output.csv')

# Obtener el DataFrame de los datos
data_frame = dataset.get_data()
print("DataFrame de los datos:")
print(data_frame)
"""

# ANALISIS --------------------------------------------------------------------
class Dataset:
    def __init__(self, data=None):
        """
        Inicializa un objeto Dataset.

        Parámetros:
        - data: DataFrame de pandas opcional que contiene los datos del conjunto de datos.
        """
        if data is None:
            self.data = pd.DataFrame()  # Crea un DataFrame vacío si no se proporcionan datos
        else:
            self.data = pd.DataFrame(data)  # Convierte los datos en un DataFrame


    def read_data(self, file_path):
        """
        Lee los datos desde un archivo y los carga en el objeto Dataset.

        Parámetros:
        - file_path: Ruta del archivo que contiene los datos.
        """
        self.data = pd.read_csv(file_path)  # lectura de datos desde un archivo CSV

    def write_data(self, file_path):
        """
        Escribe los datos del objeto Dataset en un archivo.

        Parámetros:
        - file_path: Ruta del archivo donde se guardarán los datos.
        """
        self.data.to_csv(file_path, index=False)  # escritura de datos a un archivo CSV

    def get_attribute(self, attribute):
        """
        Obtiene los valores de un atributo específico del conjunto de datos.

        Parámetros:
        - attribute: Nombre del atributo deseado.

        Devoluciones:
        - Serie de pandas que contiene los valores del atributo especificado.

        Excepciones:
        - ValueError: Si el atributo no existe en el conjunto de datos.
        """
        try:
            if attribute in self.data.columns:
                return self.data[attribute]
            else:
                raise ValueError(f"El atributo '{attribute}' no existe en el conjunto de datos, si quiere crear un nuevo atributo use la función \"new_attribute\".")
        except ValueError as e:
            print(e)

    def new_attribute(self, attribute, values):
        """
        Establece los valores de un nuevo atributo específico en el conjunto de datos.

        Parámetros:
        - attribute: Nombre del atributo a establecer.
        - values: Valores a asignar al atributo.
        """
        try:
            if attribute not in self.data.columns:
                self.data[attribute] = values
            else:
                raise ValueError(f"El atributo '{attribute}' ya existe en el conjunto de datos, si quieres modificarlo usa la función \"set_attribute\".")
        except ValueError as e:
            print(e)


    def set_attribute(self, attribute, values):
        """
        Establece los valores de un atributo específico en el conjunto de datos.

        Parámetros:
        - attribute: Nombre del atributo a establecer.
        - values: Valores a asignar al atributo.

        Excepciones:
        - ValueError: Si el atributo no existe en el conjunto de datos.
        """
        try:
            if attribute in self.data.columns:
                self.data[attribute] = values
            else:
                raise ValueError(f"El atributo '{attribute}' no existe en el conjunto de datos, si quiere crear un nuevo atributo use la función \"new_attribute\".")
        except ValueError as e:
            print(e)


    def get_attributes(self):
        """
        Obtiene una lista de los nombres de los atributos en el conjunto de datos.

        Devoluciones:
        - Lista de strings que representa los nombres de los atributos.
        """
        return list(self.data.columns)

    def get_data(self):
        """
        Obtiene el DataFrame de pandas que representa los datos del conjunto de datos.

        Devoluciones:
        - DataFrame de pandas que contiene los datos del conjunto de datos.
        """
        return self.data