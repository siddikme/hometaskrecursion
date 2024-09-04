def sum_series(n):
    if n <= 0:
        return 0
    else:
        return n + sum_series(n - 2)

print(f"sum_series(6) -> {sum_series(6)}")  
print(f"sum_series(10) -> {sum_series(10)}")  
