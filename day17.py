>>> #Exception Handling
>>> try:
...     print(10+'5')
... except:
...     print('Something went wrong')
...
Something went wrong
>>> try:
...     print(10+5)
... except:
...     print('Something went wrong')
...
15
>>> try:
...     name = input('Putri Leony')
...     year_born = 1899
...     age = 2026 - year_born
...     print(f'You are {name}, and your age is {age}.')
... except:
...     print('Something went wrong')
...
Putri Leony
You are , and your age is 127.
>>> try:
...     name = input('Putri Leony')
...     year_born = input('1899')
...     age = 2026 - year_born
...     print(f'You are {name}, and your age is {age}.')
... except:
...     print('Something went wrong')
...
Putri Leony
1899
Something went wrong
>>> try:
...     name = input('Putri Leony')
...     year_born = input('1899')
...     age = 2026 - year_born
...     print(f'You are {name}, and your age is {age}.')
... except TypeError:
...     print('Type error occured')
... except ValueError:
...     print('Value error occured')
... except ZeroDivisionError:
...     print('zero division error occured')
...
Putri Leony
1899
Type error occured
>>> try:
...     name = input('Enter your name:')
...     year_born = input('Born in:')
...     age = 2026 - int(year_born)
...     print(f'You are {name}, and your age is {age}.')
... except TypeError:
...     print('Type error occured')
... except ValueError:
...     print('Value error occured')
... except ZeroDivisionError:
...     print('Zero division error occured')
... else:
...     print('I usually run with the try block')
... finally:
...     print('I always run')
...
Enter your name:Putri Leony
Born in:1899
You are Putri Leony, and your age is 127.
I usually run with the try block
I always run
>>> try:
...     name = input('Enter your name:')
...     year_born = input('Born in:')
...     age = 2026 - int(year_born)
...     print(f'You are {name}, and your age is {age}.')
... except Exception as e:
...     print(e)
...
Enter your name:Putri Leony
Born in:1899
You are Putri Leony, and your age is 127.
>>> #Packing and Unpacking
>>> #Unpacking Lists
>>> def sum_of_five_nums(a,b,c,d,e):
...     return a+b+c+d+e
...
>>> lst = [1,2,3,4,5]
>>> print(sum_of_five_nums(lst))
Traceback (most recent call last):
  File "<python-input-16>", line 1, in <module>
    print(sum_of_five_nums(lst))
          ~~~~~~~~~~~~~~~~^^^^^
TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
>>> def sum_of_five_nums(a,b,c,d,e):
...     return a+b+c+d+e
...
... lst = [1,2,3,4,5]
... print(sum_of_five_nums(*lst))
...
15
>>> numbers = range(2,7)
>>> print(list(numbers))
[2, 3, 4, 5, 6]
>>> args = [2,7]
>>> numbers = range(*args)
>>> print(numbers)
range(2, 7)
>>> countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
>>> fin, sw, nor, *rest = countries
>>> print(fin, sw, nor, rest)
Finland Sweden Norway ['Denmark', 'Iceland']
>>> numbers = [1,2,3,4,5,6,7]
>>> one, *middle, last = numbers
>>> print(one, middle, last)
1 [2, 3, 4, 5, 6] 7
>>> def unpacking_person_info(name, country, age):
...     return f'{name} lives in {country}. She is {age} year old.'
... dct = {'name':'Putri', 'country':'Indonesia', 'age':111}
... print(unpacking_person_info(**dct))
...
Putri lives in Indonesia. She is 111 year old.
>>> #Packing
>>> def sum_all(*args):
...     s=0
...     for i in args:
...         s += i
...     return s
... print(sum_all(1,2,3))
... print(sum_all(1,2,3,4,5,6,7))
...
6
28
>>> def packing_person_info(**kwargs):
...     for key in kwargs:
...         print(f'{key} = {kwargs[key]}')
...     return kwargs
...
>>> print(packing_person_info(name='Putri', country='Indonesia', age=111))
name = Putri
country = Indonesia
age = 111
{'name': 'Putri', 'country': 'Indonesia', 'age': 111}
>>> def packing_person_info(**kwargs):
...     for key,value in kwargs.items():    #using kwargs.items()
...         print(f'{key} : {value}')
...     return kwargs
...
... print(packing_person_info(name='Putri', country='Indonesia', age=111))
...
name : Putri
country : Indonesia
age : 111
{'name': 'Putri', 'country': 'Indonesia', 'age': 111}
>>> #Spreading
>>> lst_one = [1,2,3]
>>> lst_two = [4,5,6,7]
>>> lst = [0, *lst_one, *lst_two]
>>> print(lst)
[0, 1, 2, 3, 4, 5, 6, 7]
>>> #Enumerate
>>> name = ['Julie', 'Victor', 'Amanda', 'Joe']
>>> for index, i in enumerate(name):
...     if i == 'Amanda':
...         print(f'{i} has been found at index {index}')
...
Amanda has been found at index 2
>>> #Zip
>>> fruits = ['banana', 'mango', 'strawberry', 'apple']
>>> vegetables = ['tomato', 'potato', 'spinach', 'kale']
>>> fruits_and_veg = []
>>> for f, v, in zip(fruits, vegetables):
...     fruits_and_veg.append({'fruit':f, 'veg':v})
...
>>> print(fruits_and_veg)
[{'fruit': 'banana', 'veg': 'tomato'}, {'fruit': 'mango', 'veg': 'potato'}, {'fruit': 'strawberry', 'veg': 'spinach'}, {'fruit': 'apple', 'veg': 'kale'}]
>>> name = ['Julie', 'Victor', 'Amanda', 'Joe']
>>> score = [81, 92, 76, 59]
>>> name_and_score = []
>>> for n,s, in zip(name, score):
...     name_and_score.append({'name':n, 'score':s})
...
>>> print(name_and_score)
[{'name': 'Julie', 'score': 81}, {'name': 'Victor', 'score': 92}, {'name': 'Amanda', 'score': 76}, {'name': 'Joe', 'score': 59}]