#!/usr/bin/env python3
""" element_length"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return length """
    return [(i, len(i)) for i in lst]
