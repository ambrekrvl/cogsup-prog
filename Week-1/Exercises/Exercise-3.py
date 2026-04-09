################################################################################
"""
Recommended readings: 
  Chapter on lists: https://automatetheboringstuff.com/3e/chapter6.html 
  List comprehension: https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
"""
################################################################################

"""
Exercise 3.1

Task:
------
Write code that prints the sum of the elements in the following list.
[1, 4, -6, 7, 2, 3, 9, 11, 6]
"""

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6] # In all exercises in this script, you will work with this list

print("Exercise 3.1")

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6]

total=0

for num in lst:
    total += num

print (total)

"""
Exercise 3.2

Task:
------
Print the product of the elements in the list.
"""

print("Exercise 3.2")

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6]

product = 1 

for num in lst:
    product *= num
print(product)

"""
Exercise 3.3

Task:
------
Print the sum of the squares of the list.
"""

print("Exercise 3.3")

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6]
total=0

for num in lst:
    total+=num**2
print(total)

"""
Exercise 3.4

Task:
------
Print the largest element of the list.
"""

print("Exercise 3.4")

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6]

max_val = lst[0]

for num in lst:
    if num>max_val:
        max_val=num
print(max_val)

"""
Exercise 3.5

Task:
------
Print the largest element of the list.
"""

print("Exercise 3.5")

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6]

print(max(lst))