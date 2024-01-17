'''
Concatenate two lists
a= [1, 2, 3] 
b= [4, 5, 6]
'''
'''
"+" operator
'''
a= [1, 2, 3] 
b= [4, 5, 6]

i=a+b
print("vani:",i)

'''
extend operator
'''
a= [1, 2, 3] 
b= [4, 5, 6]

a.extend(b)
print("vani1:",a)


"""
for Loop
append() method
"""

a = [1, 2, 3]
b = [4, 5, 6]

for x in b:
    a.append(x)
print("Concatenated List:",a)

"""
for Loop
append() method and if statement
"""

a = [1, 2, 3]
b = [4, 5, 6]

for x in b:
    if x != 0:
        a.append(x)
print("Concatenated List:",a)

'''
While Loop
'''
a = [1, 2, 3]
b = [4, 5, 6]

i = a.copy()
index = 0

while index < len(b):
    i.append(b[index])
    index += 1

print("Concatenated List:", i)
