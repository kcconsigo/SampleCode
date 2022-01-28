

# function definition
def greet(name):
    # function call
    print("Hello, "+ name + ". Good morning!")
greet('Paul')

def absolute_value(num):

    if num >=0:
        return num
    else:
        return -num

print(absolute_value(2))
print(absolute_value(-4))

def my_func():
    x = 10
    print("Value inside function:", x)
x = 20
my_func()
print("Value outside function:", x)


def greet(*names):

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)
greet("Monica", "Luke", "Steve", "John")

def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))

x = factorial(3)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

x = "global"

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()

x = 5
def foo():
    x = 10
    print("local x:", x)

foo()
print("global x:", x)