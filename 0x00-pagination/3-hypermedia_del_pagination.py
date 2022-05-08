#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from operator import indexOf
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        return a dictionary with the following key-value pairs:
        index: the current start index of the return page.
        That is the index of the first item in the current page.

        next_index: the next index to query with. That should be
        the index of the first item after the last item on the current page.

        page_size: the current page size

        data: the actual page of the dataset
        """
        assert index < len(self.__indexed_dataset)
        if not index:
            index = 0
        data = []
        new_index = index
        while True:
            try:
                valid = self.__indexed_dataset[new_index]
                break
            except KeyError:
                new_index += 1
        for idx in range(new_index, new_index + page_size):
            data.append(self.__indexed_dataset[idx])
        return {
            'index': index,
            'next_index': new_index + page_size,
            'page_size': page_size,
            'data': data
        }
