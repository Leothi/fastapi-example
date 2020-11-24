from datetime import datetime

from full_api.database.base import MongoDatabase
from full_api.settings import envs

class UsuarioDatabase(MongoDatabase):
    def __init__(self):
        super().__init__(envs.COLLECTION_USER)

    def search(self, id) -> dict:
        """Search for a record in extraction collection"""

        result = self.collection.find_one({'_id': self.str_to_objectid(id)}) or {}
        if result:
            result = self.objectid_dict_to_str(result)
        return result
    
    def insert(self, name: str, job: str, password: str):        
        document = {
            "name": name,
            "job": job,
            "password": password,
            'created_date': datetime.utcnow(),
            'updated_date': datetime.utcnow()
        }
        result = self.collection.insert_one(document)
        return self.objectid_to_str(result.inserted_id)
