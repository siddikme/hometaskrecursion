def print_numbers(n):
    if n > 50:
        return
    print(n)
    print_numbers(n + 1)

print_numbers(1)
