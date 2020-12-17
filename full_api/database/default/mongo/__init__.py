from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from full_api.settings import envs


class MongoDatabase:
    """Classe base para banco de dados MongoDB
    """
    _database: Database
    _collection: Collection

    def __init__(self, collection: str = None):
        """Conexão com o banco

        :param collection: Coleção do banco, defaults to None
        :type collection: str, optional
        """
        self.client = MongoClient(envs.MONGODB_URI)  # Conexão com o mongo
        self.db = self.client[envs.MONGODB_DATABASE]  # Conexão com o banco de dados
        if collection:
            self.collection = self.db[collection]  # Conexão com a tabela

    def test_connection(self, collection: str = None):
        """Testa a conexão com o banco.

        :param collection: Coleção do banco, defaults to None
        :type collection: str, optional
        """
        self.client.server_info(collection)

    def close(self):
        """Fecha a conexão com o banco.
        """
        self.client.close()

    @classmethod
    def objectid_to_str(cls, id: ObjectId) -> str:
        """bson.ObjectId to str"""

        return str(id)

    @classmethod
    def objectid_dict_to_str(cls, d: dict) -> dict:
        """Help function to update _id key in a list of dict (bson.ObjectId to str)"""

        try:
            d['_id'] = cls.objectid_to_str(d['_id'])
        finally:
            return d

    @classmethod
    def str_to_objectid(cls, id: str) -> ObjectId:
        return ObjectId(id)

    def __enter__(self) -> 'BaseDatabase':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
