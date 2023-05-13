import pandas as pd
import numpy as np
import sklearn as skl
from fairness import Fairness

df = pd.read_excel('./dataset/default of credit card clients.xls')

fairness = Fairness()

fairness.check_for_bias(df, "disparate_impact")
