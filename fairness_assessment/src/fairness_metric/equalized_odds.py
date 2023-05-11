import pandas as pd
from fairness import Fairness

class Equalized_Odds(Fairness):
    def __init__(self) -> None:
        super().__init__()
        
    def check(self, df: pd.DataFrame) -> None:
        pass