"""test_vector2.py: Tests for vector2.py."""
import math

from cs101.vector2 import Vector2


x = Vector2(1, 0)
y = Vector2(0, 1)
v = Vector2(3, 4)


def test_unary():
    """Test unary operators."""
    assert -v == Vector2(-3, -4)
    assert abs(v) == 5


def test_add_sub():
    """Test addition and subtraction."""
    assert x + y == Vector2(1, 1)
    assert x + y == y + x
    assert x - y == Vector2(1, -1)
    assert x - y == -(y - x)
    w = x + y
    w += x
    assert w == Vector2(2, 1)
    w -= x
    assert w == Vector2(1, 1)


def test_mul_div():
    """Test multiply and divide."""
    assert x * y == 0
    assert v * x == v.x
    assert v * y == v.y
    assert 2 * v == Vector2(6, 8)
    assert v * 2 == 2 * v
    assert v / 2 == Vector2(1.5, 2)
    w = x + y
    w /= 2
    assert w == Vector2(0.5, 0.5)
    w *= 2
    assert w == Vector2(1, 1)


def test_props():
    """Test properties."""
    assert x.r == y.r == 1
    assert v.r == 5
    assert (x + y).r == math.sqrt(2)
    assert x.theta == 0
    assert y.theta == math.pi / 2
    assert (-x).theta == math.pi
    assert (-y).theta == -math.pi / 2


if __name__ == "__main__":
    test_unary()
    test_add_sub()
    test_mul_div()
    test_props()
