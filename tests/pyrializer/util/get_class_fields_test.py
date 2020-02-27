from pyrializer.util import get_class_fields
from pyrializer.types import BoolType
from pyrializer.types import FloatType
from pyrializer.types import IntType
from pyrializer.types import StrType


def test_class_with_no_fields():
    class Test:
        pass
    fields = get_class_fields(Test)
    assert fields == {}


def test_class_with_some_fields():
    class Test:
        a = None
        b = int
        c = float
        d = bool
        e = str
    fields = get_class_fields(Test)
    assert len(fields) == 5
    assert fields['a'] is None
    assert isinstance(fields['b'], IntType)
    assert isinstance(fields['c'], FloatType)
    assert isinstance(fields['d'], BoolType)
    assert isinstance(fields['e'], StrType)


def test_class_with_private_fields():
    class Test:
        _starts_with_underscore = str
    fields = get_class_fields(Test)
    assert fields == {}


def test_class_with_underscored_fields():
    class Test:
        valid_field = int
    fields = get_class_fields(Test)
    assert len(fields) == 1
    assert isinstance(fields['valid_field'], IntType)


def test_class_with_methods():
    class Test:
        field = str

        def method():
            pass

    fields = get_class_fields(Test)
    assert len(fields) == 1
    assert isinstance(fields['field'], StrType)
