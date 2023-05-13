import pandas as pd
import numpy as np
from unbalanced_dataset import Unbalanced_Dataset
from prevalence import Prevalence
from equal_opportunity import Equal_Opportunity
from equalized_odds import Equalized_Odds
from disparate_impact import Disparate_Impact

list_metric = ["unbalanced_dataset", "prevalence", "equal_opportunity", "equalized_odds", "disparate_impact"]

class Fairness:
    def __init__(self) -> None:
        pass
        
    def check(self, df: pd.DataFrame) -> None:
        pass

     
    def check_for_bias(self, df: pd.DataFrame, metric):
        fairness_metric = return_fairness_metric(metric)
        fairness_metric_obj = fairness_metric()
        fairness_metric_obj.check(df)


def return_fairness_metric(self, metric):
    match metric:
        case "unbalanced_dataset":
            return Unbalanced_Dataset
        case "prevalence":
            return Prevalence
        case "equal_opportunity":
            return Equal_Opportunity
        case "equalized_odds":
            return Equalized_Odds
        case "disparate_impact":
            return Disparate_Impact