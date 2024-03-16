#!/usr/bin/env python3
"""Basic caching module."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic caching"""
    def put(self, key, item):
        """"assigns the value of the key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """getter method"""
        return self.cache_data.get(key, None)
