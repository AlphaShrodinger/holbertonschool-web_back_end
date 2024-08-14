#!/usr/bin/env python3
''' Complex types - functions '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Returns a function that multiplies its arguments '''

    def multiply(n: float) -> float:
        ''' Multiplies a number by the given multiplier '''

        return n * multiplier
    return multiply
