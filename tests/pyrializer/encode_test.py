import pytest

from pyrializer.encode import encode


class Fixture:
    _pyrializer_is_object = True
    number = int

@pytest.mark.parametrize('ftype', [
    (int),
    (str),
    (bool),
    (bool),
    (float),
])
def test_encode_null_context(ftype):
    value = encode(ftype, None)
    assert value is None


def test_encode_null_type():
    value = encode(None, 'context')
    assert value == 'context'


@pytest.mark.parametrize('ftype,context', [
    (int, 1),
    (str, 'string'),
    (bool, True),
    (float, 1.23),
])
def test_encode_primitive_type(ftype, context):
    value = encode(ftype, context)
    assert value == context


def test_encode_array():
    value = encode([int], [1, 2])
    assert len(value) == 2
    assert 1 in value
    assert 2 in value


def test_encode_array_wrong_type():
    with pytest.raises(ValueError):
        _ = encode([int], ['string'])


def test_encode_null_object():
    class Fixture:
        _pyrializer_is_object = True

    obj = Fixture()
    setattr(obj, '_pyrializer_is_null', True)
    value = encode(Fixture, obj)
    assert value is None


def test_encode_object():
    class Fixture:
        field = int
        pass

    obj = Fixture()
    setattr(obj, 'field', 123)
    value = encode(Fixture, obj)
    assert value == {'field': 123}
