def compute_without_recursion(n, x):
    b = (1/2) * x  # b0
    y = 1  # y0
    for k in range(1, n + 1):
        b *= (x ** 2)
        y *= b
    return y

result_non_recursive = compute_without_recursion(5, 2)
print(f"Результат без рекурсии (n=5, x=2): {result_non_recursive}")