#!/usr/bin/env python3
"""
Contains a "Cache" class.
"""
import redis
import uuid
from typing import Union, Callable, Any


class Cache:
    """This class defines a Cache object.

    Attributes:
        None

    Methods:
        store(): Stores a 'data' argument in Redis and returns its key.
    """
    def __init__(self):
        """ Instantiates a new cache object """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores a 'data' argument in Redis using a randomly generated key and
        returns the key.

        Args:
            data(str, bytes, int or float): Data to be stored in Redis.

        Returns:
            (str): Redis key of stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable[[bytes], Any] = None) -> Any:
        """
        Retrieves data from Redis with optional type conversion.

        Args:
            key(str): The Redis key to retrieve.
            fn(callable): A callable function to convert retrieved bytes to
                the desired type.

        Returns:
            Retrieved data converted to its desired type.
        """
        data = self._redis.get(key)

        if data is None:
            return None

        # Convert retrieved data to desired type if callable is provided
        if fn:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> str:
        """
        Retrieves data from Redis and converts it to a string
        """
        data = self.get(key)
        return data.decode('utf-8')

    def get_int(self, key: str) -> int:
        """
        Retrieves data from Redis and converts it to an integer
        """
        data = self.get(key)
        return int(data)
