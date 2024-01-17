str = 'harsha'
i = ' '.join(str)
print(i) 

'''
with for loop
'''
a = 'harsha'
i = ''

for char in a:
    i += char + ' ' * 1
i = i.strip()
print(i) 