from random import randint
even = 0
uneven = 0
list_number = [randint(20, 100) for _ in range(1, 101)]
for i in list_number:
    if i % 2 == 0:
        even += 1
    else:
        uneven += 1
print("четных-{}, нечетных-{}". format(even, uneven))