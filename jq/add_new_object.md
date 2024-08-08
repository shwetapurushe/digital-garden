<h3>adds objects to the main object</h3>
one.json

```
{
  "clientip": {
    "occurrence": {
      "193.331.124.34": 67383,
      "92.33.111.16": 43382
    }
  }
}
```

```
test=200  
test=1000  
```


```jq --argjson year "$test" --argjson y "$test2" '.clientip += $ARGS.named' one.json```

output
```
{
  "clientip": {
    "occurrence": {
      "193.191.134.34": 67383,
      "92.58.171.16": 43382
    },
    "year": 200,
    "y": 1000
  }
}
```