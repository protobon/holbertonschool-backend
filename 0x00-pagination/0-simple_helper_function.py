#!/usr/bin/env python3
"""Pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """
    returns a tuple of size two that contains
    the start index and end index of current page

    first parameter: page number
    second parameter: page size
    """
    if page == 1:
        page = 0
    else:
        page = page_size * (page - 1)
    return (page, page + page_size)
