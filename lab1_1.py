def eval_pol_direct(coeffs, x):
    """Прямое вычисление P(x) через степени"""
    res = 0
    for i, c in enumerate(coeffs):
        res += c * (x ** i)
    return res

def eval_pol_horner(coeffs, x):
    """Схема Горнера"""
    res = 0
    for c in reversed(coeffs):
        res = res * x + c
    return res

# Тест
if __name__ == "__main__":
    c = [1, 2, 3]  # 1 + 2x + 3x^2
    x = 2
    print(f"Прямой: {eval_pol_direct(c, x)}")
    print(f"Горнер: {eval_pol_horner(c, x)}")