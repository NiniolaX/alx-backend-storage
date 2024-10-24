#!/usr/bin/env python3
"""
Contains a "Cache" class.
"""
import redis
import uuid
from typing import Union


class Cache:
    """This class defines a Cache object
    Attributes:
        None
    Methods:
        store(): Stores a 'data' argument in Redis and returns its key
    """
    def __init__(self):
        """ Instantiates a new cache object """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores a 'data' argument in Redis using a randomly generated key
        and returns the key.

        Args:
            data(str, bytes, int or float): Data to be stored in Redis

        Return:
            (str): Key of input data stored in Redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key