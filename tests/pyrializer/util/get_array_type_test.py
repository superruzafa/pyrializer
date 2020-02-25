import pytest

from pyrializer.util import get_array_type


def test_any_type():
    itemtype = get_array_type([])
    assert itemtype is None

def test_one_type():
    itemtype = get_array_type([int])
    assert itemtype is int

def test_multiple_types():
    with pytest.raises(ValueError):
        _ = get_array_type([int, str])