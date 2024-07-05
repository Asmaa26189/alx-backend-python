#!/usr/bin/env python3
""" to_kv """
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return"""
    return (k, v**2)
