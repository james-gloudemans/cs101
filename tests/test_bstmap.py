"""test_bstmap.py: tests for binary search tree module."""
# standard library
import random

# third party libraries
import pytest

# local libraries
from cs101.bstmap import BSTMap


def test_build():
    """Test constructing a BSTMap."""
    init = []
    for _ in range(1000):
        n = random.randrange(1, 10000)
        init.append((n, n))
    tree = BSTMap(init)
    assert tree._isBST()
    for key in tree:
        assert tree[key] == key


def test_del():
    """Test deleting a key, value pair from BSTMap."""
    init = []
    for _ in range(1000):
        n = random.randrange(1, 10000)
        init.append((n, n))
    tree = BSTMap(tuple(init))
    for k, v in set(init):
        del tree[k]
        assert tree._isBST()
        assert k not in tree


def test_parent():
    """Test that each node is tracking its parent."""
    init = []
    for _ in range(100):
        n = random.randrange(1, 10000)
        init.append((n, n))
    tree = BSTMap(init)
    for node in tree._nodes():
        if node.left is not None:
            assert node.left.parent == node
        if node.right is not None:
            assert node.right.parent == node


def test_nodes_iter():
    """Test method for finding the successor of a node."""
    lst = [(5, 5), (1, 1), (7, 7), (2, 2), (3, 3), (6, 6), (4, 4)]
    tree = BSTMap(lst)
    for node in tree._nodes():
        if node.right is not None:
            assert next(node.right._nodes()).key == node.key + 1


if __name__ == "__main__":
    test_build()
    test_del()
    test_parent()
