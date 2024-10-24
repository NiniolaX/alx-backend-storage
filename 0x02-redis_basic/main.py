#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

print("Test 1")
cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

print("Test 2")
for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value

print("Test 3")
cache.store(b"foo")
print(cache.get("foo"))