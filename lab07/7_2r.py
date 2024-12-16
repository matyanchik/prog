def compute_with_recursion(k, x):
    if k == 0:
        return 1
    else:
        b_prev = compute_b(k - 1, x)
        b_k = b_prev * (x ** 2)
        return b_k * compute_with_recursion(k - 1, x)

def compute_b(k, x):
    if k == 0:
        return (1/2) * x
    else:
        return compute_b(k - 1, x) * (x ** 2)
    
result_recursive = compute_with_recursion(5, 2)
print(f"Результат с рекурсией (n=5, x=2): {result_recursive}")