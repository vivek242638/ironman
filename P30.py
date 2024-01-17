'''
Flatten a list without using recursion
Input: [[1, 2], [3, 4], [5, 6]]
Output: [1, 2, 3, 4, 5, 6]
'''
'''
For Loop
'''
a= [[1, 2], [3, 4], [5, 6]]
i = []

for sublist in a:
    for item in sublist:
        i.append(item)
print("Flattened List:", i)

'''
While Loop
'''
a= [[1, 2], [3, 4], [5, 6]]
i = []
index_outer = 0

while index_outer < len(a):
    index_inner = 0
    while index_inner < len(a[index_outer]):
        i.append(a[index_outer][index_inner])
        index_inner += 1
    index_outer += 1
print("Flattened List:", i)