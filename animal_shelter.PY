from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, pw, host, port, db, col):

        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    """ Create method """
    
    def create(self, data):          

        if data:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                return False
        else:
            raise ValueError("Data parameter is empty")

    """ Read method """
    
    def read(self, query):

        try:
            result = self.collection.find(query)
            return result
        except Exception as e:
            return str(e)
            
    """ Update method """
            
    def update(self, query, update_data, multi=False):
    	try:
    	    result = self.collection.update_many(query, {'$set': update_data}) if multi else self.collection.update_one(query, {'$set': update_data})
    	    return result.modified_count
    	except Exception as e:
    	    return str(e)
    	    
    	    
   """ Delete method """
   
    def delete(self, query):
        try: 
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            return str(e)	    
    	
