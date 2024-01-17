'''
Find the index of an item in a specified list
o Input: [10, 20, 30, 40, 50], 40
o Output: 3
'''
'''
While Loop
'''
a = [10, 20, 30, 40, 50]
i = 40

index = 0
index_found = None

while index < len(a):
    if a[index] == i:
        index_found = index
        break
    index += 1
if index_found is not None:
    print(f"The index of {i} is: {index_found}")
else:
    print(f"{i} not found in the list.")

'''
For Loop
'''
a = [10, 20, 30, 40, 50]
i = 40

index_found = None

for index, item in enumerate(a):
    if item == i:
        index_found = index
        break
if index_found is not None:
    print(f"The index of {i} is: {index_found}")
else:
    print(f"{i} not found in the list.")
