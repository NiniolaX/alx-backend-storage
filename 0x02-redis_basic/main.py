#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

print()
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

print()
print("Test 2")
for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value

print()
print("Test 3")
cache.store(b"foo")
print(cache.get("foo"))

print()
print("Test 4")
Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))


print()
print("Test 4")
Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))


print()
print("Test 5")
Cache = __import__('exercise').Cache
replay = __import__('exercise').replay
cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store("egg")
cache.store("eggsperiment")
replay(cache.store)
