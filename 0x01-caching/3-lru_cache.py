#!/usr/bin/env python3
"""LRU caching module."""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRU caching"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """"assigns the value of the key"""
        if key is None or item is None:
            return
        if key not in self.cache_data.keys():
            #self.cache_datai[key] = item
            #self.cache_data.move_to_end(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                d_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", d_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, ikey):
        """getter method"""
        return self.cache_data.get(key, None)
