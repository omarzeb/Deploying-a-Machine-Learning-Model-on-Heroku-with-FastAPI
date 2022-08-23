"""
A small script to clean the data
"""
import pandas as pd
import sys
df = pd.read_csv(sys.path[0] + '/../data/raw/census.csv')

clean_df = pd.DataFrame(columns = df.columns)
for index, row in df.iterrows():
    i = 0
    for val in row:

        if val == " ?":
            i = 1
            break
            
    if i == 0:
        clean_df = clean_df.append(row)


clean_df.dropna(inplace=True)
clean_df.drop_duplicates(inplace=True)
clean_df.drop(" education-num", axis=1, inplace=True)
clean_df.drop(" capital-gain", axis=1, inplace=True)
clean_df.drop(" capital-loss", axis=1, inplace=True)

clean_df.to_csv(sys.path[0] + "/../data/clean/census.csv")
