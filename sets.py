# Different types of sets in Python
# Set of integers

my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# add an element
my_set = {1, 2, 3, 4, 3, 2}
my_set.add(5)
my_set.discard(7)
print(my_set)


# add multiple elements
my_set = set([1, 2, 3, 4])
my_set.update([1, 5, 7, 8])
my_set.remove(8)
print(my_set)

my_set = set("HelloWorld")
print(my_set)
print(my_set.pop())

my_set.clear()

# initialize my_set
my_set = set ("apple")

# check if 'a' is present
# Output: True
print('a' in my_set)

# check if 'p' is present
# Output: False
print('p' not in my_set)

for letter in set("apple"):
    print(letter)

