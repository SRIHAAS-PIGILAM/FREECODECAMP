"""Dictionaries: Common Applications"""

"""What will the following code print?"""

"""code:"""

counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))

"""
Q)Briefly explain a topic in a specific context, in three bullet-points or less. 
The topic is
 counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0)) 
in the context of Python for Everybody - Dictionaries: Common Applications | Learn | freeCodeCamp.org. 

Explanation:T
he countsvariable is a dictionary in Python.

The counts.get('kris', 0)
 method will return the value of the key 'kris' in the 
counts dictionary. 
If the key does not exist in the dictionary, the method will return the second parameter, which is 0 in this case.
So, the output of the given code will be 0 since 'kris' is not a key in the 
counts dictionary.

A)0

"""