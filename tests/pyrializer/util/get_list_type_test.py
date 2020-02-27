import pytest

from pyrializer.util import get_list_type


@pytest.fixture
def augment(mocker):
    return mocker.patch('pyrializer.util.augment')


def test_any_type():
    itemtype = get_list_type([])
    assert itemtype is None


def test_one_type(augment):
    augment.side_effect = lambda x: x * 2
    item_type = get_list_type([1])
    assert item_type == 2


def test_multiple_types():
    with pytest.raises(ValueError):
        _ = get_list_type([int, str])
