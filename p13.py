'''
Find the second smallest number in a list
Input: [1, 2, 3, 4, 5]
'''
'''
While loop
'''
list=[1,2,3,4,5]


length = len(list)
index = 0
smallest = float('inf')
second_smallest = float('inf')
while index < length:
    num = list[index]
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num
    index += 1
print("Second smallest number:", second_smallest)

'''
For Loop
'''
list=[1,2,3,4,5]

smallest = float('inf')
second_smallest = float('inf')
for num in list:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num
print("Second smallest number:", second_smallest)