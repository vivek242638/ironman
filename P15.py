'''
Check if a list is empty or not
Input: []
'''
'''
For Loop
'''
a=[]
is_empty = True
for _ in a:
    is_empty = False
    break
if is_empty:
    print("list is empty.")
else:
    print("list is not empty.")

'''
While Loop
'''
a=[]
is_empty = True
index=0
while index < len(a):
    is_empty = False
    break
    index += 1
if is_empty:
    print("list is empty.")
else:
    print("list is not empty.")