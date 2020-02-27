import pytest

from pyrializer.types import augment
from pyrializer.types import IntType
from pyrializer.types import FloatType
from pyrializer.types import BoolType
from pyrializer.types import StrType
from pyrializer.types import CustomType


def test_augment_int():
    value = augment(int)
    assert isinstance(value, IntType)


def test_augment_float():
    value = augment(float)
    assert isinstance(value, FloatType)


def test_augment_bool():
    value = augment(bool)
    assert isinstance(value, BoolType)


def test_augment_str():
    value = augment(str)
    assert isinstance(value, StrType)


def test_augment_custom_type_class():
    class MyType(CustomType):
        pass
    value = augment(MyType)
    assert isinstance(value, MyType)
    assert isinstance(value, CustomType)


def test_augment_custom_type_object():
    class MyType(CustomType):
        pass
    instance = MyType()
    value = augment(instance)
    assert value is instance


def test_augment_list_of_any_type():
    value = augment([])
    assert type(value) is list
    assert len(value) == 0


def test_augment_list():
    class MyType(CustomType):
        pass

    value = augment([MyType])
    assert type(value) is list
    assert isinstance(value[0], MyType)


@pytest.mark.parametrize('ftype', [
    ({}),
])
def test_augment_other_type(ftype):
    value = augment(ftype)
    assert value is ftype
