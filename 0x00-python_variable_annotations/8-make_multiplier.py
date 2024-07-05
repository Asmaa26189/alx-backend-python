#!/usr/bin/env python3
""" make_multiplier"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return callable"""

    def f(n: float) -> float:
        """ multiplier """
        return float(n * multiplier)
    
    return f
