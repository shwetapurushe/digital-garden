Get current time

```
jq -n 'now | strftime("%a %b %d, %Y %Z %H:%M:%S")'
```

Get local time

```
jq -n 'now | localtime | strftime("%a %b %d, %Y %Z %H:%M:%S")
```
