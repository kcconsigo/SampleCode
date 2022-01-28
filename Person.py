class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')

harry = Person()

print(Person.age)

print(Person.greet)

print(Person.__doc__)

harry.greet()