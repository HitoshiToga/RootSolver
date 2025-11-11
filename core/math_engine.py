import sympy as sp

def compute_root(value, degree=2):
    """Вычисляет корень n-й степени из числа"""
    try:
        return sp.root(value, degree)
    except Exception as e:
        raise ValueError(f"Ошибка при вычислении корня: {e}")
