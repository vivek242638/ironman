'''
Create and display all combinations of letters, selecting each letter from a different key in
a dictionary
Input: {'1': ['a', 'b'], '2': ['c', 'd']}
Output: ['ac', 'ad', 'bc', 'bd']
'''
'''
For Loop
'''
a= {'1':['a', 'b'], '2':['c', 'd']}
my_list= list(a.values())
for i in my_list[0]:
    for j in my_list[1]:
        print(i+j)

'''
While Loop
'''
# Input dictionary
input_dict = {'1': ['a', 'b'], '2': ['c', 'd']}

# Create and display all combinations using a while loop
combinations = []
keys = list(input_dict.keys())
index_outer = 0

while index_outer < len(input_dict[keys[0]]):
    index_inner = 0
    combination = ''
    while index_inner < len(keys):
        key = keys[index_inner]
        combination += input_dict[key][index_outer]
        index_inner += 1

    combinations.append(combination)
    index_outer += 1
print("All Combinations:", combinations)

# Input dictionary
input_dict = {'1': ['a', 'b'], '2': ['c', 'd']}

# Create and display all combinations using a for loop
combinations = []
keys = list(input_dict.keys())

for index_outer in range(len(input_dict[keys[0]])):
    combination = ''
    for key in keys:
        combination += input_dict[key][index_outer]
    
    combinations.append(combination)
print("All Combinations:", combinations)
