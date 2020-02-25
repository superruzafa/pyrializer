from pyrializer.util import get_class_fields


def test_class_with_no_fields():
    class Test:
        pass
    fields = get_class_fields(Test)
    assert fields == {}


def test_class_with_some_fields():
    class Test:
        a = None
        b = int
        c = str
    fields = get_class_fields(Test)
    assert len(fields) == 3
    assert fields['a'] == None
    assert fields['b'] == int
    assert fields['c'] == str


def test_class_with_private_fields():
    class Test:
        _starts_with_underscore = str
    fields = get_class_fields(Test)
    assert fields == {}


def test_class_with_underscored_fields():
    class Test:
        valid_field = int
    fields = get_class_fields(Test);
    assert len(fields) == 1
    assert fields['valid_field'] == int


def test_class_with_methods():
    class Test:
        field = str
        def method():
            pass
    fields = get_class_fields(Test)
    assert len(fields) == 1
    assert fields['field'] == str
