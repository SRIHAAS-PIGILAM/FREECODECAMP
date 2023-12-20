"""Which does the same thing as the following code?:"""

"""
lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)"""

"""counts
 is a Python dictionary containing key-value pairs.

The for loop iterates through each key-value pair using the 
.items()
 method and creates a new tuple 
newtup
 with the value as the first element and the key as the second element.

The 
newtup
 tuples are appended to a list 
lst
, which is then sorted in descending order using the 
sorted()
 function with the 
reverse=True
 argument. The sorted 
lst
 is then printed.

 A)print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )
"""