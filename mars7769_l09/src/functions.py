"""
-------------------------------------------------------
[Lab 9, Functions]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-03-13"
-------------------------------------------------------
"""
# Imports

# Constants

def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
     695    2 Lasagna, 7
    1355    4 Butter Chicken, 2
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("Hashes")
    print("Hash     Slot Key")
    print("-------- ---- --------------------")
    for i in values:
        h = hash(i)
        slot = h % slots
        f_str = i.key()
        print("{:8}{:5} {}".format(h, slot, f_str))
    return
    