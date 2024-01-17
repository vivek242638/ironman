'''
Find the ASCII value of a character
Input: 'A'
'''
'''
for Loop
'''
i = 'A' 
i_length = len(i)  
for K in i:  
    ASCII = ord(K)  
print ("Vivek:",K,ASCII)

'''
While Loop
'''
i = 'A' 
ascii_value = None
index = 0

while index < 256:
    if chr(index) == i:
        ascii_value = index
        break
    index += 1

# Print the result
if ascii_value is not None:
    print(f"The ASCII value of '{i}' is: {ascii_value}")
else:
    print(f"Character '{i}' not found.")

