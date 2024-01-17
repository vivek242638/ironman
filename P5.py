"""
Calculate the average of numbers in a list
Input: [1, 2, 3, 4, 5]
"""
'''
for loop
'''
a=[1,2,3,4,5]

b=0
for i in range(len(a)):
       b += a[i]
avg = b/len(a)
print("R:",avg)

'''
While loop
'''
a=[1,2,3,4,5]
i=0
count=0
while count < len(a):
   i += a[count]
   count +=1
avg=i/len(a)
print("R1:",avg)