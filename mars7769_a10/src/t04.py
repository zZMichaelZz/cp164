"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-03-26"
-------------------------------------------------------
"""
# Imports
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()
a.insert_front(56)
a.insert_front(54)
a.insert_front(133)
a.insert_front(3)
a.insert_front(35)
a.insert_front(52)
a.insert_front(15423120)


Sorts.gnome_sort(a)

for i in a:
    print(i)