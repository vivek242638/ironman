'''
Create a list by concatenating a given list which range goes from 1 to n
o Input: ['p', 'q'], n = 3
o Output: ['p1', 'q1', 'p2', 'q2', 'p3', 'q3']
'''
'''
For Loop
'''
a = ['p', 'q']
n = 3

i = []
for b in range(1, n + 1):
    for item in a:
        i.append(item + str(b))
print(f"i (Concatenated with range 1 to {n}):", i)

'''
While Loop
'''
a = ['p', 'q']
n = 3

i = []
index_outer = 1

while index_outer <= n:
    index_inner = 0

    while index_inner < len(a):
        i.append(a[index_inner] + str(index_outer))
        index_inner += 1
    index_outer += 1
print(f"i (Concatenated with range 1 to {n}):", i)