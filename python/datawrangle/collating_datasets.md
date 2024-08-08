<h4>Load a bunch of files into a single dataset using pandas</h4>

```
import pandas as pd
import os

path = os.getcwd()
extension = '.tsv'

files = [f for f in os.listdir(path) if f.endswith(extension)]

dfs = []
for file in files:
    df = pd.read_csv(file, sep='\t')
    dfs.append(df)

final_df = pd.concat(dfs, ignore_index=True)

final_df.to_csv('name.csv', index=False)

```