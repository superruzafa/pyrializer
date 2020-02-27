import pytest
import sys

from pyrializer.encode import encode


@pytest.fixture
def is_custom_type(mocker):
    return mocker.patch.object(
        sys.modules['pyrializer.encode'], 'is_custom_type'
    )


@pytest.fixture
def get_list_type(mocker):
    return mocker.patch.object(
        sys.modules['pyrializer.encode'], 'get_list_type'
    )


@pytest.fixture
def get_class_fields(mocker):
    return mocker.patch.object(
        sys.modules['pyrializer.encode'], 'get_class_fields'
    )


def test_encode_any_type():
    value = encode(None, 'context')
    assert value == 'context'


def test_encode_custom_type_with_null_context(mocker, is_custom_type):
    custom_type = mocker.Mock()
    value = encode(custom_type, None)
    assert value is None


def test_encode_custom_type(mocker, is_custom_type):
    is_custom_type.return_value = True
    custom_type = mocker.Mock()
    custom_type.encode = mocker.Mock()
    custom_type.encode.return_value = '456'
    value = encode(custom_type, '123')
    assert value == '456'
    is_custom_type.assert_called_with(custom_type)
    custom_type.encode.assert_called_with('123')


def test_encode_list_with_null_context():
    value = encode([int], None)
    assert value is None


def test_encode_empty_list():
    value = encode([int], [])
    assert value == []


def test_encode_list(mocker, get_list_type, is_custom_type):
    custom_type = mocker.Mock()
    custom_type.encode = mocker.Mock()
    custom_type.encode.side_effect = lambda x: x * 2
    get_list_type.return_value = custom_type
    is_custom_type.side_effect = lambda x: x is custom_type

    value = encode([custom_type], [1, 2])
    assert value == [2, 4]


def test_encode_object_with_null_context():
    class Obj:
        pass
    obj = Obj()
    obj._pyrializer_is_null = True
    get_class_fields.return_value = {'a': None, 'b': None}

    value = encode(Obj, obj)
    assert value is None


def test_encode_object(get_class_fields):
    class Obj:
        pass
    obj = Obj()
    setattr(obj, 'a', 'A')
    setattr(obj, 'b', 'B')
    obj._pyrializer_is_null = False
    get_class_fields.return_value = {'a': None, 'b': None, 'c': None}

    value = encode(Obj, obj)
    assert value == {'a': 'A', 'b': 'B', 'c': None}
    get_class_fields.assert_called_with(Obj)
