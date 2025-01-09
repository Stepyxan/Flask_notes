from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import bussiness
class NotesService:
    def __init__(self, uri: str):
        self.collection = MongoClient(uri, server_api = ServerApi('1')).get_database('notesdb').get_collection('notes')

    def create(self, entity: bussiness.NotesEntity):
        new_inserted_result = self.collection.insert_one(entity.to_db_dto())
        return self.collection.find_one({"_id": str(new_inserted_result.inserted_id)})
