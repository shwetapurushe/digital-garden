<h4>Word distribution from pandas series</h4>
```df['asn'].str.split(expand=True).stack().value_counts()```
