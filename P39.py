'''
Remove spaces from dictionary keys 
oInput: {"a b": 1, "c d": 2, "e f": 3} 
Output: {"ab": 1, "cd": 2, "ef": 3}
'''
'''
For Loop
'''
a={"a b": 1, "c d": 2, "e f": 3}
b = {}

for key, value in a.items():
    new_key = key.replace(' ', '')
    b[new_key] = value
print("Dictionary with Keys without Spaces:", b)

'''
While Loop
'''
a={"a b": 1, "c d": 2, "e f": 3}
b = {}
keys = list(a.keys())

index = 0
while index < len(keys):
    key = keys[index]
    new_key = key.replace(' ', '')
    b[new_key] = a[key]
    index += 1
print("Dictionary with Keys without Spaces:", b)