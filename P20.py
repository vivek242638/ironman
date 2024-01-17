'''
Find the index of an item in a specified list
Input: [1, 2, 3, 4, 5], 4
Output: 3
'''
'''
For Loop
'''
a=[1, 2, 3, 4, 5]
b=4
i = None

for index, item in enumerate(a):
    if item == b:
        i = index
        break

# Print the result
if i is not None:
    print(f"The index of {b} is: {i}")
else:
    print(f"{b} not found in the list.")

'''
While Loop
'''
a=[1, 2, 3, 4, 5]
b=4
i = None
while index < len(a):
    if a[index] == b:
        i = index
        break
    index += 1

# Print the result
if i is not None:
    print(f"The index of {b} is: {i}")
else:
    print(f"{b} not found in the list.")