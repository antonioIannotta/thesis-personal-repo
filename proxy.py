import pandas as pd
from apyori import apriori

#method to return the list of records of a dataframe needed to the apriori library
def return_list_of_list_for_apriori_library(df: pd.DataFrame):
    records = []
    for i in range(0, len(df)):
        records.append([str(df.values[i, j]) for j in range(0, len(df.columns))])
    return records

#method to return the association results
def return_association_results(df: pd.DataFrame):
    records = return_list_of_list_for_apriori_library(df)
    association_rules = apriori(records, min_support=0.0045, min_confidence=0.5, min_lift=3, min_length=2)
    return list(association_rules)