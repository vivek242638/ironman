'''
Flatten a shallow list
Input: [[1, 2, 3], [4, 5], [6]]
Output: [1, 2, 3, 4, 5, 6]
'''
'''
While Loop
'''
a=[[1, 2, 3], [4, 5], [6]]
i = []
index = 0

while index < len(a):
    if isinstance(a[index], list):
        i.extend(a[index])
    else:
        i.append(a[index])
    index += 1
print(f"Flattened List: {i}")

'''
For Loop
'''
a=[[1, 2, 3], [4, 5], [6]]
i = []
index = 0
for sublist in a:
    if isinstance(sublist, list):
        i.extend(sublist)
    else:
        i.append(sublist)
print(f"Flattened List: {i}")