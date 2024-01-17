'''
Convert a list into a nested dictionary of keys 
Input: [1, 2, 3, 4]
Output: {1: {2: {3: {4: {}}}}}
'''
'''
While Loop
'''
a=[1, 2, 3, 4]
i = {}
index = len(a) - 1

while index > 0:
    i = {a[index]: i}
    index -= 1
print("Nested Dictionary:", i)

'''
For Loop
'''
a=[1, 2, 3, 4]
i = {}

for item in reversed(a):
    i = {item: i}
print("Nested Dictionary:", i)