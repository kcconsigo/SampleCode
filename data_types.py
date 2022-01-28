from decimal import Decimal as D
print(D('1.1') + D('2.2'))
print(D('1.2') * D('2.50'))

# List indexing

my_list = ['p','r','o','b','e']

print(my_list[0])

print(my_list[2])

print(my_list[4])

# Nested List
n_list = ["Happy", [2,0,1,5]]

print(n_list[0][1])

print(n_list[1][3])

#print(my_list[4.0])

# Negative indexing in lines
my_list = ['p','r','o','b','e']

print(my_list[-1])
print(my_list[-5])

my_list = ['p','r','o','g','r','a','m','i','z']

my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

print(my_list[2:5])

print(my_list[:-5])

print(my_list[5:])

print(my_list[:])

del my_list[1:5]

my_list.clear()

# Python list methods
my_list = [3, 8, 1, 6, 0, 8, 4]

# Output: 2
print(my_list.count(8))

# Output: 1
print(my_list.index(8))

my_list.sort()

# Output: [0, 1, 3, 4, 6, 8, 8]
print(my_list)

my_list.reverse()

# Output: [8, 8, 6, 4, 3, 1, 0]
print(my_list)

for fruit in ['apple','banana','mango']:
    print("I like ", fruit)