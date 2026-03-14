import numpy as np
from test_functions import *


def midpoint_rule(f, a, b, n):
    """Составная формула средних прямоугольников"""
    h = (b - a) / n
    x_mid = np.linspace(a + h / 2, b - h / 2, n)
    return h * np.sum(f(x_mid))


def trapezoidal_rule(f, a, b, n):
    """Составная формула трапеций"""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])


def simpson_rule(f, a, b, n):
    """Составная формула Симпсона"""
    n_original = n
    if n % 2 != 0:
        n = n + 1
        print(f"  Метод Симпсона: n={n_original} нечетное, используем n={n}")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    result = h / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]))
    return result


def three_eights_rule(f, a, b, n):
    """Составная формула трех восьмых"""
    n_original = n
    if n % 3 != 0:
        n = n + (3 - n % 3)
        print(f"  Метод 3/8: n={n_original} не кратно 3, используем n={n}")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    result = 0
    for i in range(0, n, 3):
        result += (3 * h / 8) * (y[i] + 3 * y[i + 1] + 3 * y[i + 2] + y[i + 3])
    return result


def compute_results():
    """Вычисляет интегралы для всех функций"""

    functions = [
        (f1, 0, 2, 'f1'),
        (f2, 0.5, 2, 'f2'),
        (f3, 0, 3, 'f3'),
    ]

    # УБИРАЕМ 'f4' - его нет в functions!
    results = {
        'f1': {'mid': [], 'trap': [], 'simp': [], 'three': [], 'n': []},
        'f2': {'mid': [], 'trap': [], 'simp': [], 'three': [], 'n': []},
        'f3': {'mid': [], 'trap': [], 'simp': [], 'three': [], 'n': []}
        # 'f4' удален!
    }

    print("Вычисляем интегралы...")
    for n in range(1, 256, 4):
        n_simp = n if n % 2 == 0 else n + 1
        n_three = n if n % 3 == 0 else n + (3 - n % 3)

        for f, a, b, key in functions:
            mid_val = midpoint_rule(f, a, b, n)
            trap_val = trapezoidal_rule(f, a, b, n)
            simp_val = simpson_rule(f, a, b, n_simp)
            three_val = three_eights_rule(f, a, b, n_three)

            results[key]['mid'].append(mid_val)
            results[key]['trap'].append(trap_val)
            results[key]['simp'].append(simp_val)
            results[key]['three'].append(three_val)
            results[key]['n'].append(n)

    print("Готово!")
    return results


if __name__ == "__main__":
    res = compute_results()
    print("\nКлючи в results:", res.keys())
    print(f"Для f1: {len(res['f1']['n'])} значений")
    print(f"Для f2: {len(res['f2']['n'])} значений")
    print(f"Для f3: {len(res['f3']['n'])} значений")