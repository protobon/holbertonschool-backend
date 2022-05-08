#!/usr/bin/env python3
"""Pagination"""

import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        return a list from dataset with values in the range of
        page, page_size taken from the index_page method

        return empty list if range is outside of dataset
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        [start, end] = index_range(page, page_size)  # range of data to return
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        returns hypermedia dictionary of page from dataset

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        hypermedia: dict = {}

        hypermedia["page_size"] = len(data)
        hypermedia["page"] = page
        hypermedia["data"] = data
        hypermedia["next_page"] = page + 1 if page + 1 <= total_pages else None
        hypermedia["prev_page"] = page - 1 if page > 1 else None
        hypermedia["total_pages"] = total_pages

        return hypermedia
