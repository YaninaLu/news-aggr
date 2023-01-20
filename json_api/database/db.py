from pymongo import MongoClient
import settings


client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DATABASE]
