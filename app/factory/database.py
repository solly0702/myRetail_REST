import os
from pymongo import MongoClient
from dotenv import dotenv_values


class Database(object):
    def __init__(self):
        config = dotenv_values(".flask_env")

        if config and config["ENV"] == "production":
            self.client = MongoClient(
                host=config["DB_HOST"],
                port=int(config["DB_PORT"]),
                username=config["DB_USER"],
                password=config["DB_PWD"],
                authSource=config["DB_SOURCE"]
            )
        else:
            self.client = MongoClient(
                host="mongodb://localhost/",
                port=27017)

        self.db = self.client[config["DB_NAME"] if config and config[
            "DB_NAME"] is not None else "myRetail"]

    def find(self, criteria, collection_name, projection=None, sort=None, limit=0, cursor=False):  # find all from db

        if "id" in criteria:
            criteria["id"] = criteria["id"]

        found = self.db[collection_name].find(
            filter=criteria, projection=projection, limit=limit, sort=sort)

        if cursor:
            return found

        found = list(found)

        return found

    def find_by_id(self, id, collection_name):
        found = self.db[collection_name].find_one({"id": id})

        if found is None:
            return None

        return found

    def update(self, id, payload, collection_name):
        criteria = {"id": id}

        # update value
        set_obj = {"$set": payload}

        updated = self.db[collection_name].update_one(criteria, set_obj)

        return self.find_by_id(id, collection_name) if updated.matched_count == 1 else None
