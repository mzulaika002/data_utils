import unittest
import pandas as pd
from dataset_utils.dataset import *


class TestDataset(unittest.TestCase):
    def setUp(self):
        # Create a sample dataset for testing
        data = {
            'Name': ['John', 'Alice', 'Bob'],
            'Age': [25, 30, 35],
            'City': ['New York', 'Paris', 'London']
        }
        self.dataset = Dataset(data=pd.DataFrame(data))

    def test_read_data(self):
        # Test reading data from a file
        file_path = '/home/mz/Mahaigaina/KISA/SME/Python/datasets/Student_bucketing.csv'
        self.dataset.read_data(file_path)
        print(len(self.dataset.data))
        #self.assertEqual(len(self.dataset.data), 3)  # Check if data is loaded correctly

    def test_write_data(self):
        # Test writing data to a file
        file_path = '/home/mz/Mahaigaina/KISA/SME/Python/datasets/Student_bucketing.csv'
        self.dataset.write_data(file_path)
        loaded_data = pd.read_csv(file_path)
        self.assertEqual(len(loaded_data), 3)  # Check if data is written correctly

    def test_get_attribute(self):
        # Test getting attribute values
        attribute = 'Age'
        attribute_values = self.dataset.get_attribute(attribute)
        expected_values = pd.Series([25, 30, 35])
        pd.testing.assert_series_equal(attribute_values, expected_values)  # Check if attribute values match

        # Test getting non-existing attribute
        non_existing_attribute = 'Salary'
        with self.assertRaises(ValueError):
            self.dataset.get_attribute(non_existing_attribute)

    def test_set_attribute(self):
        # Test setting attribute values
        attribute = 'City'
        new_values = ['Tokyo', 'Berlin', 'Sydney']
        self.dataset.set_attribute(attribute, new_values)
        updated_attribute_values = self.dataset.get_attribute(attribute)
        expected_values = pd.Series(new_values)
        pd.testing.assert_series_equal(updated_attribute_values, expected_values)  # Check if attribute values are updated

        # Test setting values for non-existing attribute
        non_existing_attribute = 'Salary'
        with self.assertRaises(ValueError):
            self.dataset.set_attribute(non_existing_attribute, [50000, 60000, 70000])

    def test_get_attributes(self):
        # Test getting attribute names
        attributes = self.dataset.get_attributes()
        expected_attributes = ['Name', 'Age', 'City']
        self.assertListEqual(attributes, expected_attributes)  # Check if attribute names match

    def test_get_data(self):
        # Test getting the DataFrame representing the data
        data = self.dataset.get_data()
        self.assertTrue(isinstance(data, pd.DataFrame))  # Check if the returned object is a DataFrame


if __name__ == '__main__':
    unittest.main()
