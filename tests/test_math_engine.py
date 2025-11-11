import sympy as sp

from core.math_engine import compute_root


class TestMathEngine:

    def test_square_root(self):
        assert compute_root(9, 2) == 3

    def test_negative_even_degree(self):
        res = compute_root(-8, 2)
        assert not res.is_real
        assert res.has(sp.I)
        assert abs(res) == sp.sqrt(8)

    def test_default_degree(self):
        assert compute_root(16) == 4
