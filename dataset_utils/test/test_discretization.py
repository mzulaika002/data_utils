from dataset_utils.discretization import *
import unittest
import numpy as np

class TestDiscretizationMethods(unittest.TestCase):

    def test_equal_width_discretization_single_attribute(self):
        attribute_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        num_bins = 3
        expected_discretized_values = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
        discretized_values = equal_width_discretization_single_attribute(attribute_values, num_bins)
        self.assertEqual(discretized_values.tolist(), expected_discretized_values)

    def test_equal_width_discretization_single_attribute_invalid_num_bins(self):
        attribute_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        num_bins = 10
        self.assertRaises(ValueError, equal_width_discretization_single_attribute, attribute_values, num_bins)

    def test_equal_frequency_discretization_single_attribute(self):
        attribute_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        num_bins = 3
        expected_discretized_values = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
        discretized_values = equal_frequency_discretization_single_attribute(attribute_values, num_bins)
        self.assertEqual(discretized_values.tolist(), expected_discretized_values)

    def test_equal_frequency_discretization_single_attribute_invalid_num_bins(self):
        attribute_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        num_bins = 10
        self.assertRaises(ValueError, equal_frequency_discretization_single_attribute, attribute_values, num_bins)

    def test_equal_width_discretization_dataset(self):
        dataset = Dataset()
        dataset.set_attribute('A', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        dataset.set_attribute('B', [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        num_bins = 3
        expected_discretized_dataset = Dataset()
        expected_discretized_dataset.set_attribute('A', [0, 0, 0, 1, 1, 1, 2, 2, 2, 2])
        expected_discretized_dataset.set_attribute('B', [0, 0, 0, 1, 1, 1, 2, 2, 2, 2])
        equal_width_discretization_dataset(dataset, num_bins)
        self.assertEqual(dataset.get_data(), expected_discretized_dataset.get_data())

    def test_equal_frequency_discretization_dataset(self):
        dataset = Dataset()
        dataset.set_attribute('A', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        dataset.set_attribute('B', [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        num_bins = 3
        expected_discretized_dataset = Dataset()
        expected_discretized_dataset.set_attribute('A', [0, 0, 0, 1, 1, 1, 2, 2, 2, 2])
        expected_discretized_dataset.set_attribute('B', [0, 0, 1, 1, 2, 2, 2, 2, 2, 2])
        equal_frequency_discretization_dataset(dataset, num_bins)
        self.assertEqual(dataset.get_data(), expected_discretized_dataset.get_data())

if __name__ == '__main__':
    unittest.main()
