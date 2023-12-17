"""What will the following code print?:"""

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])



"""Briefly explain a topic in a specific context, in three bullet-points or less. The topic is 

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key]) 

in the context of Python for Everybody - Dictionaries and Loops | Learn | freeCodeCamp.org. 

exp:counts
is a dictionary with three key-value pairs.

The 
for
loop iterates through each key in 
counts
.

The 
if
statement checks if the value of the current key is greater than 10, and if so, prints both the key and its corresponding value.

"""
