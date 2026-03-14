"""
Три главных графика для анализа квадратурных формул.
"""

import numpy as np
import matplotlib.pyplot as plt
from quadrature import compute_results
from test_functions import exact_values

results = compute_results()
exact = exact_values()

def plot_smoothness_effect(results, exact):
    """
    Показывает, как гладкость функции влияет на точность метода Симпсона
    """
    plt.figure(figsize=(10, 6))
    functions = [
        ('f1', 'Полином 5-й степени (очень гладкая)', 'blue', 'o-'),
        ('f3', 'exp(-x²) (гладкая)', 'green', 's-'),
        ('f2', 'sin⁻²(x) (средняя)', 'red', '^-')
    ]

    for key, label, color, marker in functions:
        n = results[key]['n']
        errors = [abs(v - exact[key]) for v in results[key]['simp']]  # Симпсон
        plt.loglog(n, errors, marker, color=color, label=label, linewidth=2, markersize=6)
    n_theor = np.array([4, 16, 64])
    plt.loglog(n_theor, 1 / n_theor ** 4, 'k--', alpha=0.3, label='O(1/n⁴)')

    plt.xlabel('Количество отрезков n', fontsize=12)
    plt.ylabel('Погрешность', fontsize=12)
    plt.title('Влияние гладкости функции на точность метода Симпсона', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    plt.savefig('1_smoothness_effect.png', dpi=150)
    plt.show()

def plot_methods_comparison(results, exact):
    """
    Сравнивает все 4 метода на функции sin⁻²(x) (средняя гладкость)
    """
    plt.figure(figsize=(10, 6))

    methods = [
        ('mid', 'Прямоугольники (2-й порядок)', 'blue', 'o-'),
        ('trap', 'Трапеции (2-й порядок)', 'green', 's-'),
        ('simp', 'Симпсон (4-й порядок)', 'red', '^-'),
        ('three', '3/8 (4-й порядок)', 'purple', 'd-')
    ]

    key = 'f2'
    exact_val = exact[key]

    for method, label, color, marker in methods:
        n = results[key]['n']
        errors = [abs(v - exact_val) for v in results[key][method]]
        plt.loglog(n, errors, marker, color=color, label=label, linewidth=2, markersize=6)

    n_theor = np.array([4, 16, 64])
    plt.loglog(n_theor, 1 / n_theor ** 2, 'k--', alpha=0.3, label='O(1/n²)')
    plt.loglog(n_theor, 1 / n_theor ** 4, 'k:', alpha=0.3, label='O(1/n⁴)')

    plt.xlabel('Количество отрезков n', fontsize=12)
    plt.ylabel('Погрешность', fontsize=12)
    plt.title('Сравнение методов на функции sin⁻²(x)', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    plt.savefig('2_methods_comparison.png', dpi=150)
    plt.show()

def plot_theory_vs_practice(results, exact):
    """
    Сравнивает фактическую погрешность с теоретической оценкой
    """
    plt.figure(figsize=(10, 6))
    key = 'f1'
    method = 'mid'
    exact_val = exact[key]

    n = np.array(results[key]['n'])
    errors = np.array([abs(v - exact_val) for v in results[key][method]])
    theory = 100 / (3 * n**2)  
    mask = errors > 1e-15
    plt.loglog(n[mask], errors[mask], 'ro-', label='Фактическая погрешность', linewidth=2, markersize=6)
    plt.loglog(n, theory, 'b--', label=f'Теоретическая оценка O(100/3n²)', linewidth=2)

    plt.xlabel('Количество отрезков n', fontsize=12)
    plt.ylabel('Погрешность', fontsize=12)
    plt.title('Метод прямоугольников на полиноме 5-й степени\nСравнение теории и практики', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    plt.savefig('3_theory_vs_practice.png', dpi=150)
    plt.show()

if __name__ == "__main__":
    plot_smoothness_effect(results, exact)
    plot_methods_comparison(results, exact)
    plot_theory_vs_practice(results, exact)
