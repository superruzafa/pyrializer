import pytest
import sys

from pyrializer.decode import decode


@pytest.fixture
def is_custom_type(mocker):
    return mocker.patch.object(
        sys.modules['pyrializer.decode'], 'is_custom_type'
    )


@pytest.fixture
def get_class_fields(mocker):
    return mocker.patch.object(
        sys.modules['pyrializer.decode'], 'get_class_fields'
    )


@pytest.fixture
def get_list_type(mocker):
    return mocker.patch.object(
        sys.modules['pyrializer.decode'], 'get_list_type'
    )


def test_decode_any_type():
    value = decode(None, 'context')
    assert value == 'context'


def test_decode_custom_type_with_null_context(mocker, is_custom_type):
    is_custom_type.return_value = True
    custom_type = mocker.Mock()
    value = decode(custom_type, None)
    assert value is None
    is_custom_type.assert_called_with(custom_type)


def test_decode_custom_type(mocker, is_custom_type):
    is_custom_type.return_value = True
    custom_type = mocker.Mock()
    custom_type.decode = mocker.Mock()
    custom_type.decode.return_value = '456'
    value = decode(custom_type, '123')
    assert value == '456'
    is_custom_type.assert_called_with(custom_type)
    custom_type.decode.assert_called_with('123')


def test_decode_list_with_null_context():
    value = decode([int], None)
    assert value is None


def test_decode_empty_list():
    value = decode([int], [])
    assert value == []


def test_decode_list(mocker, is_custom_type, get_list_type):
    custom_type = mocker.Mock()
    custom_type.decode = mocker.Mock()
    custom_type.decode.side_effect = lambda x: x * 2

    is_custom_type.return_value = True
    get_list_type.return_value = custom_type

    itemtype = mocker.Mock()
    itemtype.decode = mocker.Mock()
    itemtype.decode.side_effect = lambda x: x * 2
    is_custom_type.side_effect = lambda ftype: ftype is custom_type

    ftype = [itemtype]
    value = decode(ftype, [1, 2, 3])
    get_list_type.assert_called_with(ftype)
    is_custom_type.assert_called_with(custom_type)
    assert value == [2, 4, 6]


def test_decode_object_with_null_context(mocker, get_class_fields):
    class Obj:
        pass
    get_class_fields.return_value = {'a': None, 'b': None}

    value = decode(Obj, None)
    get_class_fields.assert_called_with(Obj)
    assert isinstance(value, Obj)
    assert value._pyrializer_is_null
    assert value.a is None
    assert value.b is None


def test_decode_object(mocker, get_class_fields):
    class Obj:
        pass
    get_class_fields.return_value = {'a': None, 'b': None}

    value = decode(Obj, {'a': 1, 'b': 2})
    get_class_fields.assert_called_with(Obj)
    assert isinstance(value, Obj)
    assert not value._pyrializer_is_null
    assert value.a == 1
    assert value.b == 2
