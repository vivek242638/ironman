'''
Get the difference between two lists
o Input: [1, 2, 3, 4], [2, 3]
o Output: [1, 4]
'''
'''
For Loop
'''
a = [1, 2, 3, 4]
b = [2, 3]

i = []
for element in a:
    if element not in b:
        i.append(element)
print("Difference:", i)

'''
While Loop
'''
a = [1, 2, 3, 4]
b = [2, 3]

i = []
index = 0

while index < len(a):
    if a[index] not in b:
        i.append(a[index])
    index += 1
print("Difference:", i)