<h3>Collapses corresponding keys within multiple json objects into one.</h3>
Useful for log files.

one.json
```
{
  "clientip": {
    "occurrence": {
      "193.191.124.34": 67383,
      "92.58.111.16": 43382
    }
  }
}
```
two.json
```
{
    "clientip": {
        "occurrence": {
            "130.345.134.17": 21896,
            "88.174.96.78": 21130
        }
    }
}
```

```jq '.'  *.json | jq -n 'reduce inputs as $item ({}; . *= $item)'```

final output
```

{
  "clientip": {
    "occurrence": {
      "193.191.124.34": 67383,
      "92.58.111.16": 43382,
     "130.345.134.17": 21896,
      "88.174.96.78": 21130
    }
  }
}
```


