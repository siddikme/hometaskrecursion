def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

# Example usage:
a = 3
b = 4
result = power(a, b)
print(result)  # Output will be 8
