'''
Check whether two lists are circularly identical
o Input: [1, 2, 3, 4], [2, 3, 4, 1]
o Output: True
'''
'''
For Loop
'''
a = [1, 2, 3, 4]
b = [2, 3, 4, 1]

i = False
for i in range(len(a)):
    if all(a[j] == b[(i + j) % len(b)] for j in range(len(a))):
        i = True
        break
print("Output:", i)

'''
While Loop
'''
a = [1, 2, 3, 4]
b = [2, 3, 4, 1]

i = False
index = 0

while index < len(a):
    if all(a[j] == b[(index + j) % len(b)] for j in range(len(a))):
        i = True
        break
    index += 1
print("Output:", i)