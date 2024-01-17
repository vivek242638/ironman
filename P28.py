'''
Convert a list of characters into a string
o Input: ['P', 'y', 't', 'h', 'o', 'n']
o Output: "Python"
'''
'''
For Loop
'''
a= ['P', 'y', 't', 'h', 'o', 'n']

i = ""
for char in a:
    i += char
print("Converted String:", i)

'''
While Loop
'''
a= ['P', 'y', 't', 'h', 'o', 'n']

i = ""
index = 0

while index < len(a):
    i += a[index]
    index += 1
print("Converted String:", i)
