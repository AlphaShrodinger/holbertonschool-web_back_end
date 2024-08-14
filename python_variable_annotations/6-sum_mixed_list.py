#!/usr/bin/env python3
''' Complex types - mixed list '''
from typing import Union
from typing import List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    ''' Sum of all elements in a mixed list '''
    return float(sum(mxd_list))
