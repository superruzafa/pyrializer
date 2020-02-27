import inspect
from .types import augment

__all__ = [
    'get_class_fields',
    'get_list_type'
]


def get_class_fields(cls):
    fields = inspect.getmembers(cls, lambda a: not(inspect.isroutine(a)))
    return {
        a[0]: augment(getattr(cls, a[0]))
        for a in fields if not a[0].startswith('_')
    }


def get_list_type(spec):
    ftype_len = len(spec)
    if ftype_len == 0:
        return None
    elif ftype_len == 1:
        return augment(spec[0])
    else:
        raise ValueError('Multiple listitem types')
