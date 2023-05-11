import pandas as pd
from fairness import Fairness

class Disparate_Impact(Fairness):
    def __init__(self) -> None:
        super().__init__()
        
    def check(self, df: pd.DataFrame) -> None:
        y = df.columns[len(df.columns) - 1]
        