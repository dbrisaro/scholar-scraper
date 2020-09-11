import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("out1950-1994.csv")

ax = df.plot.bar(x='year', y='GoogleScholarResults', rot=0)
