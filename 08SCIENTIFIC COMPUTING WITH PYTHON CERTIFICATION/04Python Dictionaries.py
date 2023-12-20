"""What does dict equal after running this code?:"""

"""code:"""

dict = {"Fri": 20, "Thu": 6, "Sat": 1}
dict["Thu"] = 13
dict["Sat"] = 2
dict["Sun"] = 9

"""
Q)Briefly explain a topic in a specific context, in three bullet-points or less. 
The topic is 
dict = {"Fri": 20, "Thu": 6, "Sat": 1}
dict["Thu"] = 13
dict["Sat"] = 2
dict["Sun"] = 9 in the context of Python for Everybody - Python Dictionaries | Learn | freeCodeCamp.org.

Explanation:
A dictionary is a collection of key-value pairs in Python.

The values of a dictionary can be accessed using the keys associated with them.

The "get" method can be used to retrieve a value from a dictionary, and a default value can be specified if the key is not found.

a){'Fri': 20, 'Thu': 13, 'Sat': 2, 'Sun': 9}
 """