#!/usr/bin/env python3
"""LIFO caching module."""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """LIFO caching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """"assigns the value of the key"""
        if key is None or item is None:
            return
        #self.cache_data[key] = item
        if key not in self.cache_data.keys():
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem()
                print("DISCARD:", last_key)
        self.cache_data[key] = item

    def get(self, key):
        """getter method"""
        return self.cache_data.get(key, None)
