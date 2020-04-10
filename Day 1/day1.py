# Name :- Vinayak Parab
# Email id :- vinayakparab5626@gmail.com

#list and its defualt functions

list1 = [[12, 16], 1, 18, 'vinayak', 'parab']
print(list1)
print(list1[0])
list1.append('vinayakparab')
print(list1)
list1.remove('parab')
print(list1)
list1.insert(1, 'hello')
print(list1)
list1.extend(['vin', 2])
print(list1)
print(list1[0][1])
print(list1.pop())
print(list1.pop(3))

# dict

dict1 = {'Nokia':13999, 'samsung': 16999, 'apple': 39999}
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1)
print(dict1.pop('Nokia'))
dict1.update({'Nokia': 13999})
print(dict1)
print(dict1.get('apple'))
print(dict1.popitem())
print(dict1.clear())

# tuple
tuple1 = (1, 2, 3, 4, 5, 1, 6)
print(tuple1[1])
print(tuple1.count(1))
print(tuple1.index(4))
