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
    for _ in range(100):
        n = random.randrange(1, 10000)
        init.append((n, n))
    tree = BSTMap(init)
    assert tree._isBST()
    for key in tree:
        assert tree[key] == key


def test_del():
    """Test deleting a key, value pair from BSTMap."""
    init = []
    for _ in range(100):
        n = random.randrange(1, 10000)
        init.append((n, n))
    tree = BSTMap(init)
    for i in range(100):
        print(i)
        m = random.choice(init)
        initial = tree[m[0]]
        del tree[m[0]]
        assert tree._isBST()
        with pytest.raises(KeyError) as e:
            assert tree[m[0]]
        tree[m[0]] = m[1]


if __name__ == "__main__":
    test_build()
    test_del()
