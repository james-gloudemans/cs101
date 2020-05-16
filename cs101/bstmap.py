"""bstmap.py: Implements a binary search tree."""
# Standard Library
from collections.abc import Hashable
from functools import total_ordering
from typing import Any, Iterable, Iterator, MutableMapping, Optional, Tuple, TypeVar

# Third party libraries

# Local imports


K = TypeVar("K", bound=Hashable)


@total_ordering
class BSTMap(MutableMapping[K, Any]):
    """A Binary search tree."""

    def __init__(self, iterable: Optional[Iterable[Tuple[K, Any]]] = None) -> None:
        """Initialize a new empty tree."""
        self.left: Optional["BSTMap"] = None
        self.right: Optional["BSTMap"] = None
        self.parent: Optional["BSTMap"] = None
        self.key: Optional[K] = None
        self.value: Any = None
        if iterable is not None:
            iterator = iter(iterable)
            init = next(iterator)
            self.key = init[0]
            self.value = init[1]
            for k, v in iterator:
                self[k] = v

    def __lt__(self, other) -> bool:
        """Return self < other."""
        if isinstance(other, BSTMap):
            return hash(self.key) < hash(other.key)
        if isinstance(other, Hashable):
            return hash(self.key) < hash(other)
        return False

    def __eq__(self, other) -> bool:
        """Return self == other."""
        if isinstance(other, BSTMap):
            return hash(self.key) == hash(other.key)
        if isinstance(other, Hashable):
            return hash(self.key) == hash(other)
        return False

    def __getitem__(self, key: K) -> Any:
        """Return self[key]."""
        return self._get_node(key).value

    def __contains__(self, key) -> bool:
        """Return key in self."""
        if self == key:
            return True
        elif self < key:
            if self.right is not None:
                return key in self.right
            else:
                return False
        else:
            if self.left is not None:
                return key in self.left
            else:
                return False

    def __delitem__(self, key: K) -> None:
        """del self[key]."""
        node = self._get_node(key)
        if node.left is None and node.right is None:
            if node.parent is None:
                node.key = None
                node.value = None
            else:
                if node.parent.left == node:
                    node.parent.left = None
                elif node.parent.right == node:
                    node.parent.right = None
        elif node.left is None and node.right is not None:
            node.key = node.right.key
            node.value = node.right.value
            node.left = node.right.left
            if node.left is not None:
                node.left.parent = node
            node.right = node.right.right
            if node.right is not None:
                node.right.parent = node
        elif node.right is None and node.left is not None:
            node.key = node.left.key
            node.value = node.left.value
            node.right = node.left.right
            if node.right is not None:
                node.right.parent = node
            node.left = node.left.left
            if node.left is not None:
                node.left.parent = node
        elif node.right is not None and node.left is not None:
            suc = next(node.right._nodes())
            node.key = suc.key
            node.value = suc.value
            if suc.right is not None:
                suc.key = suc.right.key
                suc.value = suc.right.value
                suc.left = suc.right.left
                suc.right = suc.right.right
                if suc.left is not None:
                    suc.left.parent = suc
                if suc.right is not None:
                    suc.right.parent = suc
            elif suc.parent is not None:
                if suc.parent.right == suc:
                    suc.parent.right = None
                elif suc.parent.left == suc:
                    suc.parent.left = None

    def __setitem__(self, key: K, value: Any) -> None:
        """Set self[key] = value"""
        if self == key:
            self.value = value
        elif self < key:
            if self.right is not None:
                self.right[key] = value
            else:
                self.right = BSTMap(((key, value),))
                self.right.parent = self
        else:
            if self.left is not None:
                self.left[key] = value
            else:
                self.left = BSTMap(((key, value),))
                self.left.parent = self

    def __iter__(self) -> Iterator[K]:
        """Return iter(self)."""
        if self.left is not None:
            yield from self.left
        if self.key is not None:
            yield self.key
        if self.right is not None:
            yield from self.right

    def __len__(self) -> int:
        """Return len(self)."""
        return len(dict(self))

    def __str__(self) -> str:
        """Return str(self)."""
        return str(dict(self))

    def __repr__(self) -> str:
        """Return repr(self)."""
        return f"'{str(self)}'"

    def keys(self) -> Iterator[K]:
        """Return an iterator over the keys."""
        return iter(self)

    def values(self) -> Iterator[Any]:
        """Return an iterator over the values."""
        if self.left is not None:
            yield from self.left.values()
        yield self.value
        if self.right is not None:
            yield from self.right.values()

    def items(self) -> Iterator[Tuple[K, Any]]:
        """Return an iterator over key, value tuples."""
        if self.left is not None:
            yield from self.left.items()
        if self.key is not None:
            yield self.key, self.value
        if self.right is not None:
            yield from self.right.items()

    def _isBST(self) -> bool:
        """Does self satisfy the tree invariant?"""
        for node in self._nodes():
            if node.left is not None and node <= node.left:
                print(node.key, node.left.key)
                return False
            if node.right is not None and node >= node.right:
                print(node.key, node.right.key)
                return False
        return True

    def _nodes(self) -> Iterator["BSTMap"]:
        """Return an iterator over the nodes of the tree in-order."""
        if self.left is not None:
            yield from self.left._nodes()
        yield self
        if self.right is not None:
            yield from self.right._nodes()

    def _get_node(self, key: K) -> "BSTMap":
        """Get the node associated with key."""
        if self == key:
            return self
        elif self < key:
            if self.right is not None:
                return self.right._get_node(key)
            else:
                raise KeyError(f"{key}")
        else:
            if self.left is not None:
                return self.left._get_node(key)
            else:
                raise KeyError(f"{key}")


if __name__ == "__main__":

    lst = [(5, 5), (1, 1), (7, 7), (2, 2), (3, 3), (6, 6), (4, 4)]
    tree = BSTMap(lst)
    print(tree._get_node(2) == tree[2])
    print(tree)
    # pass
