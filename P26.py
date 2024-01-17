'''
Generate all permutations of a list
o Input: [1, 2, 3]
o Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
'''
'''
For Loop
'''
from itertools import permutations

a= [1, 2, 3]
i = []

for perm in permutations(a):
    i.append(tuple(perm))
print("All Permutations:", i)

'''
While Loop
'''
a = [1, 2, 3]
b = []
indices = [0] * len(a)
while True:
    current_permutation = tuple(a[i] for i in indices)
    b.append(current_permutation)

    i = len(a) - 1
    while i >= 0 and indices[i] == i:
        indices[i] = 0
        i -= 1
    if i < 0:
        break
    indices[i] += 1
print("All Permutations:", b)


