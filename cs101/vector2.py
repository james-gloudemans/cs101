"""vector2.py: class for 2D vectors."""
import math
from collections import namedtuple
from collections.abc import Sequence
from numbers import Real
from typing import NamedTuple


class Vector2(NamedTuple):
    """Representation of vector in 2D space."""

    x: int
    y: int

    def __repr__(self) -> str:
        """Return repr(self)."""
        return f"Vector2({self.x}, {self.y})"

    @property
    def r(self) -> float:
        """Return the length of the vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def theta(self) -> float:
        """Return the polar angle in radians (-pi, pi]."""
        return math.atan2(self.y, self.x)

    def __neg__(self) -> "Vector2":
        """Return -self."""
        return Vector2(-self.x, -self.y)

    def __abs__(self) -> float:
        """Return abs(self)."""
        return self.r

    def __add__(self, other) -> "Vector2":
        """Return self + other."""
        if Vector2._is_vector2like(other):
            return Vector2(self.x + other[0], self.y + other[1])
        raise TypeError(f"Cannot add types Vector2 and {type(other)}")

    def __sub__(self, other) -> "Vector2":
        """Return self - other."""
        if Vector2._is_vector2like(other):
            return Vector2(self.x - other[0], self.y - other[1])
        raise TypeError(f"Cannot subtract types Vector2 and {type(other)}")

    def __mul__(self, other):
        """Return self*other, dot product if other is Vector2 or len 2 sequence."""
        if isinstance(other, Real):
            return Vector2(self.x * other, self.y * other)
        if Vector2._is_vector2like(other):
            return self.x * other[0] + self.y * other[1]
        raise TypeError(f"Cannot multiply types Vector2 and {type(other)}")

    def __truediv__(self, other) -> "Vector2":
        """Return self / other."""
        if not isinstance(other, Real):
            raise TypeError(f"Cannot mulitply types Vector2 and {type(other)}")
        return Vector2(self.x / other, self.y / other)

    def __radd__(self, other) -> "Vector2":
        """Return other + self."""
        return self + other

    def __rsub__(self, other) -> "Vector2":
        """Return other - self."""
        return Vector2(other[0] - self.x, other[1] - self.y)

    def __rmul__(self, other):
        """Return other * self."""
        return self * other

    def __iadd__(self, other) -> "Vector2":
        """Evaluate self += other."""
        return self + other

    def __isub__(self, other) -> "Vector2":
        """Evaluate self -= other."""
        return self - other

    def __imul__(self, other):
        """Evaluate self *= other."""
        return self * other

    def __itruediv__(self, other: Real) -> "Vector2":
        """Evaluate self /= other."""
        return self / other

    def angle_between(self, other) -> Real:
        """Return the angle between self and other."""
        if isinstance(other, Vector2):
            return math.acos(self * other / (self.r * other.r))
        raise TypeError(
            f"Cannot find the angle between types Vector2 and {type(other)}"
        )

    def rotate(self, theta: Real, *, radians=True):
        """Return a new vector rotated by theta counterclockwise."""
        if not radians:
            theta *= 2 * math.pi / 360.0
        x = self.x * math.cos(theta) - self.y * math.sin(theta)
        y = self.x * math.sin(theta) + self.y * math.cos(theta)
        return Vector2(x, y)

    def unit(self) -> "Vector2":
        """Return the unit vector of self."""
        return self / self.r

    def project(self, other: "Vector2") -> "Vector2":
        """Vector projection of self onto other."""
        if not isinstance(other, Vector2):
            raise TypeError(f"Cannot project Vector2 onto type {type(other)}")
        return (self * other.unit()) * other.unit()

    def reject(self, other: "Vector2") -> "Vector2":
        """Vector rejection of self from other."""
        if not isinstance(other, Vector2):
            raise TypeError(f"Cannot reject Vector2 from type {type(other)}")
        return self - self.project(other)

    @staticmethod
    def _is_vector2like(other) -> bool:
        """Does other look like a 2D vector?"""
        if isinstance(other, Vector2):
            return True
        if isinstance(other, Sequence) and len(other) == 2:
            return True
        return False
