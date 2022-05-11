#!/usr/bin/env python3
"""Caching Algorithms"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache"""
    def __init__(self):
        """"""
        super().__init__()

    def put(self, key, item):
        """puts a new item into Cache key"""
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """retrieves item from Cache key"""
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
