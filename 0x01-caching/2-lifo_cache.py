#!/usr/bin/env python3
""""""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """"""
    keys_order = []

    def __init__(self):
        """"""
        super().__init__()
    
    def put(self, key, item):
        """"""
        if not key or not item:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.keys_order.append(key)
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            del_key = self.keys_order.pop()
            del self.cache_data[del_key]
            print(f"DISCARD: {del_key}")
        self.cache_data[key] = item
        self.keys_order.append(key)

    def get(self, key):
        """"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
