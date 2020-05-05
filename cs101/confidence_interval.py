"""confidence_interval.py: namedtuple type for confidence interval."""
from numbers import Real
from typing import NamedTuple


class CI(NamedTuple):
    """namedtuple for representing a confidence interval."""

    lo: Real
    mid: Real
    hi: Real

    def __repr__(self) -> str:
        """Return repr(self)."""
        return f"CI({self.lo}, {self.mid}, {self.hi})"

    def __str__(self) -> str:
        """Return str(self)."""
        return f"{self.lo}|---------{self.mid}---------|{self.hi}"

    def __contains__(self, value: Real) -> bool:
        """Return value in self."""
        return self.lo < value < self.hi

    def __lt__(self, other: "CI") -> bool:
        """Return self < other."""
        return self.hi < other.lo

    def __gt__(self, other: "CI") -> bool:
        """Return self > other."""
        return self.lo > other.hi

    def __eq__(self, other: "CI") -> bool:
        """Return self == other."""
        return (self.lo in other) or (self.hi in other)

    def __le__(self, other):
        """Return self <= other.  Don't implement."""
        raise NotImplementedError("Cannot compare CIs with <=")

    def __ge__(self, other):
        """Return self >= other.  Don't implement."""
        raise NotImplementedError("Cannot compare CIs with >=")
