def smallest_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors[:5]

def M(N):
    divs = smallest_divisors(N)
    if len(divs) < 5:
        return 0
    product = 1
    for d in divs:
        product *= d
    return product

numbers_found = []
n = 200_000_001

while len(numbers_found) < 5:
    m_value = M(n)
    if 0 < m_value < n:
        numbers_found.append(m_value)
    n += 1

numbers_found.sort()
print(numbers_found)