'''
Find a list in reverse order 
'''
'''
list in reverser order with default reverse method
'''

a=[1,2,3,4,5]
a.reverse()
print("vive:",a)

'''
with FOR LOOP
list in reverser order with for loop
'''
a=[1,2,3,4,5]
i = []
for value in a:
  i = [value] + i
print("vivek : ", i)


'''
list in reverse order with insert() method
'''
a=[1,2,3,4,5]
i = []
for value in a:
  i.insert(0,value)
print("vivek1: ", i )

'''
list in reverse order with append() method
'''
a=[1,2,3,4,5]
i = []
for value in range(len(a)):
  i.append(a.pop())
print("vivek2 : ", i)

'''
list in reverse order with sciling method
'''

a=[1,2,3,4,5]
i=a[::-1]
print("vivek3:",i)

'''
With While Loop
list in reverser order with while loop
'''

a=[1,2,3,4,5]
i=[]
while a:
    temp=a.pop()
    i.append(temp)
print("vivek4:",i)
