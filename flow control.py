
#num = float(input("Enter a number: "))
#if num >= 0:
#    if num == 0:
#        print("Zero")
#    else:
#        print("Positive")
#else:
#    print("Negative number")

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 5

# iterate over the list
for val in numbers:
    sum = sum + val #5+48

print("The sum is", sum)

genre = ['pop', 'rock', 'jazz']

for i in range(len(genre)):
    print("I like", genre[i])

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

student_name = 'Soyuj'

marks = {'James' : 90, 'Jules': 55, 'Arthur' : 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print("No entry with that name found")

n = int(input("Enter n:"))
n = 10

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1   # update counter

print("The sum is", sum)

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")

# Use of break statement inside the loop

for val in "string":
    if val == "i":
        break
    print(val)
print("The end")

for val in "string":
    if val == "i":
        continue
    print(val)
print("The end")

'''pass is just a placeholder for
functionality to be added later.'''
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass