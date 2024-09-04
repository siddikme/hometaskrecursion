def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = int(input('-> '))
b = int(input('-> '))
print("Max devision:",gcd(a,b))

# # Example usage:
# a = 48 b = 18
# output: 6

# a = 18 b = 12
# output: 6
