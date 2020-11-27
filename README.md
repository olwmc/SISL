# SISL
Simple information sectioning language

Takes information in the form

```
# Comment
TYPE name attribute1 attribute2
:START
Here is the inside of the body
This area is plaintext
:END
```

Or, without a body
```
TYPE NAME ATTR1 ATTR2
```

An example
```
Meaning_of_life 42
Meaning_of_life 100

CODE code_test number
:START
#include <stdio.h>
int main () { 
  int n = $number$;
  print("%d\n", n); 
  return 0; 
} 
:END
```

The program returns a python dictionary

```python
{"CODE": [Statement_1],
 "Meaning_of_life": [Statement_2, Statement_3]}

Statement:
  kind = "CODE"
  name = "code_test"
  attr = ["number"]
  body = ['#include <stdio.h>\n', 'int main () { \n', '  int n = $number$;\n', '  print("%d\\n", n); \n', '  return 0; \n', '} \n']
 
Statement:
  kind = "Meaning_of_life"
  name = "42"
  attr = None
  body = None

Statement:
  kind = "Meaning_of_life"
  name = "100"
  attr = None
  body = None
```
