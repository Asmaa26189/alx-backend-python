#!/usr/bin/env python3
""" make_multiplier"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier"""
    def f(n: float) -> float:
        """ multiplies a float by multiplier """
        return float(n * multiplier)

    return f
