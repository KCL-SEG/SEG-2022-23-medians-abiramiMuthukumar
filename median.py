"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()

if len(numbers) % 2 != 0:
    print(numbers[int((len(numbers) -1)/2)])
else:
    num_index = int(len(numbers)/2 - 1)
    result = (numbers[num_index] + numbers[num_index + 1]) / 2
    print(result)