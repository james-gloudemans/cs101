"""proportion.py: Module for representing a proportion as a namedtuple."""
# Standard Library
from typing import NamedTuple

# Third  party libraries

# Local libraries


class Proportion(NamedTuple):
    """Class for representing a proportion."""

    correct: int = 0
    attempts: int = 0

    def __repr__(self) -> str:
        """Return repr(self)."""
        return f"Proportion({self.correct}, {self.attempts})"

    def __str__(self) -> str:
        """Return str(self)."""
        return f"({self.correct} / {self.attempts})"

    def __add__(self, other: "Proportion") -> "Proportion":
        """Return self + other."""
        if not isinstance(other, Proportion):
            raise TypeError(
                f"can only add Proportion (not {type(other)}) to Proportion)"
            )
        result = Proportion(
            self.correct + other.correct, self.attempts + other.attempts
        )
        if result.correct > result.attempts:
            raise ValueError("Proportion must be in [0, 1]")
        return result

    def __iadd__(self, other: "Proportion") -> "Proportion":
        """Set self to self + other."""
        if not isinstance(other, Proportion):
            raise TypeError(
                f"can only add Proportion (not {type(other)}) to Proportion)"
            )
        return self + other

    def __mul__(self, other: "Proportion") -> "Proportion":
        """Return self * other."""
        if not isinstance(other, Proportion):
            raise TypeError(
                f"can only multiply Proportion (not {type(other)}) to Proportion)"
            )
        return Proportion(self.correct * other.correct, self.attempts * other.attempts)

    def __imul__(self, other: "Proportion") -> "Proportion":
        """Set self to self * other."""
        if not isinstance(other, Proportion):
            raise TypeError(
                f"can only multiply Proportion (not {type(other)}) to Proportion)"
            )
        return self * other
