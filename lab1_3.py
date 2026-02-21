from lab1_2 import multiply_pol_classic, multiply_pol_karatsuba

def string_to_coeffs(s):
    """Строка преобразуется в список"""
    return [int(c) for c in reversed(s)]


def coeffs_to_string(coeffs):
    """Список коэффициентов преобразуется в строку"""
    if not coeffs:
        return "0"

    carry = 0
    for i in range(len(coeffs)):
        val = coeffs[i] + carry
        coeffs[i] = val % 10
        carry = val // 10

    while carry:
        coeffs.append(carry % 10)
        carry //= 10

    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()

    return ''.join(map(str, reversed(coeffs)))


def multiply_int_classic(s1, s2):
    c1 = string_to_coeffs(s1)
    c2 = string_to_coeffs(s2)
    return coeffs_to_string(multiply_pol_classic(c1, c2))


def multiply_int_karatsuba(s1, s2):
    c1 = string_to_coeffs(s1)
    c2 = string_to_coeffs(s2)
    return coeffs_to_string(multiply_pol_karatsuba(c1, c2))


# Тест
if __name__ == "__main__":
    print(f"123 * 456 = {multiply_int_classic('123', '456')}")
    print(f"123 * 456 = {multiply_int_karatsuba('123', '456')}")