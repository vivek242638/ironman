'''
Get unique values from a list
Input: [1, 2, 3, 3, 3, 4, 4]
'''
'''
For Loop
'''
a= [1, 2, 3, 3, 3, 4, 4]
i = []

for item in a:
    if item not in i:
        i.append(item)
print("Unique Values:", i)

'''
While Loop
'''
a= [1, 2, 3, 3, 3, 4, 4]

i = []
index = 0
while index < len(a):
    item = a[index]
    if item not in i:
        i.append(item)
    index += 1
print("Unique Values:", i)