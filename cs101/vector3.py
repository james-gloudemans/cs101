"""vector3.py: A 3D vector representation."""
# Standard library
import math
from collections.abc import Sequence
from numbers import Real
from typing import NamedTuple


class Vector3(NamedTuple):
    """A 3D vector."""

    x: Real
    y: Real
    z: Real

    @property
    def r(self):
        """Vector magnitude of self."""
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __repr__(self) -> str:
        """Return repr(self)."""
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def __str__(self) -> str:
        """Return str(self)."""
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other) -> "Vector3":
        """Return self + other."""
        if Vector3._is_vector3like(other):
            return Vector3(self.x + other[0], self.y + other[1], self.z + other[2])
        raise TypeError(f"Cannot add types Vector3 and {type(other)}")

    def __sub__(self, other) -> "Vector3":
        """Return self - other."""
        if Vector3._is_vector3like(other):
            return Vector3(self.x - other[0], self.y - other[1], self.z - other[2])
        raise TypeError(f"Cannot subtract types Vector3 and {type(other)}")

    def __mul__(self, other):
        "Return self * other.  Dot product if other is len 3 sequence"
        if Vector3._is_vector3like(other):
            return self.x * other[0] + self.y * other[1] + self.z * other[2]
        if isinstance(other, Real):
            return Vector3(self.x * other, self.y * other, self.z * other)
        raise TypeError(f"Cannot multiply types Vector3 and {type(other)}")

    def __truediv__(self, other: Real) -> "Vector3":
        """Return self / other."""
        if isinstance(other, Real):
            return Vector3(self.x / other, self.y / other, self.z / other)
        raise TypeError(f"Cannot divide types Vector3 and {type(other)}")

    def __radd__(self, other) -> "Vector3":
        """Return other + self."""
        if Vector3._is_vector3like(other):
            return self + other
        raise TypeError(f"Cannot add types {type(other)} and Vector3")

    def __rsub__(self, other) -> "Vector3":
        """Return other - self."""
        if Vector3._is_vector3like(other):
            return Vector3(other[0] - self.x, other[1] - self.y, other[2] - self.z)
        raise TypeError(f"Cannot subtract types {type(other)} and Vector3")

    def __rmul__(self, other):
        """Return other * self.  Dot product if other is len 3 sequence."""
        return self * other

    def __iadd__(self, other) -> "Vector3":
        """Set self to self + other."""
        return self + other

    def __isub__(self, other) -> "Vector3":
        """Set self to self - other."""
        return self - other

    def __imul__(self, other):
        """Set self to self * other."""
        return self * other

    def __itruediv__(self, other) -> "Vector3":
        """Set self to self / other."""
        return self / other

    @staticmethod
    def _is_vector3like(other) -> bool:
        if isinstance(other, Vector3):
            return True
        if isinstance(other, Sequence) and len(other) == 3:
            return True
        return False
