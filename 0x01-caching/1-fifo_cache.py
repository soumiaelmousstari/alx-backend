#!/usr/bin/env python3
"""1. FIFO caching"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class FIFOCache that inherits from BaseCaching."""
    def __init__(self):
        """Initializes the cache. """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign to the dictionary self.cache_data
        the item value for the key key."""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        return self.cache_data.get(key, None)
