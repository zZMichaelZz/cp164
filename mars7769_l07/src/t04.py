"""
-------------------------------------------------------
[Lab 7, Task 4]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-02-29"
-------------------------------------------------------
"""
# Imports
from List_linked import List

source1 = List()
source2 = List()
target = List()

source1.append(1)
source1.append(3)
source1.append(2)
source1.append(1)

source2.append(1)
source2.append(2)
source2.append(3)

target.intersection(source1, source2)

print(target._front._value, target._front._next._value,
      target._front._next._next._value)