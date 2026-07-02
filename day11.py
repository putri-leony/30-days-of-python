>>> #Function
>>> def generate_full_name():
...     first_name = 'Putri'
...     last_name = 'Leony'
...     space = ' '
...     full_name = first_name+space+last_name
...     print(full_name)
... generate_full_name()
...
Putri Leony
>>> def add_two_numbers():
...     num_one = 2
...     num_two = 3
...     total = num_one+num_two
...     print(total)
... add_two_numbers()
...
5
>>> def add_two_numbers():
...     num_one = 2
...     num_two = 3
...     total = num_one+num_two
...     return total
... print(add_two_numbers())
...
5
>>> def add_ten(num):
...     ten = 10
...     return num + ten
... print(add_ten(90))
...
100
>>> def y(num):
...     number = 111
...     return num+number
... print(y(333))
...
444
>>> def square_number(x):
...     return x*x
... print(square_number(2))
...
4
>>> def area_of_circle(r):
...     phi = 3.14
...     area = phi*r**2
...     return area
... print(area_of_circle(10))
...
314.0
>>> def sum_of_numbers(n):
...     total = 0
...     for i in range(n+1):
...         total+=i
...     return total
... print(sum_of_numbers(10))
...
55
>>> print(sum_of_numbers(100))
5050
>>> def multiplication_of_numbers(n):
...     total = 1
...     for i in range(n+2):
...         total+=i
...     return total
... print(multiplication_of_numbers(10))
...
67
>>> def multiplication_of_numbers(n):
...     initial = 1
...     for i in range (n+2):
...         initial *= i
...     return initial
... print(multiplication_of_numbers(8))
...
0
>>> def multiplication_of_numbers(n):
...     initial = 1
...     for i in range(1,n+1):
...         initial *= i
...     return initial
... print(multiplication_of_numbers(8))
...
40320
>>> def sum (num_one, num_two):
...     sum = num_one + num_two
...     return sum
... print('Sum result:', sum(5,15))
...
Sum result: 20
>>> def weight (mass, gravity):
...     weight = str(mass*gravity)
...     return weight
... print('Weight formula:', weight(100, 9.81))
...
Weight formula: 981.0
>>> #Key and Value
>>> def sum (x, y, z):
...     total = x + y + z
...     return total
... print(sum(x=7, y=10, z=12))
...
29
>>> def is_even (n):
...     if n % 2 == 0:
...         return True
...     return False
... print(is_even(10))
...
True
>>> print(is_even(7))
False
>>>
>>> def find_even_numbers(n):
...     evens = []
...     for i in range (n+1):
...         if i%2 == 0:
...             evens.append(i)
...     return evens
... print(find_even_numbers(10))
...
[0, 2, 4, 6, 8, 10]
>>> def find_odd_numbers(n):
...     odd = []
...     for i in range (n+1):
...         if i%3 == 0:
...             odd.append(i)
...     return odd
... print(find_odd_numbers(30))
...
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
>>> def weight (mass, gravity = 9.81):
...     weight = str(mass*gravity)
...     return weight
... print('Weight in Newton:', weight(100))
...
Weight in Newton: 981.0
>>> print('Weight in Newton:', weight(100, 1.62))
Weight in Newton: 162.0
>>> def sum_all_nums(*nums):
...     total = 0
...     for num in nums:
...         total += num
...     return total
... print(sum_all_nums(90,91,9))
...
190
>>> def generate_groups (team, *args):
...     print(team)
...     for i in args:
...         print(i)
... generate_groups('Team-1', 'John', 'Jane', 'Doe')
...
Team-1
John
Jane
Doe
>>> def greet (name, location):
...     print('Welcome,', name, 'to the land of fantasy', location)
... greet(name = 'Joe', location='Neverland')
...
Welcome, Joe to the land of fantasy Neverland
>>> dictionary = {'name':'Joe', 'location':'Neverland'}
>>> greet(**dictionary)
Welcome, Joe to the land of fantasy Neverland
>>> def square_number (n):
...     return n**n
...
>>> def square_number (n):
...     return n**n
... def function (f,x):
...     return f(x)
... print(function(square_number, 3))
...
27