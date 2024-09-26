#!/usr/bin/env python3
"""
Contains a function that returns the list of schools having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """ Returns the list of schools having a specific topic
    Args:
        mongo_collection (PymongoCollectionObject): pymongo collection object
        topic (str): topic searched
    Return:
        (list of pymongo collection objects): List of schools having topic
    """
    result = mongo_collection.find({'topics': topic})
    return result