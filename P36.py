'''
Count the values associated with a key in a dictionary 
Input: {'A': [1, 2, 3], 'B': [4, 5], 'C': [6]}
Output: {‘A’: 3, ‘B’: 2, ‘C’: 1}
'''
'''
While Loop
'''
a= {'A': [1, 2, 3], 'B': [4, 5], 'C': [6]}
keys = list(a.keys())

index = 0
while index < len(keys):
    key = keys[index]
    value_count = len(a[key])
    print(f"Key '{key}' has {value_count}.")
    index += 1

'''
For Loop
'''
a= {'A': [1, 2, 3], 'B': [4, 5], 'C': [6]}
for key, values in a.items():
    value_count = len(values)
    print(f"Key '{key}' has {value_count}.")