'''
Create a dictionary from a string
Input: "w3resource" 
Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
'''
'''
While Loop
'''
a="w3resource"
i = {}
index = 0

while index < len(a):
    char = a[index]
    if char in i:
        i[char] += 1
    else:
        i[char] = 1
    index += 1
print("Character Count Dictionary:", i)

'''
for Loop
'''
a="w3resource"
i = {}
for char in a:
    if char in i:
        i[char] += 1
    else:
        i[char] = 1
print("Character Count Dictionary:", i)