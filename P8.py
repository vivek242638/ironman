'''
Swap two variables
Input: a = 5, b = 10
'''
'''
For Loop
'''
a=5
b=10

for _ in range(2):  
    a, b = b, a
print("a =", a)
print("b =", b)

'''
While Loop
'''
a = 5
b = 10

count = 0
while count < 2: 
    a, b = b, a
    count += 1
print("a =", a)
print("b =", b)
