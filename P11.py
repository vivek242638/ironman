'''
Print a specified list after removing the 0th, 4th, and 5th elements
Input: ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
'''
list= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Remove specified elements using a for loop
list1 = []
for index, value in enumerate(list):
    if index not in [0, 4, 5]:
        list1.append(value)

# Print the result
print("List after removing elements:", list1)

'''
While loop
'''
list= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

list1 = []
index = 0
while index < len(list):
    if index not in [0, 4, 5]:
        list1.append(list[index])
    index += 1
print("List after removing elements:", list1)