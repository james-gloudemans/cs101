"""test_btree.py: tests for binary tree module."""
# standard library

# third party libraries

# local libraries
from cs101.btree import BTree


def test_btree():
    """Unit test for BTree class."""
    tree = BTree(1)
    tree.left = BTree(2)
    tree.right = BTree(3)
    tree.left.left = BTree(4)
    tree.left.right = BTree(5)
    tree.right.left = BTree(6)
    tree.right.right = BTree(7)

    assert len(tree) == 7
    assert list(tree.levelorder()) == [1, 2, 3, 4, 5, 6, 7]
