import random

distinct_number = int(input("How many distinct coupon do you need to generate:"))
random_numbers = []
counter = 0
#
while True:
    numbers = random.randint(1000, 9999)
    counter += 1
    if numbers not in random_numbers:
        random_numbers.append(numbers)
    if len(random_numbers) == distinct_number:
        break
print("Total number of random numbers is generated :", counter)

# printing the list
for i in range(0, len(random_numbers)):
    print(random_numbers[i])
print()
