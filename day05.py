>>> #Create a List
>>> lst_function_1 = list()
>>> print(len(lst_function_1))
0
>>> lst_function_2 = []
>>> print(len(lst_function_2))
0
>>> country_in_asia = ['Indonesia', 'China', 'India', 'Malaysia']
>>> print('Country in Asia', len(country_in_asia))
Country in Asia 4
>>> print('Country in Asia:', len(country_in_asia))
Country in Asia: 4
>>> #Accessing List Items Using Indexing
>>> fruits = ['apple', 'orange', 'banana']
>>> first_fruit = fruits[0]
>>> print(first_fruit)
apple
>>> second_fruit = fruits[1]
>>> print(second_fruit)
orange
>>> #negative index
>>> last_fruit = fruits[-1]
>>> print(last_fruit)
banana
>>> lst = ['item1', 'item2', 'item3', 'item4', 'item5']
>>> first_item, second_item, third_item, *rest = lst
>>> print(first_item)
item1
>>> print(second_item)
item2
>>> print(third_item)
item3
>>> print(rest)
['item4', 'item5']
>>> first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
>>> print(first)
1
>>> print(third)
3
>>> print(rest)
[4, 5, 6, 7, 8, 9]
>>> print(tenth)
10
>>> countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', '\
Finland', 'Norway', 'Iceland', 'Estonia']
>>> gr, fr, bg, sw, *scandic, es = countries
>>> print(gr)
Germany
>>> print(fr)
France
>>> print(scandic)
['Denmark', 'Finland', 'Norway', 'Iceland']
>>> print(es)
Estonia
>>> #Slicing Items from a List
>>> fruits = ['banana', 'apple', 'watermelon']
>>> all_fruits = fruits[0:3]
>>> all_fruits = fruits[0:]
>>> apple_and_watermelon = fruits[1:3]
>>> banana_apple_watermelon = fruits[0:]
>>> fruits = ['banana', 'apple', 'watermelon', 'lemon']
>>> all_fruits = fruits[-4]
>>> apple_and_watermelon = fruits[-3:-1]
>>> apple_watermelon_lemon = fruits[-3:]
>>> reverse_fruits = fruits[::-1]
>>> print(all_fruits)
banana
>>> all_fruits = fruits[-4:]
>>> print(all_fruits)
['banana', 'apple', 'watermelon', 'lemon']
>>> #Modifying Lists
>>> vegetables = ['spinach', 'kale', 'lettuce', 'cucumber']
>>> vegetables[0] = 'cabbage'
>>> print(vegetables)
['cabbage', 'kale', 'lettuce', 'cucumber']
>>> vegetables[1] = 'green beans'
>>> print(vegetables)
['cabbage', 'green beans', 'lettuce', 'cucumber']
>>> last_index = len(vegetables)
>>> last_index = len(vegetables) - 1
>>> vegetables[last_index] = 'spinach'
>>> print(vegetables)
['cabbage', 'green beans', 'lettuce', 'spinach']
>>> vegetables[last_index] = 'kale'
>>> print(vegetables)
['cabbage', 'green beans', 'lettuce', 'kale']
>>> last_index = len(vegetables)
>>> vegetables[last_index] = 'spinach'
Traceback (most recent call last):
  File "<python-input-61>", line 1, in <module>
    vegetables[last_index] = 'spinach'
    ~~~~~~~~~~^^^^^^^^^^^^
IndexError: list assignment index out of range
>>> #Checking Items in a List
>>> fruits = ['orange', 'pineapple', 'watermelon', 'apple']
>>> does_exist = 'banana'
>>> print(does_exist)
banana
>>> does_exist = 'banana' in fruits
>>> print(does_exist)
False
>>> does_exist = 'pineapple' in fruits
>>> print(does_exist)
True
>>> #Adding Items to a List
>>> fruits = ['orange', 'pineapple', 'watermelon', 'apple']
>>> fruits.append('lemon')
>>> print(fruits)
['orange', 'pineapple', 'watermelon', 'apple', 'lemon']
>>> fruits.append('lime')
>>> print(fruits)
['orange', 'pineapple', 'watermelon', 'apple', 'lemon', 'lime']
>>> #Inserting Items into a List
>>> fruits = ['orange', 'pineapple', 'watermelon', 'apple']
>>> fruits.insert(2, 'lemon')
>>> print(fruits)
['orange', 'pineapple', 'lemon', 'watermelon', 'apple']
>>> fruits.insert(3, 'lime')
>>> print(fruits)
['orange', 'pineapple', 'lemon', 'lime', 'watermelon', 'apple']
>>> #Removing Items from a List
>>> fruits = ['orange', 'pineapple', 'watermelon', 'apple']
>>> fruits.remove('orange')
>>> print(fruits)
['pineapple', 'watermelon', 'apple']
>>> fruits.remove('apple')
>>> print(fruits)
['pineapple', 'watermelon']
>>> #Remove Items Using Pop
>>> fruits = ['orange', 'pineapple', 'watermelon', 'apple']
>>> fruits.pop()
'apple'
>>> print(fruits)
['orange', 'pineapple', 'watermelon']
>>> fruits.pop(2)
'watermelon'
>>> print(fruits)
['orange', 'pineapple']
>>> #Removing Items Using Del
>>> stationery = ['pencil', 'pen', 'eraser', 'ruler']
>>> del stationery[3]
>>> print(stationery)
['pencil', 'pen', 'eraser']
>>> del stationery[1:3]
>>> print(stationery)
['pencil']
>>> del stationery
>>> print(stationery)
Traceback (most recent call last):
  File "<python-input-103>", line 1, in <module>
    print(stationery)
          ^^^^^^^^^^
NameError: name 'stationery' is not defined
>>> lst = ['item1', 'item2', 'item3', 'item4']
>>> lst.clear()
>>> print(lst)
[]
>>> lst = ['item1', 'item2', 'item3', 'item4']
>>> lst_copy = lst.copy()
>>> print(lst_copy)
['item1', 'item2', 'item3', 'item4']
>>> #Joining Lists
>>> positive_numbers = [6, 7, 8, 9, 10]
>>> zero = [0]
>>> negative_numbers = [-1, -2, -3, -4, -5]
>>> integers = negative_numbers+zero+positive_numbers
>>> print(integers)
[-1, -2, -3, -4, -5, 0, 6, 7, 8, 9, 10]
>>> num1 = [2,5,8,9]
>>> num2 = [1,6,7]
>>> num1.extend(num2)
>>> print('Numbers:', num1)
Numbers: [2, 5, 8, 9, 1, 6, 7]
>>> negative_numbers = [-5,-4,-3,-2,-1]
>>> zero = [0]
>>> positive_numbers = [1,2,3,4,5]
>>> print('Integers:', negative_numbers)
Integers: [-5, -4, -3, -2, -1]
>>> #Counting Items in a List
>>> data = [17, 18, 9, 17, 10, 17, 12]
>>> print(data.count(17))
3
>>> #Find Index of an Item
>>> data = [13, 14, 32, 44, 14, 14, 65]
>>> print(data.index(14))
1
>>> #Reversing a List
>>> data = [22, 18, 32, 14, 15, 17]
>>> data.reverse()
>>> print(data)
[17, 15, 14, 32, 18, 22]
>>> #Sorting List Items
>>> data = [87, 45, 62, 15, 21, 8]
>>> data.sort()
>>> print(data)
[8, 15, 21, 45, 62, 87]
>>> data.sort(reverse=True)
>>> print(data)
[87, 62, 45, 21, 15, 8]