'''
Find the highest 3 values in a dictionary
Input: {'a': 10, 'b': 15, 'c': 4, 'd': 25, 'e': 8}
Output: [25, 15, 10]
'''
'''
For Loop
'''
a={'a': 10, 'b': 15, 'c': 4, 'd': 25, 'e': 8}
i = []

for key, value in sorted(a.items(), key=lambda x: x[1], reverse=True)[:3]:
    i.append((key, value))
print("Highest 3 Values:", i)

'''
While Loop
'''
a={'a': 10, 'b': 15, 'c': 4, 'd': 25, 'e': 8}
i = []
sorted_items = sorted(a.items(), key=lambda x: x[1], reverse=True)
index = 0

while index < min(3, len(sorted_items)):
    key, value = sorted_items[index]
    i.append((key, value))
    index += 1
print("Highest 3 Values:", i)   