'''
Append a list to the second list
Input: [1, 2, 3], [4, 5, 6]
Output: [1, 2, 3, 4, 5, 6]
'''
'''
While Loop
'''
a=[1,2,3]
b=[4,5,6]
index = 0
while index < len(b):
    a.append(b[index])
    index += 1
print("First List:", a)

'''
For Loop
'''
a=[1,2,3]
b=[4,5,6]
for item in b:
    a.append(item)
print("First List:", a)