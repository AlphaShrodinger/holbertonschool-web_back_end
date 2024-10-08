#!/usr/bin/env python3

'''More involved type annotations'''

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    '''Returns a value from dictionary or default value if key is not found'''
    if key in dct:
        return dct[key]
    else:
        return default
