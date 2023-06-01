################################################################################
# #
# #
##
# *****************************************************************************#
# Autora:   Muitze Zulaika Gallastegi                                          #
# Fecha:    02/06/2023                                                         #
################################################################################


# CARGAR LIBRERIAS -------------------------------------------------------------
import pandas as pd

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
        self.data = pd.read_csv(file_path)  # Ejemplo de lectura de datos desde un archivo CSV

    def write_data(self, file_path):
        """
        Escribe los datos del objeto Dataset en un archivo.

        Parámetros:
        - file_path: Ruta del archivo donde se guardarán los datos.
        """
        self.data.to_csv(file_path, index=False)  # Ejemplo de escritura de datos a un archivo CSV

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
        if attribute in self.data.columns:
            return self.data[attribute]
        else:
            raise ValueError(f"El atributo '{attribute}' no existe en el conjunto de datos.")

    def set_attribute(self, attribute, values):
        """
        Establece los valores de un atributo específico en el conjunto de datos.

        Parámetros:
        - attribute: Nombre del atributo a establecer.
        - values: Valores a asignar al atributo.

        Excepciones:
        - ValueError: Si el atributo no existe en el conjunto de datos.
        """
        if attribute in self.data.columns:
            self.data[attribute] = values
        else:
            raise ValueError(f"El atributo '{attribute}' no existe en el conjunto de datos.")

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