import pytest
from ..position import Position


def test_add_sum():
    x = Position(1, 2, 3)
    y = Position(4, 5, 6)
    z = x + y
    assert z.q == 5
    assert z.r == 7
    assert z.s == 9


def test_add_to_self():
    x = Position(1, 2, 3)
    y = Position(4, 5, 6)
    x += y
    assert x.q == 5
    assert x.r == 7
    assert x.s == 9


# test negatives
# add limit for q,r,s - e.g. -4 and +4 - check for each q,r,s etc
# check for multiple adds
# check for mixed adds e.g. +1, 0, -1