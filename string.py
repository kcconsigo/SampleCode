my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

my_string = """Hello, welcome to the world of Python"""
print(my_string)

str = 'programiz'
print('str = ', str )

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:2] = ', str[5:-2])

tell_some = """Programiz"""

#first character
print('tell_some[0] =', tell_some[0])

#last character
print('tell_some[2:5] = ', tell_some[2:5])

#slicing 3th to 2nd last character
print('tell_some[3:-2] = ', tell_some[3:-2])

str = 'cold'
list_enumerate = list(enumerate(str))
print('list(enumerate(str)', len(str))

print('len(str) = ', len(str))

# Python string format() method

#default(implicit) order
default_order = "{}, {} and {}".format('John', 'Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

#order using positional argument
positional_order = "{1}, {0} and {2}".format('John', 'Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

#order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j = 'John', b = 'Bill', s = 'sean')
print('\n--- Keyword Order ---')
print(keyword_order)


