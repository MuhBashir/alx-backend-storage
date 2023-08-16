def list_all(mongo_collection):
    """
    printing list of collections otherwise empty lisi
    """
    return [doc for doc in mongo_collection.find()]
