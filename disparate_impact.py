import pandas as pd
import numpy as np
#from fairness import Fairness

class Disparate_Impact():
    def __init__(self) -> None:
        pass
        
    def check(self, df: pd.DataFrame) -> pd.DataFrame:
        sensitive_attributes = return_sensitive_attributes(df)
        normalized_df = columns_normalization_max_min(df, sensitive_attributes)
        return return_disparate_impact(normalized_df, sensitive_attributes)
        


def return_sensitive_attributes(df: pd.DataFrame):
    sensitive_attributes = []

    for attr in df.columns[:len(df.columns) - 1]:
        unique_values = return_unique_values_for_attribute(attr, df)
        if len(unique_values) == 2:
            sensitive_attributes.append(attr)
            unique_values = []
        else:
            unique_values = []
            continue
    
    return sensitive_attributes

def return_unique_values_for_attribute(attr, df: pd.DataFrame):
    unique_values = []
    for value in df[attr][1:].values:
        if not value in unique_values:
            unique_values.append(value)
        else:
            continue
    
    return unique_values
    

def columns_normalization_max_min(df: pd.DataFrame, sensitive_attributes):
    for attr in sensitive_attributes:
        unique_values = return_unique_values_for_attribute(attr, df)
        df[attr].replace({max(unique_values): 1, min(unique_values):0}, inplace=True)

    return df

def return_disparate_impact(df: pd.DataFrame, sensitive_attributes) -> pd.DataFrame:
    #disparate_impact_dataframe = pd.DataFrame(columns=["Attribute", "Disparate Impact"])
    attr_series = pd.Series(sensitive_attributes)
    di_array = []
    for attribute in sensitive_attributes:
        pr_unpriv = compute_di(df, attribute, 0, df.columns[len(df.columns) - 1], 1)
        pr_priv = compute_di(df, attribute, 1, df.columns[len(df.columns) - 1], 1)
        di = pr_unpriv / pr_priv
        di_array.append(di)
        #disparate_impact_dataframe = disparate_impact_dataframe.append({attribute: pr_unpriv / pr_priv}, ignore_index=True)
    
    di_series = pd.Series(np.array(di_array))
    disparate_impact_dataframe = pd.DataFrame({"Attribute": attr_series, "Disparate Impact": di_series})
    return disparate_impact_dataframe

def compute_di(df: pd.DataFrame, attribute, attr_value, output_col, output_value):
    attribute_columns_data = df[df[attribute] == attr_value]
    return len(attribute_columns_data[attribute_columns_data[output_col] == output_value])/len(attribute_columns_data)