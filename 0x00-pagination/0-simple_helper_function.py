#!/usr/bin/env python3
"""0. Simple helper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """A function return a tuple of size two containing a start
    index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters."""
    s = (page - 1) * page_size
    f = s + page_size
    return (s, f)
