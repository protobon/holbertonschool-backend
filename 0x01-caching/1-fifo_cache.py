#!/usr/bin/env python3
""""""

from curses import KEY_SOPTIONS


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """"""
    keys_order = []

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """"""
        if not key or not item:
            return
        self.cache_data[key] = item
        self.keys_order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del_key = self.keys_order.pop(0)
            del self.cache_data[del_key]
            print(f"DISCARD: {del_key}")

    def get(self, key):
        """"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
