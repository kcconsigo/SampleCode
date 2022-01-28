try:
    num = int(input("Enter numerator: "))
    den = int(input(("Enter denominator: ")))

    result = num / den #compute the numerator and denominator
    print(result)
except:
    print("Denominator cannot be 0. Please try again.")
print("Program ends")

import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

try:
    pass
except ValueError:
    pass
except (TypeError, ZeroDivisionError):
    pass
except:
    pass

try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number")
except ValueError as ve:
    print(ve)

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number")
else:
    reciprocal = 1/num
    print(reciprocal)