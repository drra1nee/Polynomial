import time
import random
from lab1_1 import eval_pol_direct, eval_pol_horner
from lab1_2 import multiply_pol_classic, multiply_pol_karatsuba
from lab1_3 import multiply_int_classic, multiply_int_karatsuba

def time_func(func, *args, iterations=5):
    """Замер среднего времени выполнения"""
    start = time.perf_counter()
    for _ in range(iterations):
        func(*args)
    return (time.perf_counter() - start) / iterations

def run_benchmarks():
    print("=== Бенчмарк ===\n")

    print("1. Умножение многочленов:")
    for n in [64, 256, 1024]:
        a = [random.randint(1, 10) for _ in range(n)]
        b = [random.randint(1, 10) for _ in range(n)]
        t1 = time_func(multiply_pol_classic, a, b)
        t2 = time_func(multiply_pol_karatsuba, a, b)
        status = "Карацуба быстрее" if t2 < t1 else "Классика быстрее"
        print(f"   N={n:<4} Классика: {t1:.4f}с | Карацуба: {t2:.4f}с | {status}")

    print("\n2. Вычисление P(x) (степень 10^4, x=2):")
    coeffs = [random.randint(1, 10) for _ in range(10000)]
    t1 = time_func(eval_pol_direct, coeffs, 2)
    t2 = time_func(eval_pol_horner, coeffs, 2)
    print(f"   Прямой: {t1:.3f}с | Горнер: {t2:.3f}с | Горнер быстрее в {t1 / t2:.0f} раз")

    print("\n3. Умножение больших чисел:")
    for n in [128, 512]:
        s1 = ''.join([str(random.randint(1, 9)) for _ in range(n)])
        s2 = ''.join([str(random.randint(1, 9)) for _ in range(n)])
        t1 = time_func(multiply_int_classic, s1, s2)
        t2 = time_func(multiply_int_karatsuba, s1, s2)
        status = "Карацуба быстрее" if t2 < t1 else "Классика быстрее"
        print(f"   Длина={n:<3} Классика: {t1:.4f}с | Карацуба: {t2:.4f}с | {status}")


if __name__ == "__main__":
    run_benchmarks()