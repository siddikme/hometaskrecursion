def int_to_string(a):
    if a == 0:
        return ""
    elif a < 0:
        return "-" + int_to_string(-a)
    else:
        return int_to_string(a // 10) + str(a % 10)

digit = int(input("-> "))

if digit == 0:
    string_digit = "0"
else:
    string_digit = int_to_string(digit)

print(string_digit, type(string_digit))
