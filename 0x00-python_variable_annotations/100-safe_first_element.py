#!/usr/bin/env python3
""" safe_first_element """
from typing import Any, Union, Sequence, Iterable, List, Tuple


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe_first_element"""
    if lst:
        return lst[0]
    else:
        return None