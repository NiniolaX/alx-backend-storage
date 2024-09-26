#!/usr/bin/env python3
"""
Contains a function that changes all the topics of a school document based on its name
"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]):
    """ Changes all the topics of a school document based on its name
    Args:
        mongo_collection (PymongoCollectionObject): pymongo ollection object
        name (str): school name to update
        topics (list of strings): List of topics approached in the school
    """
    result = mongo_collection.update_many( { 'name': name }, { '$set': { 'topics': str(topics) } })
