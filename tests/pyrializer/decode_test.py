import pytest

from pyrializer.decode import decode


def test_decode_any_type():
    value = decode(None, 'context')
    assert value == 'context'


@pytest.mark.parametrize('ftype', [
    (int),
    (str),
    (bool),
    (bool),
    (float),
])
def test_decode_primitive_with_null_context(ftype):
    value = decode(ftype, None)
    assert value is None


def test_decode_primitive_with_null_context():
    value = decode(int, None)
    assert value is None


@pytest.mark.parametrize('ftype,context', [
    (int, 1),
    (str, 'string'),
    (bool, True),
    (bool, False),
    (float, 123.4),
])
def test_decode_primitive(ftype, context):
    value = decode(ftype, context)
    assert value == context


@pytest.mark.parametrize('ftype,context', [
    (int, 'string'),
    (str, True),
    (bool, 1.23),
    (float, '123.4'),
])
def test_decode_primitive_wrong_type(ftype, context):
    with pytest.raises(ValueError):
        _ = decode(ftype, context)


def test_decode_array_with_null_context():
    value = decode([int], None)
    assert value == None


def test_decode_empty_array():
    value = decode([int], [])
    assert value == []


def test_decode_array():
    value = decode([int], [1, 2, 3])
    assert len(value) == 3
    assert 1 in value
    assert 2 in value
    assert 3 in value


def test_decode_array_wrong_type():
    with pytest.raises(ValueError):
        _ = decode([bool], [True, 'string', 1])


def test_decode_object_with_null_context():
    class Fixture:
        _pyrializer_is_object = True
        @classmethod
        def from_dict(cls, dictionary):
            assert dictionary == {}
            return Fixture()

    value = decode(Fixture, None)
    assert type(value) is Fixture
    assert value._pyrializer_is_null


def test_decode_object():
    class Fixture:
        _pyrializer_is_object = True
        field = int
        @classmethod
        def from_dict(cls, dictionary):
            assert dictionary == {'field': 1}
            obj = Fixture()
            setattr(obj, 'field', 1)
            return obj

    value = decode(Fixture, {'field': 1})
    assert type(value) is Fixture
    assert value.field == 1
    assert not value._pyrializer_is_null
