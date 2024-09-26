#!/usr/bin/env python3
"""
Contains a function that inserts a new document into a collection
"""


def insert_school(mongo_collection, **kwargs) -> str:
    """ Inserts a new document into a collection """
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
