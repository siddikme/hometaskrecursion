def recursive_sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + recursive_sum(numbers[1:])

numbers = [1, 2, 3, 4, 5]
print("The sum is:", recursive_sum(numbers))
