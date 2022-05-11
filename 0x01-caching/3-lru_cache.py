#!/usr/bin/env python3
""""""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """"""
    use_count = {}
    keys_order = []

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """"""
        if not key or not item:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.use_count[key] += 1
            self.keys_order.append((key, self.use_count[key]))
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            lru = sorted(self.keys_order, key=lambda tup: tup[1])
            while True:
                del_key = lru.pop(0)[0]
                if del_key in self.cache_data.keys():
                    break
            del self.cache_data[del_key]
            print(f"DISCARD: {del_key}")
        if key not in self.use_count:
            self.use_count[key] = 0
        else:
            self.use_count[key] += 1
        self.keys_order.append((key, self.use_count[key]))
        self.cache_data[key] = item

    def get(self, key):
        """"""
        if not key or key not in self.cache_data:
            return None
        self.use_count[key] += 1
        self.keys_order.append((key, self.use_count[key]))
        return self.cache_data[key]
