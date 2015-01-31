# use
    
    If you want detailed please check example.py
    
## way 1
    from pymongo_dbref import WrapperMongoClient
    con = WrapperMongoClient(host='localhost', port=17117)
    
    coll_t2 = get_test_coll(con)
    cursor = coll_t2.find().deref()
    l = list(cursor)
    print l
    
    
## way 2

    from pymongo import MongoClient
    from pymongo_dbref import patch_cursor
    con = MongoClient(host='localhost', port=17117)
    patch_cursor()
    
    coll_t2 = get_test_coll(con)
    cursor = coll_t2.find()
    l = list(cursor)
    print l