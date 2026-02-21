def multiply_pol_classic(a, b):
    """Классическое умножение"""
    if not a or not b:
        return [0]
    n, m = len(a), len(b)
    res = [0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            res[i + j] += a[i] * b[j]
    return res


def multiply_pol_karatsuba(a, b):
    """Умножение Карацубы"""
    while len(a) > 1 and a[-1] == 0: a.pop()
    while len(b) > 1 and b[-1] == 0: b.pop()
    n = max(len(a), len(b))
    if n <= 32:
        return multiply_pol_classic(a, b)

    m = 1
    while m < n:
        m *= 2
    a = a + [0] * (m - len(a))
    b = b + [0] * (m - len(b))

    mid = m // 2
    a_low, a_high = a[:mid], a[mid:]
    b_low, b_high = b[:mid], b[mid:]

    z0 = multiply_pol_karatsuba(a_low, b_low)
    z2 = multiply_pol_karatsuba(a_high, b_high)
    sum_a = [x + y for x, y in zip(a_low, a_high)]
    sum_b = [x + y for x, y in zip(b_low, b_high)]
    z1 = multiply_pol_karatsuba(sum_a, sum_b)
    for i in range(len(z0)):
        if i < len(z1): z1[i] -= z0[i]
    for i in range(len(z2)):
        if i < len(z1): z1[i] -= z2[i]

    res = [0] * (2 * m)
    for i in range(len(z0)): res[i] += z0[i]
    for i in range(len(z1)): res[i + mid] += z1[i]
    for i in range(len(z2)): res[i + 2 * mid] += z2[i]
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res


# Тест
if __name__ == "__main__":
    a = [1, 2, 3]  # 1 + 2x + 3x^2
    b = [4, 5]  # 4 + 5x
    print(f"Классика: {multiply_pol_classic(a, b)}")
    print(f"Карацуба: {multiply_pol_karatsuba(a, b)}")