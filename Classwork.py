import numpy as np
import matplotlib.pyplot as plt

class Basic_stats():
    def __init__(self):
        pass

    def bs_median(self,bs_value):
        n = len(bs_value)
        bs_value.sort()
        if n % 2 == 0:
            median1 = bs_value[n//2]
            median2 = bs_value[n//2 - 1]
            median = (median1 + median2)/2
        else:
            median = bs_value[n//2]
        return median

    def bs_spread(self,bs_value):
        a = np.percentile(bs_value,25)
        b = np.percentile(bs_value,75)
        c = b-a
        return c

    def bs_outliers(self, bs_value):
        a = np.percentile(bs_value,25)
        b = np.percentile(bs_value,75)
        c = b-a
        Q1 = a - 1.5*c
        Q2 = b + 1.5*c
        length = bs_value.count()
        
        for i in length:
            if(bs_value[i]>Q2 or bs_value[i]<Q1):
                return bs_value[i]
    
    def bs_boxplot(self, bs_value):
        plt.boxplot(bs_value)
        plt.show()