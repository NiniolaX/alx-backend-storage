#!/usr/bin/env python3
"""
Contains a function that lists all the collections in a mongodb database
"""
from pymongo.collection import Collection
from typing import List


def list_all(mongo_collection: Collection) -> List:
    """ Lists all documents in a collection """
    if mongo_collection.count_documents == 0:
        return []

    documents = mongo_collection.find()
    return list(documents)
