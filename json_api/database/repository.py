from database.db import db


async def get_all_news():
    collection = db["news"]
    news_dict = dict()
    i = 1
    for doc in collection.find():
        news_dict[i] = {"source": doc["source"], "date": doc["date"], "title": doc["title"],
                                 "brief": doc["brief"]}
        i += 1
    return news_dict
