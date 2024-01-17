'''
Clone or copy a list
Input: [1, 2, 3, 4, 5]
'''
'''
For Loop
'''
a=[1,2,3,4,5]
i = []

for item in a:
    i.append(item)
print("Copied List:", i)
'''
While Loop
'''
a=[1,2,3,4,5]
i = []
index = 0

while index < len(a):
    i.append(a[index])
    index += 1
print("Copied List:", i)