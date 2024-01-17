'''
Get the frequency of the elements in a list
o Input: [1, 2, 2, 3, 4, 4, 4]
o Output: {1: 1, 2: 2, 3: 1, 4: 3}
'''
'''
For Loop
'''
a = [1, 2, 2, 3, 4, 4, 4]
i = {}
for element in a:
    if element in i:
        i[element] += 1
    else:
        i[element] = 1
print("Frequency of Elements:", i)

'''
While Loop
'''
a = [1, 2, 2, 3, 4, 4, 4]
i = {}
index = 0
while index < len(a):
    current_element = a[index]
    if current_element in i:
        i[current_element] += 1
    else:
        i[current_element] = 1
    index += 1
print("Frequency of Elements:", i)