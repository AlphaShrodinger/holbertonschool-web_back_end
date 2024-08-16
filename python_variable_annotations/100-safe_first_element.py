#!/usr/bin/env python3

'''Duck typing - first element of a sequence'''

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    '''Returns the first element of a sequence or None if is empty'''
    if lst:
        return lst[0]
    else:
        return None
