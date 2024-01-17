'''
Print a dictionary in table format
Input: {1: ["Sam", 21], 2: ["Bob", 25], 3: ["Cara", 30]}
Output:
§ ID Name Age
§ 1 Sam 21
§ 2 Bob 25
§ 3 Cara 30
37. Count the values associated with
'''
'''
For Loop
'''
a={1: ["Sam", 21], 2: ["Bob", 25], 3: ["Cara", 30]}
print("ID  | Name | Age")
print("-" * 17)

for key, values in a.items():
    print(f"{key:<3}| {values[0]:<5}| {values[1]:<3}")

'''
While Loop
'''
a={1: ["Sam", 21], 2: ["Bob", 25], 3: ["Cara", 30]}
print("ID  | Name | Age")
print("-" * 17)
keys = list(a.keys())  # Create a list of keys to iterate over
index = 0

while index < len(keys):
    key = keys[index]
    values = a[key]
    print(f"{key:<3}| {values[0]:<5}| {values[1]:<3}")
    index += 1