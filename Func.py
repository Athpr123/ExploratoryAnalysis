import pandas as pd
import numpy as np
from Classwork import Basic_stats

salary = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]

bs = Basic_stats()
b = bs.bs_median(salary)
print(b)

print(bs.bs_outliers(salary))