"""
-------------------------------------------------------
[Task 5, Assignment 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
# Imports
from Food_utilities import food_search
from Food import Food

f = Food("pie", 3, True, 600)
f2 = Food("apple", 3, True, 7)
f3 = Food("banana", 1, False, 6)

foods = [f, f2, f3]

results = food_search(foods, 3, 500, True)

for i in results:
    print(i)