'''
Remove duplicates from a list
Input: [1, 2, 2, 3, 3, 3]
'''
'''
set() Method
'''

a=[1,2,3,3,3]
i=list(set(a))
print("V:",i)

'''
FOR LOOP with if condition
'''
a=[1,2,3,3,3]
b = []
for i in a:
    if i not in b:
        b.append(i)
print("V1:",b)

'''
WHILE LOOP with if condition
'''
a=[1,2,3,3,3]
i = 0
while i < len(a):
      j = i + 1
      while j < len(a):
         if a[i] == a[j]:
            del a[j]
         else:
            j += 1
      i += 1
print("V2:",a)

'''
Using dictionaries
'''
a=[1,2,3,3,3]
dictionary=dict.fromkeys(a)
a=list(dictionary)
print("V3:",a)

