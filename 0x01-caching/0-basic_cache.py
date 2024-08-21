#!/usr/bin/env python3
"""0. Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Create a class BasicCache that inherits from BaseCaching. """
    def put(self, key, item):
        """Assign to the dictionary self.cache_data
        the item value for the key key."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        return self.cache_data.get(key, None)
