"""bstree.py: Implements a binary search tree."""
# Standard Library
from abc import ABC, abstractmethod
from typing import Any, Iterable, Iterator, MutableMapping, Optional, Tuple, TypeVar

# Third party libraries

# Local imports
from btree import BTree


class Comparable(ABC):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass


K = TypeVar("K", bound=Comparable)
V = TypeVar("V")


class BSTMap(MutableMapping[K, V]):
    """A Binary search tree."""

    def __init__(self, iterable: Optional[Iterable[Tuple[K, V]]]) -> None:
        """Initialize a new empty tree."""
        self.left: Optional["BSTMap"] = None
        self.right: Optional["BSTMap"] = None
        if iterable is not None:
            iterator = iter(iterable)
            init = next(iterator)
            self.key: Optional[K] = init[0]
            self.value: Optional[V] = init[1]
            for k, v in iterator:
                self[k] = v
        else:
            self.key = None
            self.value = None

    def __getitem__(self, key: K) -> V:
        """Return self[key]."""
        if self.key == key:
            return self.value
        elif key < self.key:
            if self.left is not None:
                return self.left[key]
            else:
                raise KeyError(f"{key}")
        else:  # key > self.key
            if self.right is not None:
                return self.right[key]
            else:
                raise KeyError(f"{key}")

    def __delitem__(self, key: K) -> None:
        """del self[key]."""
        # I guess I need parents cuz this is stupid, ugh
        # Find del_node
        if key < self.key:
            if self.left is not None:
                if self.left.key == key:
                    if self.left.left is None and self.left.right is None:
                        self.left = None
                    elif self.left.left is None:
                        self.left = self.left.left
                    elif self.left.right is None:
                        self.left = self.left.right
                    else:
                        successor_it = self.left._nodes()
                        successor = next(successor_it)
                        successor_child = next(successor_it)
                        successor_parent = next(successor_it)
                        successor_parent.left = successor.right
                        self.left = successor
                else:
                    del self.left[key]
            else:
                raise KeyError(f"{key}")
        elif self.key < key:
            if self.right is not None:
                if self.right.key == key:
                    if self.right.left is None and self.right.right is None:
                        self.right = None
                    elif self.right.left is None:
                        self.right = self.right.left
                    elif self.right.right is None:
                        self.right = self.right.right
                    else:
                        successor_it = self.right._nodes()
                        successor = next(successor_it)
                        successor_child = next(successor_it)
                        successor_parent = next(successor_it)
                        successor_parent.left = successor.right
                        self.right = successor
                else:
                    del self.right[key]
            else:
                raise KeyError(f"{key}")
        elif self.left is None and self.right is None:  # key == self.key
            # Delete only node in tree
            self.key = None
            self.value = None

    def __setitem__(self, key: K, value: V) -> None:
        """Set self[key] = value"""
        if self.key == key:
            self.value = value
        elif key < self.key:
            if self.left is None:
                self.left = BSTMap(((key, value),))
            else:
                self.left[key] = value
        else:
            if self.right is None:
                self.right = BSTMap(((key, value),))
            else:
                self.right[key] = value

    def __iter__(self) -> Iterator[K]:
        """Return iter(self)."""
        if self.left is not None:
            yield from self.left
        yield self.key
        if self.right is not None:
            yield from self.right

    def __len__(self) -> int:
        """Return len(self)."""
        return len(list(self))

    def __str__(self) -> str:
        """Return str(self)."""
        return str(dict(self))

    def __repr__(self) -> str:
        """Return repr(self)."""
        return f"'{str(self)}'"

    def keys(self) -> Iterator[K]:
        """Return an iterator over the keys."""
        return iter(self)

    def values(self) -> Iterator[V]:
        """Return an iterator over the values."""
        if self.left is not None:
            yield from self.left
        yield self.value
        if self.right is not None:
            yield from self.right

    def items(self) -> Iterator[Tuple[K, V]]:
        """Return an iterator over key, value tuples."""
        if self.left is not None:
            yield from self.left
        yield self.key, self.value
        if self.right is not None:
            yield from self.right

    def _isBST(self) -> bool:
        """Does self satisfy the tree invariant?"""
        for node in self._nodes():
            if node.left and node.key < node.left.key:
                return False
            if node.right and node.right.key < node.key:
                return False
        return True

    def _nodes(self) -> Iterator["BSTMap"]:
        """Return an iterator over the nodes of the tree in-order."""
        if self.left is not None:
            yield from self.left
        yield self
        if self.right is not None:
            yield from self.right


if __name__ == "__main__":

    init = [(1, 1), (3, 3), (2, 2)]
    tree = BSTMap[int, int](init)
    print(tree)
    tree[5] = 5
    print(tree)
    del tree[1]
    print(tree)
