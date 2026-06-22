>>> #Create a String
>>> letter = 'P'
>>> print(letter)
P
>>> print(len(letter))
1
>>> greeting = 'Hello World!'
>>> print(greeting)
Hello World!
>>> print(len(greeting))
12
>>> multiline_string = '''I love to eat read and sleep. My dream is to travel the world\
. I like to learn something new.'''
>>> print(multiline_string)
I love to eat read and sleep. My dream is to travel the world. I like to learn something new.
>>> #Connect String (concatenation)
>>> first_name = 'Putri'
>>> last_name = 'Leony'
>>> space = ' '
>>> full_name = first_name+space+last_name
>>> print(full_name)
Putri Leony
>>> print(len(first_name))
5
>>> print(len(last_name))
5
>>> print(len(first_name) > len(last_name))
False
>>> print(len(full_name))
11
>>> #Escape Sequences in Strings
>>> print('I am fine. \n And you?')
I am fine.
 And you?
>>> print('Days\tTopics\tExercises')
Days    Topics  Exercises
>>> print('Day 1\t5\t5')
Day 1   5       5
>>> print('Day 2\\t5\\t5')
Day 2\t5\t5
>>> print('Days\tTopics\tExercises\nDay 1\t5\t5')
Days    Topics  Exercises
Day 1   5       5
>>> print('days\tTopics\tExercises\nDay 1\t5\t5\nDay 2\t6\t20\nDay 3\t5\t23')
days    Topics  Exercises
Day 1   5       5
Day 2   6       20
Day 3   5       23
>>> #String Formatting
>>> first_name = 'Putri'
>>> last_name = 'Leony'
>>> language = 'Python'
>>> formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
>>> print(formated_string)
I am Putri Leony. I teach Python
>>> first_thing = 'caffeine'
>>> second_thing = 'sleep'
>>> formated_string = 'I am addicted to %s, even though I need %s' %(first_thing, secon\
d_thing)
>>> print(formated_string)
I am addicted to caffeine, even though I need sleep
>>> radius = 10
>>> phi = 3.14
>>> area = phi*radius**2
>>> formated_string = 'The area of a circle with radius equals to %d is %f' %(radius, a\
rea)
>>> print(formated_string)
The area of a circle with radius equals to 10 is 314.000000
>>> formated_string2 = 'The area of a circle with radius equals to %d is %.2f.' %(radiu\
s, area)
>>> print(formated_string2)
The area of a circle with radius equals to 10 is 314.00.
>>> lists_example = ['Mango', 'Apple', 'Banana']
>>> formated_string = 'The following are example of lists: %s.' %(lists_example)
>>> print(formated_string)
The following are example of lists: ['Mango', 'Apple', 'Banana'].
>>> #New String Formatting
>>> first_name = 'Putri'
>>> last_name = 'Leony'
>>> language = 'Python'
>>> formated_string = 'I am {} {}. I am currently still learning {}'.format(first_name,\
 last_name, language)
>>> print(formated_string)
I am Putri Leony. I am currently still learning Python
>>> formated_string = 'I am {} {}. I am currently still learning {}.'.format(first_name\
, last_name, language)
>>> print(formated_string)
I am Putri Leony. I am currently still learning Python.
>>> a = 4
>>> b = 3
>>> print('{} + {} = {}'.format(a, b, a+b))
4 + 3 = 7
>>> print('{} - {} = {}'.format(a, b, a-b))
4 - 3 = 1
>>> print('{} * {} = {}'.format(a, b, a*b))
4 * 3 = 12
>>> print('{} % {} = {}'. format(a, b, a%b))
4 % 3 = 1
>>> radius = 10
>>> phi = 3.14
>>> area = phi*radius**2
>>> formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius,\
area)
>>> print(formated_string)
The area of a circle with a radius 10 is 314.00.
>>> #String Interpolation
>>> a = 4
>>> b = 3
>>> print(f'{a}+{b} = {a+b}')
4+3 = 7
>>> print(f'{a}**{b} = {a**b}')
4**3 = 64
>>> #Unpacking Characters
>>> language = 'Python'
>>> a,b,c,d,e,f = language
>>> print(a)
P
>>> print(b)
y
>>> print(c)
t
>>> print(d)
h
>>> print(e)
o
>>> print(f)
n
>>> print(a,b,c,d,e,f)
P y t h o n
>>> language = 'Python'
>>> first_letter = language[0]
>>> print(first_letter)
P
>>> second_letter = language[1]
>>> print(second_letter)
y
>>> last_index = len(language)
>>> last_letter = language[last_index]
Traceback (most recent call last):
  File "<python-input-90>", line 1, in <module>
    last_letter = language[last_index]
                  ~~~~~~~~^^^^^^^^^^^^
IndexError: string index out of range
>>> last_index = len(language) - 1
>>> last_letter = language[last_index]
>>> print(last_letter)
n
>>> language = 'Python'
>>> last_letter = language [-1]
>>> print(last_letter)
n
>>> second_last = language[-2]
>>> print(second_last)
o
>>> language = 'English'
>>> first_three = language[0:3]
>>> print(first_three)
Eng
>>> last_four = language[3:7]
>>> print(last_four)
lish
>>> last_three = language[-3:]
>>> print(last_three)
ish
>>> last_three = language[3:]
>>> print(last_three)
lish
>>> #Reversing a String
>>> greeting = 'Hello, World!'
>>> print(greeting[::-1])
!dlroW ,olleH
>>> print(greeting[4::-1])
olleH
>>> #Skipping Characters
>>> language = 'Python'
>>> pto = language[0:6:2]
>>> print(pto)
Pto
>>> yhn = language[1:6:2]
>>> print(yhn)
yhn