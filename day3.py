#Arithmetic Operations in Python
>>> print('Addition:', 1+2)
Addition: 3
>>> print('substraction:', 2-1)
substraction: 1
>>> print('multiplication:', 2*3)
multiplication: 6
>>> print('division:', 6/2)
division: 3.0
>>> print('division:', 7/5)
division: 1.4
>>> print('division:', 7//5)
division: 1
>>> print('modulus:', 3%2)
modulus: 1
>>> print('exponentiation:', 2**3)
exponentiation: 8
>>> #Example: Floating Numbers
>>> print('Floating Number, phi:', 3.14)
Floating Number, phi: 3.14
>>> print('Floating Number, gravity:', 9.81)
Floating Number, gravity: 9.81
>>> #Example: complex number
>>> print('Complex Number:', 1+1j)
Complex Number: (1+1j)
>>> print('multiplying complex number:', (1+1j)*(1-1j))
multiplying complex number: (2+0j)
>>> #Example of Variable
>>> a = 3
>>> b = 2
>>> total = a+b
>>> diff = a-b
>>> product = a*b
>>> division = a/b
>>> remainder = a%b
>>> floor_division = a//b
>>> exponential = a**b
>>> print (total)
5
>>> print(diff)
1
>>> print(product)
6
>>> print(division)
1.5
>>> print(remainder)
1
>>> print(floor_division)
1
>>> print(exponential)
9
>>> #Calculating area of a circle
>>> radius = 10
>>> circle_area = 3.14*radius**2
>>> print('Area of a circle:', circle_area)
Area of a circle: 314.0
>>> #Calculating Area of a Rectangle
>>> length = 10
>>> width = 20
>>> rectangle_area = length*width
>>> print('Area of a rectangle:', rectangle_area)
Area of a rectangle: 200
>>> #Calculating a weight of an object
>>> mass = 75
>>> gravity = 9.81
>>> weight = mass*gravity
>>> print('weight:', weight)
weight: 735.75
>>> #Calculating the density of a liquid
>>> mass = 75
>>> volume = 0.075
>>> density = mass/volume
>>> print(density, 'kg/m^3')
1000.0 kg/m^3
>>> #Comparison Operators
>>> print(3>2)
True
>>> print(3>=2)
True
>>> print(3<2)
False
>>> print(2<3)
True
>>> print(2<=3)
True
>>> print(3 == 2)
False
>>> print(3!=2)
True
>>> print(len('mango') == len('avocado'))
False
>>> print(len('milk') == len ('meat'))
True
>>> print(len('milk') != len ('meat'))
False
>>> print(len('onion') < len('spinach'))
True
>>> print(len('avocado') > len('apple'))
True
>>> print(len('avocado'))
7
>>> print('P in Putri', 'P' in 'Putri')
P in Putri True
>>> print('T not in Putri', 'T' in 'Putri')
T not in Putri False
>>> print('T' in 'Putri')
False
>>> print('lazy' in 'i am diligent')
False
>>> print('4 is 2**2', 4 == 2**2)
4 is 2**2 True
>>> print(3>2 and 4>3)
True
>>> print(3>2 and 4<3)
False
>>> print(3>2 or 4>3)
True
>>> print(3>2 or 4<3)
True
>>> print(3<2 or 4<3)
False
>>> print(not 3>2)
False
>>> print(not True)
False
>>> print(not False)
True
>>> print(not not True)
True
>>> print(not not False)
False
>>> #Exercise 1
>>> base = 20
>>> height = 10
>>> triangle_area = 0.5*base*height
>>> print('Area of a triangle:', triangle_area)
Area of a triangle: 100.0
>>> #Exercise 2
>>> length = 15
>>> width = 10
>>> area = length*width
>>> perimeter = 2*length*width
>>> print('Area of rectangle:', area)
Area of rectangle: 150
>>> print('Perimeter of rectangle:', perimeter)
Perimeter of rectangle: 300
>>> y = '2x-2'
>>> m = 2
>>> c = -2
>>> slope = m
>>> y_intercept = c
>>> x_intercept = -c/m
>>> print('slope:', slope)
slope: 2
>>> print('y intercept:', y_intercept)
y intercept: -2
>>> print('x intercept:', x_intercept)
x intercept: 1.0
>>> print('y intercept:', (0,y_intercept))
y intercept: (0, -2)
>>> print('x intercept:', (x_intercept,0))
x intercept: (1.0, 0)
>>> #Exercise 4
>>> m = 'y2-y2/x2-x1'
>>> 'Point: (2,2) (6,10)'
'Point: (2,2) (6,10)'
>>> #Point (2,2) (6,10)
>>> m = (10-2)/(6-2)
>>> print('slope:', m)
slope: 2.0
>>> euclidean_dist = 'sqrt of ((p1-q1)^2+(p2-q2)^2)'
>>> euclidean_dist = ((2-6)**2+(2-10)**2)**0.5
>>> print('Euclidean Distance:', euclidean_dist)
Euclidean Distance: 8.94427190999916
>>> #Exercise 5
>>> def calculate_y(x):
...     return x**2+6*x+9
...
>>> x_values = [-3, -2, -1, 0, 1, 2, 3]
>>> print('x | y')
x | y
>>> print('------')
------
>>> for x in x_values:
...     y = calculate_y(x)
...     print(f'{x:2d} | {y:2d}')
...
-3 |  0
-2 |  1
-1 |  4
 0 |  9
 1 | 16
 2 | 25
 3 | 36
>>> #Exercise 6
>>> print(len('python') == ('dragon'))
False
>>> print(len('python') == len('dragon'))
True
>>> print(len('python') != len('dragon'))
False
>>> len_python = len('python')
>>> float_python = float(len('python'))
>>> str_python = str(float_python)
>>> print('Length of python:', len_python)
Length of python: 6
>>> print('Float python:', float_python)
Float python: 6.0
>>> print('String python:', str_python)
String python: 6.0