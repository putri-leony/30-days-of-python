>>> #Higher Order Function
>>> numbers = [1,2,3,4,5]
>>> def square(x):
...     return x**2
...
>>> numbers_squared = map(square, numbers)
>>> print(list(numbers_squared))
[1, 4, 9, 16, 25]
>>> numbers_squared = map(lambda x:x**2, numbers)
>>> print(list(numbers_squared))
[1, 4, 9, 16, 25]
>>> numbers_str = ['1', '2', '3','4', '5']
>>> numbers_int = map(int, numbers_str)
>>> print(list(numbers_int))
[1, 2, 3, 4, 5]
>>> names = ['Linda', 'Joe', 'Jane', 'Doe']
>>> def change_to_upper(name):
...     return name.upper()
...
>>> names_uppercased = map(change_to_upper, names)
>>> print(list(names_uppercased))
['LINDA', 'JOE', 'JANE', 'DOE']
>>> names_uppercased = map(lambda name: name.upper(), names)
>>> print(list(names_uppercased))
['LINDA', 'JOE', 'JANE', 'DOE']
>>> numbers = [1,2,3,4,5]
>>> def is_even(num):
...     if num%2 == 0:
...         return True
...     return False
...
>>> even_numbers = filter(is_even, numbers)
>>> print(list(even_numbers))
[2, 4]
>>> numbers = [1,2,3,4,5]
>>> def is_odd(num):
...     if num%2 != 0:
...         return True
...     return False
...
>>> odd_numbers = filter(is_odd, numbers)
>>> print(list(odd_numbers))
[1, 3, 5]
>>> names = ['Bellinda', 'Chamomile', 'Joe', 'Jane']
>>> def is_name_long(name):
...     if len(name)>3:
...         return True
...     return False
...
>>> long_names = filter(is_name_long, names)
>>> print(list(long_names))
['Bellinda', 'Chamomile', 'Jane']
>>> from functools import reduce
>>> numbers_str = ['1','2','3','4','5']
>>> def add_two_nums(x,y):
...     return int(x)+int(y)
...
>>> total = reduce(add_two_nums, numbers_str)
>>> print(total)
15