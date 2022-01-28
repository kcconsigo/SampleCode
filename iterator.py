my_list = [4, 7, 0, 3]

for element in my_list:
    print(element)


#Create an iterator object from that iterable
iter_obj = iter(my_list)

while True:
    try:
        element = next(iter_obj)
    except StopIteration:
        break