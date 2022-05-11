#!/usr/bin/env python3
"""Caching algorithms"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Cache with Least Recently Used algorithm"""
    use_count = {}

    def __init__(self):
        """inits from BaseCaching"""
        super().__init__()

    def put(self, key, item):
        """
        Puts a new item to cache key.

        An auxiliar queue structure takes
        count of the keys that are being used.
        If the number of items reach a limit
        set, then the key that hasn't been used
        for the most time gets removed (LRU).
        """
        if not key or not item:
            return
        if key not in self.cache_data.keys():
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                del_key = list(self.use_count.keys())[0]
                print(f"DISCARD: {del_key}")
                del self.cache_data[del_key]
                del self.use_count[del_key]

        if key in self.use_count.keys():
            del self.use_count[key]
        self.use_count[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves value from cache key.

        Everytime a key is retrieved, it is
        added to the auxiliar queue structure
        of Least Recently Used (to the last place).
        """
        if not key or key not in self.cache_data:
            return None
        del self.use_count[key]
        self.use_count[key] = 1
        return self.cache_data[key]
