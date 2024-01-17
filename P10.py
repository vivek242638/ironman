'''
Create a dictionary from two lists
Input: ['a', 'b', 'c'], [1, 2, 3]
'''
'''
For Loop
'''
a=['a','b','c']
b=[1,2,3]

i = {}
for key in b:
    for value in a:
        i[key] = value
        a.remove(value)
        break 
print("Created Dictionary: ", i)

'''
While Loop
'''
a=['a','b','c']
b=[1,2,3]
i = {}
index = 0

while index < len(b) and index < len(a):
    i[b[index]] = a[index]
    index += 1

# Print the resulting dictionary
print("Created Dictionary:", i)