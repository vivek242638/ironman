'''
Convert a list to a tuple
Input: [1, 2, 3, 4, 5]
'''

a=[1,2,3,4,5]
i=tuple(a)
print("Converted Tuple:",i)

'''
for loop
'''
a=[1,2,3,4,5]
i=tuple()
for element in a:
        i += (element,)  
print("Converted Tuple:",i)


'''
while loop
'''
a = [1, 2, 3, 4, 5]
i = ()
index = 0

while index < len(a):
    i += (a[index],)
    index += 1
print("Converted Tuple:", i)


