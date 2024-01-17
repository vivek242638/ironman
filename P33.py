'''
Combine values in a Python list of dictionaries
Input: [{1: 10}, {2: 20}, {3: 30}]
Output: {1: 10, 2: 20, 3: 30}
'''
'''
For Loop
'''
a = [{1: 10}, {2: 20}, {3: 30}]

# Combine values into a single dictionary using a for loop
i = {}

for dictionary in a:
    i.update(dictionary)
print("Combined Dictionary:", i)

'''
While Loop
'''
a= [{1: 10}, {2: 20}, {3: 30}]
i = {}
index_outer = 0

while index_outer < len(a):
    dictionary = a[index_outer]
    
    for key, value in dictionary.items():
        i[key] = value

    index_outer += 1
print("Combined Dictionary:", i)