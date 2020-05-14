"""bstree.py: Implements a binary search tree."""
# Standard Library
from typing import Iterator, MutableMapping, TypeVar

# Third party libraries

# Local imports
from btree import BTree

K = TypeVar("K")
V = TypeVar("V")


class BST(MutableMapping[K, V]):
    """A Binary search tree."""

    def __init__(self) -> None:
        """Initialize a new empty tree."""
        super().__init__()

    def __getitem__(self, key: K) -> V:
        """Return self[key]."""
        return NotImplementedError

    def __delitem__(self, key: K) -> None:
        """del self[key]."""
        pass

    def __setitem__(self, key: K, value: V) -> None:
        """Set self[key] = value"""
        pass

    def __iter__(self) -> Iterator[K]:
        """Return iter(self)."""
        return NotImplementedError

    def __len__(self) -> int:
        """Return len(self)."""
        return len(list(self))

    def keys(self) -> Iterator[K]:
        """Return an iterator over the keys."""
        return iter(self)

    def values(self) -> Iterator[V]:
        """Return an iterator over the values."""
        return NotImplementedError

    def items(self) -> Iterator[Tuple[K, V]]:
        """Return an iterator over key, value tuples."""
        return NotImplementedError

    def _isBST(self) -> bool:
        """Does self satisfy the tree invariant?"""
        return NotImplementedError


if __name__ == "__main__":

    tree = BST()
