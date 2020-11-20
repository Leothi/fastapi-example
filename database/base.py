from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from treinamento_db.settings import envs


class BaseDatabase:
    _database: Database
    _collection: Collection

    def __init__(self, collection: str = None):
        self._client = MongoClient(envs.MONGODB_URI)
        self._database = self._client[envs.MONGODB_DATABASE]
        if collection:
            self._collection = self._database[collection]
