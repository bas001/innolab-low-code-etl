# Magic Rules Generator
Javascript generator from magic-rule files running in Flask server.

```
python -m flask run*
```

##Endpoint


```
HTTP POST /convert
Content-Type: text/plain

name: ExampleRule
action: concat
attributes: first : String, last: String -> name : String
options: " "
```