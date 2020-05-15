"""bstmap.py: Implements a binary search tree."""
# Standard Library
from abc import ABC, abstractmethod
from typing import Any, Iterable, Iterator, MutableMapping, Optional, Tuple, TypeVar

# Third party libraries

# Local imports


class Hashable(ABC):
    @abstractmethod
    def __hash__(self) -> int:
        pass


K = TypeVar("K", bound=Hashable)


class BSTMap(MutableMapping[K, Any]):
    """A Binary search tree."""

    def __init__(self, iterable: Optional[Iterable[Tuple[K, Any]]]) -> None:
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

    def __gt__(self, other) -> bool:
        """Return self > other."""
        if isinstance(other, BSTMap):
            return hash(self.key) > hash(other.key)
        if isinstance(other, Hashable):
            return hash(self.key) > hash(other)
        return False

    def __eq__(self, other) -> bool:
        """Return self == other."""
        if isinstance(other, Hashable):
            return hash(self.key) == hash(other)
        elif isinstance(other, BSTMap):
            return self.key == other.key
        return False

    def __getitem__(self, key: K) -> Any:
        """Return self[key]."""
        return self._get_node(key).value

    def _get_node(self, key: K) -> "BSTMap":
        """Get the node associated with key."""
        if self.key == key:
            return self
        if self < key:
            if self.left is not None:
                return self.left._get_node(key)
            else:
                raise KeyError(f"{key}")
        if self.right is not None:
            return self.right._get_node(key)
        else:
            raise KeyError(f"{key}")

    def _set_parent_ref(self, node: Optional["BSTMap"]) -> None:
        """Remove the reference to self from its parent."""
        if self.parent is not None:
            if self.parent.left == self:
                self.parent.left = node
            if self.parent.right == self:
                self.parent.right = node

    def __delitem__(self, key: K) -> None:
        """del self[key]."""
        node = self._get_node(key)
        if node.left is None and node.right is None:
            node._set_parent_ref(None)
        elif node.left is None:
            node._set_parent_ref(node.right)
        elif node.right is None:
            node._set_parent_ref(node.left)
        else:  # Node has two children
            suc = next(node.right._nodes())
            suc._set_parent_ref(suc.right)
            suc.left = node.left
            suc.right = node.right
            suc.parent = node.parent
            node._set_parent_ref(suc)

    def __setitem__(self, key: K, value: Any) -> None:
        """Set self[key] = value"""
        if self == key:
            self.value = value
        elif self > key:
            if self.left is None:
                self.left = BSTMap(((key, value),))
                self.left.parent = self
            else:
                self.left[key] = value
        else:
            if self.right is None:
                self.right = BSTMap(((key, value),))
                self.right.parent = self
            else:
                self.right[key] = value

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

    def values(self) -> Iterator[Any]:
        """Return an iterator over the values."""
        if self.left is not None:
            yield from self.left
        yield self.value
        if self.right is not None:
            yield from self.right

    def items(self) -> Iterator[Tuple[K, Any]]:
        """Return an iterator over key, value tuples."""
        if self.left is not None:
            yield from self.left
        if self.key is not None:
            yield self.key, self.value
        if self.right is not None:
            yield from self.right

    def _isBST(self) -> bool:
        """Does self satisfy the tree invariant?"""
        for node in self._nodes():
            if node.left and node < node.left:
                return False
            if node.right and node > node.right:
                return False
        return True

    def _nodes(self) -> Iterator["BSTMap"]:
        """Return an iterator over the nodes of the tree in-order."""
        if self.left is not None:
            yield from self.left._nodes()
        yield self
        if self.right is not None:
            yield from self.right._nodes()


if __name__ == "__main__":
    pass
