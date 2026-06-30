>>> #Dictionaries
>>> #Creating a dictionary
>>> score = {'A':55, 'B':60, 'C':51, 'E':67, 'F':70}
>>> print(len(score))
5
>>> print(score['A'])
55
>>> print(score['B'])
60
>>> print(score.get('C'))
51
>>> score['G'] = 80
>>> print(score)
{'A': 55, 'B': 60, 'C': 51, 'E': 67, 'F': 70, 'G': 80}
>>> score['A'] = 75
>>> print(score)
{'A': 75, 'B': 60, 'C': 51, 'E': 67, 'F': 70, 'G': 80}
>>> #Checking key
>>> print('C' in score)
True
>>> print('J' in score)
False
>>> #Removing key
>>> score = {'A':75, 'B':60, 'C':51, 'E':67, 'F':70, 'G':80}
>>> score.pop('A')
75
>>> print(score)
{'B': 60, 'C': 51, 'E': 67, 'F': 70, 'G': 80}
>>> score.popitem()
('G', 80)
>>> print(score)
{'B': 60, 'C': 51, 'E': 67, 'F': 70}
>>> del score['E']
>>> print(score)
{'B': 60, 'C': 51, 'F': 70}
>>> #Changing Dictionary to a List of Items
>>> score = {'A':75, 'B':60, 'C': 51, 'E':67, 'F':70, 'G':80}
>>> print(score.items())
dict_items([('A', 75), ('B', 60), ('C', 51), ('E', 67), ('F', 70), ('G', 80)])
>>> #Clearing a Dictionary
>>> print(score.clear())
None
>>> #Copy a Dictionary
>>> score = {'A':75,'B':60,'C':88,'D':98,'E':67}
>>> score_copy = score.copy()
>>> print(score_copy)
{'A': 75, 'B': 60, 'C': 88, 'D': 98, 'E': 67}
>>> #Getting Dictionary Keys as a List
>>> score = {"A":78, "B":96,"H":45, "F":65, "O":87}
>>> keys = score.keys()
>>> print(keys)
dict_keys(['A', 'B', 'H', 'F', 'O'])
>>> #Getting Dictionary Values as a List
>>> values = score.values()
>>> print(values)
dict_values([78, 96, 45, 65, 87])