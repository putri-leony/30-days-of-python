#Module
#Create a mymodule.py file
def generate_full_name(firstname, lastname):
    space = ' '
    fullname = firstname + space + lastname
    return fullname

def sum_two_nums (num1, num2):
    return num1 + num2
gravity = 9.81
person = {'firstname':'Putri', 'age':99, 'city':'Neverland'}
#Create a main.py file
import mymodule
print(mymodule.generate_full_name('Putri', 'Leony'))
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Putri', 'Leony'))
#Results: (after Running the main.py file)
Putri Leony
Putri Leony #twice because I printed it twice

from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Putri', 'Leony'))
print(sum_two_nums(1,9))
mass = 100
weight = mass*gravity
print(weight)
print(person['firstname'])
#Results: (after Running the main.py file)
Putri Leony
10
981.0
Putri

#Renaming the Module
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Putri','Leony'))
print(total(1,999))
mass = 99
weight = mass*g
print(weight)
print(p)
print(p['firstname'])
#Results: (after Running the main.py file)
Putri Leony
1000
971.19
{'firstname': 'Putri', 'age': 99, 'city': 'Neverland'}
Putri

#Import Built-in Modules
>>> import os
>>> os.mkdir('newfolder')
>>> print(os.getcwd())
C:\Users\sipul\Downloads #I previously changed the directory to Downloads
>>> os.rmdir('newfolder') #to delete the folder

#Sys Module
#Create a script.py file
import sys
print('Welcome {}. Enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))
#Open Command Prompt, navigate to the folder where the script.py file is located, and run the following command:
python script.py Putri 30DaysofPython
#Results:
Welcome Putri. Enjoy 30DaysofPython challenge!

#sys commands (written in new file)
import sys
print(sys.version)
print(sys.maxsize)
print(sys.path)
sys.exit()
#Results:
3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)]
9223372036854775807
['C:/Users/sipul/Downloads', 'C:\\Users\\sipul\\OneDrive\\Documents', 'C:\\Users\\sipul\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\idlelib', 'C:\\Users\\sipul\\AppData\\Local\\Python\\pythoncore-3.14-64\\python314.zip', 'C:\\Users\\sipul\\AppData\\Local\\Python\\pythoncore-3.14-64\\DLLs', 'C:\\Users\\sipul\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib', 'C:\\Users\\sipul\\AppData\\Local\\Python\\pythoncore-3.14-64', 'C:\\Users\\sipul\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages']

#Statistics Module
>>> from statistics import *
>>> ages = [20,20,4,24,22,25,26,20,23]
>>> print(mean(ages))
20.444444444444443
>>> print(median(ages))
22
>>> print(mode(ages))
20
>>> print(stdev(ages))
6.559556218051475

#Math Module
>>> import math
>>> print(math.pi)
3.141592653589793
>>> print(math.sqrt(2))
1.4142135623730951
>>> print(math.pow(2,3)) #exponential
8.0
>>> print(math.floor(9.81)) #rounding to the lowest
9
>>> print(math.ceil(9.81)) #rounding to the highest
10
>>> print(math.log10(100))
2.0
>>> from math import pi, sqrt, pow, floor, ceil, log10
>>> print(pi)
3.141592653589793
>>> print(sqrt(2))
1.4142135623730951
>>> print(pow(2,3))
8.0
>>> print(floor(9.81))
9
>>> print(ceil(9.81))
10
>>> print(log10(100))
2.0
>>> from math import *
>>> print(pi)
3.141592653589793
>>> print(sqrt(2))
1.4142135623730951
>>> print(pow(2,3))
8.0
>>> print(floor(9.81))
9
>>> print(ceil(9.81))
10
>>> print(log10(100))
2.0
>>> from math import pi as PHI
>>> print(PHI)
3.141592653589793

#String Module
>>> import string
>>> print(string.ascii_letters)
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
>>> print(string.digits)
0123456789
>>> print(string.punctuation)
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

#Random Module
>>> from random import random, randint
>>> print(random())
0.4481220314454051
>>> print(randint(5,20))
8

#Exercise 1
import random
import string
def random_id():
    characters = string.ascii_letters + string.digits
    random_char = random.choices(characters, k=6)
    final_id =''.join(random_char)
    return final_id
print(random_id())
#Results:
skTKn4

#Exercise 2
import random
import string
def modified_id():
    characters = string.ascii_letters + string.digits
    length_of_id = int(input('length:'))
    total_of_id = int(input('total:'))
    result_id = []
    for i in range(total_of_id):
        random_char = random.choices(characters, k=length_of_id)
        final_id = ''.join(random_char)
        result_id.append(final_id)
    return '\n'.join(result_id)
print(modified_id())
#Results:
length:5 #(input from user)
total:5 #(input from user)
LGRVn
mbhLG
R0RhG
djdH5
Kv4pm

#Exercise 3
import random
def rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_result = f'rgb({r},{g},{b})'
    return rgb_result
print(rgb_color())
#Results:
rgb(17,184,204)