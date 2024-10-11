numbers = [2, 4, 3]

for number in numbers:  # Use 'number' instead of 'numbers' to iterate over the list
    if number % 3 == 0:  # Check if divisible by 3
        number = number ** 2
        print(f"{number} is divisible by 3")
    else:
        print(f"{number} is not divisible by 3")
