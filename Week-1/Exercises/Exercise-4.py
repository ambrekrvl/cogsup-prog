################################################################################
"""
Recommended readings: 
  Chapter on dictionaries: https://automatetheboringstuff.com/3e/chapter7.html 
  Iterating through dictionaries: https://realpython.com/iterate-through-dictionary-python/
"""
################################################################################

"""
Exercise 4.1

Task:
------
Print the sum of the values in the dictionary.
"""

dct = {'a': 3, 'b': 7, 'c': -2, 'd': 10, 'e': 5}

print("Exercise 4.1")

total = 0

for value in dct.values():
    total += value
print(total)

"""
Exercise 4.2

Task:
------
Print the key that has the largest value in dct.
"""

print("Exercise 4.2")

max_key = None
max_value = 0

for key, value in dct.items():
    if value>max_value:
        max_value = value
        max_key=key

print(max_key)
    
"""
Exercise 4.3

Task:
------
Create a new dictionary with the squares of all the values in dct.
"""

print("Exercise 4.3")
new_dct = {}
for key, value in dct.items():
    new_dct[key] = value **2
print(new_dct)

"""
Exercise 4.4

Task:
------
Print only the keys in dct whose values are even numbers.
"""

print("Exercise 4.4")

for key, value in dct.items():
    if value % 2==0:
        print(key)

"""
Exercise 4.5

Task:
------
Create a new dictionary that swaps the keys and values in dct.
"""

print("Exercise 4.5")

new_dct = {}
for key, value in dct.items():
    new_dct[value]=key
print(new_dct)

"""
Exercise 4.6

Task:
------
Count the number of times each letter appears in the string 'ccctcctttttcc'
and print the resulting dictionary.
"""

s = 'ccctcctttttcc'

print("Exercise 4.6")

count = {}

for letter in 'ccctcctttttcc':
    count[letter] = count.get(letter,0)+1

print(count)

"""
Exercise 4.7

Task:
------
Given the dictionary of responses_mapping = {'j':'jazz', 'p':'pop'},
and the string responses = 'jjjpjjpppppjj',
print the list of corresponding words.
"""

responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'

print("Exercise 4.7")

result =[]

for letter in responses:
    result.append(responses_mapping[letter])

print(result)

"""
Exercise 4.8

Task:
------
Merge the following two dictionaries into one:
{'a': 1, 'b': 2} and {'c': 3, 'd': 4}
"""

print("Exercise 4.8")

d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
merged = {}
for key, value in d1.items():
    merged[key] = value
for key, value in d2.items():
    merged[key] = value
print(merged)

"""
Exercise 4.9

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose keys are sorted alphabetically.
"""

print("Exercise 4.9")

dct = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}
sorted_dct = {}
for key in sorted(dct):
    sorted_dct[key] = dct[key]
print(sorted_dct)

"""
Exercise 4.10

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose values appear in increasing order.
"""

print("Exercise 4.10")
dct = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}

sorted_dct = {}
for key, value in sorted(dct.items(), key=lambda item: item[1]):
    sorted_dct[key]=value

print(sorted_dct)