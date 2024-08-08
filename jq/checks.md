Find all objects that do **NOT** have the specific property

```
jq '.[]|select( any( has("property_name"); not) )' file.json

```