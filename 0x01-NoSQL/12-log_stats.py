#!/usr/bin/env python3
""" This script provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
collection = client.logs.nginx

logs_count: int = collection.count_documents({})
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
status_check = collection.count_documents({'path': "/status"})


print(f"{logs_count} logs")
print("Methods:")
for method in methods:
    doc_count: int = collection.count_documents({'method': method})
    print(f"\tmethod {method}: {doc_count}")
print(f"{status_check} status check")
