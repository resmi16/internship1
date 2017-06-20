big_list = ['p','r','o','b','l','e','m']
big_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(big_list)

# Output: 'o'
print(big_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(big_list)

# Output: 'm'
print(big_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(big_list)

big_list.clear()

# Output: []
print(big_list)
