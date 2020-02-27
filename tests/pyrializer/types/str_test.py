import pytest

from pyrializer.types import StrType
from pyrializer.exceptions import CastError


@pytest.fixture
def str_type():
    return StrType()


def test_decode_string(str_type):
    assert str_type.decode('') == ''
    assert str_type.decode('foo') == 'foo'


def test_decode_int(str_type):
    assert str_type.decode(0) == '0'
    assert str_type.decode(123) == '123'
    assert str_type.decode(-456) == '-456'
    assert str_type.decode(+789) == '789'


def test_decode_float(str_type):
    assert str_type.decode(-1.23) == '-1.23'
    assert str_type.decode(123.99) == '123.99'
    assert str_type.decode(-456.23) == '-456.23'
    assert str_type.decode(+789.02) == '789.02'


@pytest.mark.parametrize('fvalue', [
    (False),
    (True),
    ({}),
    ({'key': 'value'}),
    ([]),
    ((1, 2))
])
def test_decode_int_raises_error(str_type, fvalue):
    with pytest.raises(CastError):
        _ = str_type.decode(fvalue)


def test_encode_string(str_type):
    assert str_type.encode('') == ''
    assert str_type.encode('foo') == 'foo'


def test_encode_int(str_type):
    assert str_type.encode(0) == '0'
    assert str_type.encode(123) == '123'
    assert str_type.encode(-456) == '-456'
    assert str_type.encode(+789) == '789'


def test_encode_float(str_type):
    assert str_type.encode(-1.23) == '-1.23'
    assert str_type.encode(123.99) == '123.99'
    assert str_type.encode(-456.23) == '-456.23'
    assert str_type.encode(+789.02) == '789.02'


@pytest.mark.parametrize('fvalue', [
    (False),
    (True),
    ({}),
    ({'key': 'value'}),
    ([]),
    ((1, 2))
])
def test_encode_int_raises_error(str_type, fvalue):
    with pytest.raises(CastError):
        _ = str_type.encode(fvalue)
