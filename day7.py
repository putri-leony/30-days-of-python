>>> #Sets
>>> st = {'item1', 'item2', 'item3', 'item4'}
>>> len(st)
4
>>> print('Does set st contain item3?', 'item3' in st)
Does set st contain item3? True
>>> st.add('item5')
>>> print(st)
{'item1', 'item5', 'item4', 'item3', 'item2'}
>>> st.update(['item5', 'item6', 'item7'])
>>> print(st)
{'item6', 'item1', 'item5', 'item4', 'item3', 'item2', 'item7'}
>>> fruits = {'banana', 'orange', 'mango', 'lemon'}
>>> vegetables = {'tomato', 'potato', 'cabbage', 'carrot'}
>>> fruits.update(vegetables)
>>> print(fruits)
{'banana', 'lemon', 'orange', 'carrot', 'cabbage', 'mango', 'potato', 'tomato'}
>>> #Removing Items
>>> st.remove('item2')
>>> print(st)
{'item6', 'item1', 'item5', 'item4', 'item3', 'item7'}
>>> fruits = {'banana', 'orange', 'mango', 'lemon'}
>>> fruits.pop()
'banana'
>>> removed_item = fruits.pop()
>>> print(removed_item)
lemon
>>> #Clearing Items
>>> st = {'item1', 'item2', 'item3', 'item4'}
>>> st.clear()
>>> print(st)
set()
>>> #Deleting a set
>>> st ={'item1', 'item2', 'item3', 'item4'}
>>> del st
>>> print(st)
Traceback (most recent call last):
  File "<python-input-26>", line 1, in <module>
    print(st)
          ^^
NameError: name 'st' is not defined. Did you mean: 'set'?
>>> #Converting list to set
>>> lst = ['item1', 'item2', 'item3', 'item4', 'item1']
>>> st = set(lst)
>>> print(st)
{'item3', 'item1', 'item4', 'item2'}
>>> #Joining Sets
>>> st1 = {'item1', 'item2', 'item3', 'item4'}
>>> st2 = {'item5', 'item6', 'item7', 'item8'}
>>> st3 = st1.union(st2)
>>> print(st3)
{'item6', 'item1', 'item5', 'item4', 'item3', 'item2', 'item8', 'item7'}
>>> st1 = {'item1', 'item2', 'item3', 'item4'}
>>> st2 = {'item5', 'item6', 'item7', 'item8'}
>>> print(st1.union(st2))
{'item6', 'item1', 'item5', 'item4', 'item3', 'item2', 'item8', 'item7'}
>>> #Finding Intersection Items
>>> st1 = {'item1', 'item2', 'item3', 'item4'}
>>> st2 = {'item3', 'item2'}
>>> st1.intersection(st2)
{'item3', 'item2'}
>>> whole_numbers = {0,1,2,3,4,5,6,7}
>>> even_numbers = {0,2,4,6}
>>> whole_numbers.intersection(even_numbers)
{0, 2, 4, 6}
>>> #Subset and Super Set
>>> whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
>>> even_numbers = {0,2,4,6,8,10}
>>> whole_numbers.issubset(even_numbers)
False
>>> whole_numbers.issuperset(even_numbers)
True
>>> #Difference between two sets
>>> st1 = {'item1', 'item2', 'item3', 'item4'}
>>> st2 = {'item2', 'item3'}
>>> st2.difference(st1)
set()
>>> st1.difference(st2)
{'item1', 'item4'}
>>> whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
>>> even_numbers = {0,2,4,6,8,10}
>>> whole_numbers.difference(even_numbers)
{1, 3, 5, 7, 9}
>>> #Symmetric difference between two sets
>>> st1 = {'item1', 'item2', 'item3', 'item4'}
>>> st2 = {'item2', 'item3'}
>>> st2.symmetric_difference(st1)
{'item1', 'item4'}
>>> whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
>>> some_numbers = {1,2,3,4,11}
>>> whole_numbers.symmetric_difference(some_numbers)
{0, 5, 6, 7, 8, 9, 10, 11}
>>> #Joining Sets
>>> st1 = {'item1', 'item2', 'item3', 'item4'}
>>> st2 = {'item2', 'item3'}
>>> st2.isdisjoint(st1)
False
>>> even_numbers = {0,2,4,6,8}
>>> odd_numbers = {1,3,5,7,9}
>>> even_numbers.isdisjoint(odd_numbers)
True