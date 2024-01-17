'''
Sort a list alphabetically in a dictionary 
Input: {'n1': ['c', 'b', 'a'], 'n2': ['e', 'd']} 
Output: {'n1': ['a', 'b', 'c'], 'n2': ['d', 'e']}
'''
'''
For Loop
'''
a= {'n1': ['c', 'b', 'a'], 'n2': ['e', 'd']}
for key, value in a.items():
    value.sort()
print("Sorted Dictionary:", a)

'''
While Loop
'''
a= {'n1': ['c', 'b', 'a'], 'n2': ['e', 'd']}
keys = list(a.keys())
index = 0
while index < len(keys):
    key = keys[index]
    a[key].sort()
    index += 1
print("Sorted Dictionary:", a)
