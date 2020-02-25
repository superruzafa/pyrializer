import pytest

import pyrializer


@pytest.fixture
def cls():
    @pyrializer.serializable
    class Fixture:
        pass
    return Fixture


def test_a_decorated_class_has_a_decode_method(cls):
    assert hasattr(cls, 'decode')


def test_a_decorated_class_has_an_encode_method(cls):
    assert hasattr(cls, 'encode')


def test_decode(cls, mocker):
    mocker.patch('pyrializer.decode')
    value = cls.decode('context')
    pyrializer.decode.assert_called_once_with(cls, 'context')


def test_encode(cls, mocker):
    mocker.patch('pyrializer.encode')
    obj = cls()
    value = obj.encode()
    pyrializer.encode.assert_called_once_with(cls, obj)