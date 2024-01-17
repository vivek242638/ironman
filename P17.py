'''
Find the list of words that are longer than n from a given list of words
Input: ['hello', 'world', 'name', 'python', 'programming'], n = 4
Output: ['hello', 'world', 'python', 'programming']
'''
'''
For Loop
'''
a= ['hello', 'world', 'name', 'python', 'programming'] 
n = 4
long_words = []

for word in a:
    if len(word) > n:
        long_words.append(word)
print(f"Words longer than {n} characters: {long_words}")

'''
While Loop
'''
a= ['hello', 'world', 'name', 'python', 'programming'] 
n = 4
long_words = []
index = 0

while index < len(a):
    if len(a[index]) > n:
        long_words.append(a[index])
    index += 1
print(f"Words longer than {n} characters: {long_words}")