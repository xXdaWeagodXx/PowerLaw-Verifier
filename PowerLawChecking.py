import pandas as pd
import numpy as np
import powerlaw as pl

## Put the data as csv file in the same folder as this code and name it 'data_1.csv'
## read data from csv(excel) file and store in a pandas dataframe
## convert pandas dataframe to a one dimentional list by Numpy array and store in DATA1


df = pd.read_csv("data_1.csv")
DATA1 = np.array(df['a'].tolist())
print (DATA1)

results = pl.Fit(DATA1); 
print (results.power_law.alpha)
print (results.power_law.xmin)

R, p = results.distribution_compare('power_law', 'lognormal')

print ("R = " + str(R))
print ("p = " + str(p))

