'''
Get the difference between two lists
a= [1, 2, 3, 4],
b= [1, 2]

'''
'''
For Loop
'''
a=[1,2,3,4]
b=[1,2]
i = []
for element in a:
   if element  not in b:
    i.append(element)
print('vivek:',i)

'''
While Loop
'''
a=[1,2,3,4]
b=[1,2]
i = []

index1 = 0
while index1 < len(a):
    item = a[index1]
    if item not in b:
        i.append(item)
    index1 += 1

index2 = 0
while index2 < len(b):
    item = b[index2]
    if item not in a:
        i.append(item)
    index2 += 1
print("Difference between two lists:", i)
