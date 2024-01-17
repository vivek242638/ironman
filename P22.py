'''
Find the second largest number in a list
o Input: [1, 3, 4, 5, 0, 2]
o Output: 4
'''
'''
While Loop
'''
a= [1, 3, 4, 5, 0, 2]

largest = second_largest = float('-inf')
index = 0

while index < len(a):
    current_number = a[index]
    
    if current_number > largest:
        second_largest = largest
        largest = current_number
    elif current_number > second_largest and current_number < largest:
        second_largest = current_number

    index += 1

print("Second Largest Number:", second_largest)

'''
For Loop
'''
a = [1, 3, 4, 5, 0, 2]

largest = second_largest = float('-inf')

for current_number in a:
    if current_number > largest:
        second_largest = largest
        largest = current_number
    elif current_number > second_largest and current_number < largest:
        second_largest = current_number
print("Second Largest Number:", second_largest)

