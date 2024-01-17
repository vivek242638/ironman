'''
Find the intersection of two sets
Input: {1, 2, 3}, {2, 3, 4}
'''
'''
& Operator
'''
a= {1, 2, 3}
b= {2, 3, 4}

i = a & b
print("Intersection Set:",i)

'''
for Loop with if statement
'''
a= {1, 2, 3}
b= {2, 3, 4}

i = []
for element in a:
    if element in b:
         i.append(element)
print("Intersection Set:",set(i))

'''
While Loop
'''
a= {1, 2, 3}
b= {2, 3, 4}
i = set()
index1 = 0
index2 = 0

while index1 < len(a):
    element = list(a)[index1]
    if element in b:
        i.add(element)
    index1 += 1
print("Intersection Set:", i)