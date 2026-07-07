>>> #Python Error Types
>>> #Syntax Error
>>> print 'hello world'
  File "<python-input-2>", line 1
    print 'hello world'
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print(hello world)
  File "<python-input-3>", line 1
    print(hello world)
          ^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('hello world')
hello world

#Name Error
>>> print(age)
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    print(age)
          ^^^
NameError: name 'age' is not defined
>>> age = 111
>>> print(age)
111

#Index Error
>>> numbers = [1,2,3,4,5]
>>> numbers[5]
Traceback (most recent call last):
  File "<python-input-9>", line 1, in <module>
    numbers[5]
    ~~~~~~~^^^
IndexError: list index out of range
>>> numbers[4]
5

#Module Not Found Error
>>> import maths
Traceback (most recent call last):
  File "<python-input-10>", line 1, in <module>
    import maths
ModuleNotFoundError: No module named 'maths'

#Attribute Error
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<python-input-14>", line 1, in <module>
    math.PI
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
>>> math.pi
3.141592653589793

#Key Error
>>> data = {'name': 'Jane Doe', 'age':'unknown', 'country':'Canada'}
>>> data['name']
'Jane Doe'
>>> data['county']
Traceback (most recent call last):
  File "<python-input-19>", line 1, in <module>
    data['county']
    ~~~~^^^^^^^^^^
KeyError: 'county'
>>> data['country']
'Canada'

#Type Error
>>> 4 + '3'
Traceback (most recent call last):
  File "<python-input-21>", line 1, in <module>
    4 + '3'
    ~~^~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0

#Import Error
>>> from math import power
Traceback (most recent call last):
  File "<python-input-24>", line 1, in <module>
    from math import power
ImportError: cannot import name 'power' from 'math' (unknown location)
>>> from math import pow
>>> pow(2,3)
8.0

#Value Error
>>> int('12a')
Traceback (most recent call last):
  File "<python-input-27>", line 1, in <module>
    int('12a')
    ~~~^^^^^^^
ValueError: invalid literal for int() with base 10: '12a'

#Zero Division Error
>>> 1/0
Traceback (most recent call last):
  File "<python-input-28>", line 1, in <module>
    1/0
    ~^~
ZeroDivisionError: division by zero