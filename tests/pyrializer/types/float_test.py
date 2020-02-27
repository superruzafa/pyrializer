import pytest

from pyrializer.types import FloatType
from pyrializer.exceptions import CastError


@pytest.fixture
def float_type():
    return FloatType()


def test_decode_int(float_type):
    assert float_type.decode(0) == 0.0
    assert float_type.decode(123) == 123.0
    assert float_type.decode(-456) == -456.0
    assert float_type.decode(+789) == 789.0


def test_decode_float(float_type):
    assert float_type.decode(3.1415) == pytest.approx(3.1415)
    assert float_type.decode(-3.1415) == pytest.approx(-3.1415)
    assert float_type.decode(+.999) == pytest.approx(0.999)
    assert float_type.decode(-.999) == pytest.approx(-0.999)


def test_decode_int_in_string(float_type):
    assert float_type.decode('11') == 11.0
    assert float_type.decode('-22') == -22.0
    assert float_type.decode('+33') == +33.0
    assert float_type.decode('    44   ') == 44.0


def test_decode_float_in_string(float_type):
    assert float_type.decode('3.1415') == pytest.approx(3.1415)
    assert float_type.decode('-4.999') == pytest.approx(-4.999)
    assert float_type.decode('-.123') == pytest.approx(-0.123)


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
def test_decode_int_raises_error(float_type, fvalue):
    with pytest.raises(CastError):
        _ = float_type.decode(fvalue)


def test_encode_int(float_type):
    assert float_type.encode(0) == 0.0
    assert float_type.encode(123) == 123.0
    assert float_type.encode(-456) == -456.0
    assert float_type.encode(+789) == 789.0


def test_encode_float(float_type):
    assert float_type.encode(3.1415) == pytest.approx(3.1415)
    assert float_type.encode(-3.1415) == pytest.approx(-3.1415)
    assert float_type.encode(+.999) == pytest.approx(0.999)
    assert float_type.encode(-.999) == pytest.approx(-0.999)


def test_encode_int_in_string(float_type):
    assert float_type.encode('11') == 11.0
    assert float_type.encode('-22') == -22.0
    assert float_type.encode('+33') == +33.0
    assert float_type.encode('    44   ') == 44.0


def test_encode_float_in_string(float_type):
    assert float_type.encode('3.1415') == pytest.approx(3.1415)
    assert float_type.encode('-4.999') == pytest.approx(-4.999)
    assert float_type.encode('-.123') == pytest.approx(-0.123)


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
def test_encode_int_raises_error(float_type, fvalue):
    with pytest.raises(CastError):
        _ = float_type.encode(fvalue)
