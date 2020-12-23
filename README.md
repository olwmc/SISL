# SISL
Simple information sectioning language

Fundamentally, there are only two types of statements in SISL
```
A_Type with_a_name and some attributes
```
or
```
A_Type with_a_name and some attributes
:START
and a body!!
:END
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

Statement_1:
  kind = "CODE"
  name = "code_test"
  attr = ["number"]
  body = ['#include <stdio.h>\n', 'int main () { \n', '  int n = $number$;\n', '  print("%d\\n", n); \n', '  return 0; \n', '} \n']
 
Statement_2:
  kind = "Meaning_of_life"
  name = "42"
  attr = None
  body = None

Statement_3:
  kind = "Meaning_of_life"
  name = "100"
  attr = None
  body = None
```


## Example
unit_test_example.py is an example of what you can do. The program takes from the file "testing.txt" and generates and runs unit tests for a class called `Thing`

encyclopedia.py is an example of how you may build a quick and dirty information collection program, maybe for dungeons and dragons or another situation where bulk information is important.
