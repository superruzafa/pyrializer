import pytest

from pyrializer.types import BoolType
from pyrializer.exceptions import CastError


@pytest.fixture
def bool_type():
    return BoolType()


def test_decode_bool(bool_type):
    assert bool_type.decode(False) is False
    assert bool_type.decode(True) is True


@pytest.mark.parametrize('fvalue', [
    (0),
    (1),
    (-1),
    (12),
    (123.34),
    (''),
    ('54a'),
    ({}),
    ({'key': 'value'}),
    ([]),
    ((1, 2))
])
def test_decode_int_raises_error(bool_type, fvalue):
    with pytest.raises(CastError):
        _ = bool_type.decode(fvalue)


def test_encode_bool(bool_type):
    assert bool_type.encode(False) is False
    assert bool_type.encode(True) is True


@pytest.mark.parametrize('fvalue', [
    (0),
    (1),
    (-1),
    (12),
    (123.34),
    (''),
    ('54a'),
    ({}),
    ({'key': 'value'}),
    ([]),
    ((1, 2))
])
def test_encode_int_raises_error(bool_type, fvalue):
    with pytest.raises(CastError):
        _ = bool_type.encode(fvalue)
