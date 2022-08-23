"""
A small script to clean the data
"""
import pandas as pd

df = pd.read_csv("./data/raw/census.csv")

clean_df = pd.DataFrame(columns = df.columns)
for index, row in df.iterrows():
    i = 0
    for val in row:

        if val == " ?":
            i = 1
            break
            
    if i == 0:
        clean_df = clean_df.append(row)


clean_df.to_csv("./data/clean/census.csv")
