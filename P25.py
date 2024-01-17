'''
Check whether a list contains a sublist
o Input: [2, 4, 3, 5, 7], [4, 3]
o Output: True
'''
'''
For Loop
'''
a = [2, 4, 3, 5, 7]
b = [4, 3]

i = False

for i in range(len(a) - len(b) + 1):
    if a[i:i+len(b)] == b:
        i = True
        break
print("Does the list contain the sublist?", i)

'''
While Loop
'''
a = [2, 4, 3, 5, 7]
b = [4, 3]

i = False
index_main = 0

while index_main < len(a) - len(b) + 1:
    index_sub = 0
    while index_sub < len(b) and a[index_main + index_sub] == b[index_sub]:
        index_sub += 1

    if index_sub == len(b):
        i = True
        break

    index_main += 1
print("Does the list contain the sublist?", i)
