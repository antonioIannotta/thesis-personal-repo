import unittest
import numpy as np
import pandas as pd
from disparate_impact import return_sensitive_attributes
from disparate_impact import columns_normalization_max_min
from disparate_impact import return_unique_values_for_attribute

class DisparateImpactTest(unittest.TestCase):

    
    
    def test_return_sensitive_attributes(self):
        gender = np.random.randint(0, 2, size=10)
        salary = np.random.randint(1000, 2000, size=10)
        millionaire = np.random.randint(0, 2, size=10)
        y  = np.random.randint(0, 2, size=10)

        example_dataframe = pd.DataFrame({'Gender': pd.Series(gender), 'Salary': pd.Series(salary), 
                                          'Millionaire': pd.Series(millionaire), 'Y': pd.Series(y)})
        sensitive_attributes = return_sensitive_attributes(example_dataframe)
        self.assertEqual(['Gender', 'Millionaire'], sensitive_attributes)


    def test_columns_normalization_max_min(self):
        gender = np.random.randint(2, 4, size=10)
        salary = np.random.randint(1000, 2000, size=10)
        millionaire = np.random.randint(0, 2, size=10)
        y  = np.random.randint(0, 2, size=10)

        example_dataframe = pd.DataFrame({'Gender': pd.Series(gender), 'Salary': pd.Series(salary), 
                                          'Millionaire': pd.Series(millionaire), 'Y': pd.Series(y)})
        
        max_min_normalized_dataset = columns_normalization_max_min(example_dataframe, ['Gender', 'Salary', 'Millionaire'])
        unique_values = return_unique_values_for_attribute('Gender', max_min_normalized_dataset)
        sorted_values_array = unique_values.sort()
        self.assertEqual(0, unique_values[0])
        self.assertEqual(1, unique_values[1])

if __name__ == '__main__':
    unittest.main()