#!/usr/bin/env python3
"""Caching Algorithms"""

from curses import KEY_SOPTIONS


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Cache with FIFO (queue) structure"""
    keys_order = []

    def __init__(self):
        """inits from BaseCaching"""
        super().__init__()

    def put(self, key, item):
        """
        puts a new item into Cache key

        if number of items reach a limit set
        then the oldest item is removed to make space
        (First in, First out)
        """
        if not key or not item:
            return
        self.cache_data[key] = item
        self.keys_order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del_key = self.keys_order.pop(0)
            del self.cache_data[del_key]
            print(f"DISCARD: {del_key}")

    def get(self, key):
        """retrieves value from Cache key"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
