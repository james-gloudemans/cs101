"""bstmap.py: Implements a binary search tree."""
# Standard Library
from collections.abc import Hashable
from functools import total_ordering
from typing import (
    Any,
    Iterable,
    Iterator,
    MutableMapping,
    Optional,
    Tuple,
    TypeVar,
)

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
                node._delete_from_parent()
        elif node.left is None and node.right is not None:
            node._replace_with_right()
        elif node.right is None and node.left is not None:
            node._replace_with_left()
        else:  # node has two children
            suc = next(node.right._nodes())  # type: ignore
            node.key = suc.key
            node.value = suc.value
            if suc.right is not None:
                suc._replace_with_right()
            elif suc.parent is not None:
                suc._delete_from_parent()

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

    def keys(self) -> Iterator[K]:  # type: ignore
        """Return an iterator over the keys."""
        return iter(self)

    def values(self) -> Iterator[Any]:  # type: ignore
        """Return an iterator over the values."""
        if self.left is not None:
            yield from self.left.values()
        yield self.value
        if self.right is not None:
            yield from self.right.values()

    def items(self) -> Iterator[Tuple[K, Any]]:  # type: ignore
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
            if node.left is not None and node <= node.left:  # type: ignore
                print(node.key, node.left.key)
                return False
            if node.right is not None and node >= node.right:  # type: ignore
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

    def _replace_with_right(self):
        """Replace self with its right child."""
        self.key = self.right.key
        self.value = self.right.value
        self.left = self.right.left
        if self.left is not None:
            self.left.parent = self
        self.right = self.right.right
        if self.right is not None:
            self.right.parent = self

    def _replace_with_left(self):
        """Replace self with its left child."""
        self.key = self.left.key
        self.value = self.left.value
        self.right = self.left.right
        if self.right is not None:
            self.right.parent = self
        self.left = self.left.left
        if self.left is not None:
            self.left.parent = self

    def _delete_from_parent(self):
        """Delete self from its parent node."""
        if self.parent.left == self:
            self.parent.left = None
        if self.parent.right == self:
            self.parent.right = None


if __name__ == "__main__":

    lst = [(5, 5), (1, 1), (7, 7), (2, 2), (3, 3), (6, 6), (4, 4)]
    tree = BSTMap(lst)
    print(tree._get_node(2) == tree[2])
    print(tree)
    # pass
