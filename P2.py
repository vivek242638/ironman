'''
Find the number of elements in a list.
a=[1,2,3,4,5]
'''
'''
using len() function
'''
a=[1,2,3,4,5]
print(len(a))

'''
for Loop
'''
a=[1,2,3,4,5]

count=0
for i in a:
    count+=1
print("Number of elements in the list:", i) 


'''
While Loop
'''

a = [1,2,3,4,5]
count = 0
index = 0

while index < len(a):
    count += 1
    index += 1
print("Number of elements in the list:", count)