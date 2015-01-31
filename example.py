#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   15/1/30
Desc    :
"""
from bson.dbref import DBRef
import pymongo

print "pymongo version:", pymongo.version

def get_test_coll(con):
    db = con["test"]

    coll_t1 = db["t1"]
    coll_t2 = db["t2"]
    coll_t1.drop()
    coll_t2.drop()

    coll_t1.save({
        "_id": "t1id",
        "name": "coll_t1"
    })

    coll_t2.save({
        "_id": "t2id",
        "name": "coll_t2",
        "t1_ref": [
            DBRef(collection="t1", id="t1id"),
            DBRef(collection="t1", id="t1id"),
        ]
    })
    return coll_t2


# way 1
from pymongo_dbref import WrapperMongoClient
con = WrapperMongoClient(host='localhost', port=17117)

coll_t2 = get_test_coll(con)
cursor = coll_t2.find().deref()
l = list(cursor)
print l


#way 2
from pymongo import MongoClient
from pymongo_dbref import patch_cursor
con = MongoClient(host='localhost', port=17117)
patch_cursor()

coll_t2 = get_test_coll(con)
cursor = coll_t2.find()
l = list(cursor)
print l