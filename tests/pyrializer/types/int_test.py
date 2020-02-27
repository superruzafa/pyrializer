import pytest

from pyrializer.types import IntType
from pyrializer.exceptions import CastError


@pytest.fixture
def int_type():
    return IntType()


def test_decode_int(int_type):
    assert int_type.decode(0) == 0
    assert int_type.decode(123) == 123
    assert int_type.decode(-456) == -456
    assert int_type.decode(+789) == 789


def test_decode_float(int_type):
    assert int_type.decode(3.1415) == 3
    assert int_type.decode(-3.1415) == -3
    assert int_type.decode(+.999) == 0
    assert int_type.decode(-.999) == 0


def test_decode_int_in_string(int_type):
    assert int_type.decode('11') == 11
    assert int_type.decode('-22') == -22
    assert int_type.decode('+33') == +33
    assert int_type.decode('    44   ') == 44


def test_decode_float_in_string(int_type):
    assert int_type.decode('3.1415') == 3
    assert int_type.decode('-4.999') == -4
    assert int_type.decode('-.123') == 0


@pytest.mark.parametrize('fvalue', [
    (''),
    ('54a'),
    ('b54'),
    (True),
    (False),
    ({}),
    ({'key': 'value'}),
    ([]),
    ((1, 2))
])
def test_decode_int_raises_error(int_type, fvalue):
    with pytest.raises(CastError):
        _ = int_type.decode(fvalue)


def test_encode_int(int_type):
    assert int_type.encode(0) == 0
    assert int_type.encode(123) == 123
    assert int_type.encode(-456) == -456
    assert int_type.encode(+789) == 789


def test_encode_float(int_type):
    assert int_type.encode(3.1415) == 3
    assert int_type.encode(-3.1415) == -3
    assert int_type.encode(+.999) == 0
    assert int_type.encode(-.999) == 0


def test_encode_int_in_string(int_type):
    assert int_type.encode('11') == 11
    assert int_type.encode('-22') == -22
    assert int_type.encode('+33') == +33
    assert int_type.encode('    44   ') == 44


def test_encode_float_in_string(int_type):
    assert int_type.encode('3.1415') == 3
    assert int_type.encode('-4.999') == -4
    assert int_type.encode('-.123') == 0


@pytest.mark.parametrize('fvalue', [
    (''),
    ('54a'),
    ('b54'),
    (True),
    (False),
    ({}),
    ({'key': 'value'}),
    ([]),
    ((1, 2))
])
def test_encode_int_raises_error(int_type, fvalue):
    with pytest.raises(CastError):
        _ = int_type.encode(fvalue)
