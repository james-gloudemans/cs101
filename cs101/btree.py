"""btree.py: binary tree representation."""
# Standard library
from collections import deque
from typing import Generic, Iterator, Optional, TypeVar

# Third party libraries

# Local libraries

T = TypeVar("T")


class BTree(Generic[T]):
    """Binary tree node."""

    def __init__(
        self,
        data: T = None,
        *,
        left_child: Optional["BTree"] = None,
        right_child: Optional["BTree"] = None
    ) -> None:
        """Initialize new Binary tree."""
        self.left = left_child
        self.right = right_child
        self.data = data

    def __repr__(self) -> str:
        """Return repr(self)."""
        left_repr = self.left and hex(id(self.left))
        right_repr = self.right and hex(id(self.right))
        return "<BTree object at {}, data={}, left={}, right={}>".format(
            hex(id(self)), self.data, left_repr, right_repr
        )

    def __str__(self) -> str:
        """Return str(self)."""
        return repr(self)

    def __iter__(self) -> Iterator[T]:
        """Return iter(self)."""
        return self.inorder()

    def __len__(self) -> int:
        """Return len(self)."""
        return len(list(iter(self)))

    def inorder(self) -> Iterator[T]:
        """Perform inorder tree traversal."""
        if self.left is not None:
            yield from self.left.inorder()
        yield self.data
        if self.right is not None:
            yield from self.right.inorder()

    def preorder(self) -> Iterator[T]:
        """Perform preorder tree traversal."""
        yield self.data
        if self.left is not None:
            yield from self.left.preorder()
        if self.right is not None:
            yield from self.right.preorder()

    def postorder(self) -> Iterator[T]:
        """Perform postorder tree traversal."""
        if self.left is not None:
            yield from self.left.postorder()
        if self.right is not None:
            yield from self.right.postorder()
        yield self.data

    def levelorder(self) -> Iterator[T]:
        """Perform level order tree traversal."""
        level = deque()
        level.append(self)
        while level:
            node = level.popleft()
            yield node.data
            if node.left is not None:
                level.append(node.left)
            if node.right is not None:
                level.append(node.right)

    def leaves(self) -> Iterator[T]:
        """Iterate over the leaf nodes in order."""
        if self.left is not None:
            yield from self.left.leaves()
        if self.right is not None:
            yield from self.right.leaves()
        if self.right is None and self.left is None:
            yield self.data


if __name__ == "__main__":
    tree = BTree(1)
    tree.left = BTree(2)
    tree.right = BTree(3)
    tree.left.left = BTree(4)
    tree.left.right = BTree(5)
    tree.right.left = BTree(6)
    tree.right.right = BTree(7)

