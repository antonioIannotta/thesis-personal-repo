import pandas as pd
import numpy as np
#from fairness import Fairness

class Disparate_Impact():
    def __init__(self) -> None:
        pass
        
    def check(self, dataset: pd.DataFrame) -> pd.DataFrame:
        sensitive_attributes = return_sensitive_attributes(dataset)
        normalized_dataset = columns_normalization_max_min(dataset, sensitive_attributes)
        return return_disparate_impact(normalized_dataset, sensitive_attributes)
    
    def fairness_evaulation(self, bias_analysis_dataframe: pd.DataFrame):
        return_value = 'unfair'
        for value in bias_analysis_dataframe['Disparate Impact'].values:
            if value < 0.80 or value > 1.25:
                return_value = 'unfair'
            else:
                return_value = 'fair'

        return return_value
        


def return_sensitive_attributes(dataset: pd.DataFrame):
    sensitive_attributes = []

    for attr in dataset.columns[:len(dataset.columns) - 1]:
        unique_values = return_unique_values_for_attribute(attr, dataset)
        if len(unique_values) == 2:
            sensitive_attributes.append(attr)
            unique_values = []
        else:
            unique_values = []
            continue
    
    return sensitive_attributes

def return_unique_values_for_attribute(attribute, dataset: pd.DataFrame):
    unique_values = []
    for value in dataset[attribute][1:].values:
        if not value in unique_values:
            unique_values.append(value)
        else:
            continue
    
    return unique_values
    

def columns_normalization_max_min(dataset: pd.DataFrame, sensitive_attributes):
    for attribute in sensitive_attributes:
        unique_values = return_unique_values_for_attribute(attribute, dataset)
        dataset[attribute].replace({max(unique_values): 1, min(unique_values):0}, inplace=True)

    return dataset

def return_disparate_impact(dataset: pd.DataFrame, sensitive_attributes) -> pd.DataFrame:
    attribute_series = pd.Series(sensitive_attributes)
    disparate_impact_array = []
    for attribute in sensitive_attributes:
        unprivileged_probability = compute_disparate_impact(dataset, attribute, 0, dataset.columns[len(dataset.columns) - 1], 1)
        privileged_probability = compute_disparate_impact(dataset, attribute, 1, dataset.columns[len(dataset.columns) - 1], 1)
        disparate_impact = unprivileged_probability / privileged_probability
        disparate_impact_array.append(disparate_impact)
    
    disparate_impact_series = pd.Series(np.array(disparate_impact_array))
    disparate_impact_dataframe = pd.DataFrame({"Attribute": attribute_series, "Disparate Impact": disparate_impact_series})
    return disparate_impact_dataframe

def compute_disparate_impact(dataset: pd.DataFrame, attribute, attribute_value, output_column, output_value):
    attribute_columns_data = dataset[dataset[attribute] == attribute_value]
    return len(attribute_columns_data[attribute_columns_data[output_column] == output_value])/len(attribute_columns_data)