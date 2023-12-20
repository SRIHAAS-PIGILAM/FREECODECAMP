"""What will the following code print?:"""

d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)

"""Briefly explain a topic in a specific context, in three bullet-points or less. The topic is
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i) 

in the context of Python for Everybody - The Tuples Collection | Learn | freeCodeCamp.org. 

The code creates a dictionary called 
d
 with three key-value pairs.

The 
for
 loop iterates through each item in the dictionary using the 
.items()
 method, which returns a list of tuple pairs containing each key-value pair in 
d
.

The 
print
 statement then prints each key-value pair in the format 
key value

A)
quincy 1
beau 5
kris 9
"""