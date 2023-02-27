import pandas as pd
import numpy as np
import seaborn as sb

df = sb.load_dataset("diamonds")

#Number of rows and number of columns
#print(df.shape)

#Print the columns of the data
#print(df.columns)

#Print first n rows of the data
#print(df.head(10))

#Shows the column and datatype
#df.info()

#Prints total number of nulls in each column
#print(df.isnull().sum().sort_values(ascending=False))

#show the summary statistics of the numeric variables
print(df.describe(include="all"))

#corr_matrix = df.corr()
#corr_matrix["price"].sort_values(ascending=False)