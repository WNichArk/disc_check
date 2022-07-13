from pymongo import MongoClient
import constants.constants as cs


class database():

    def get_database(self, db_name):

        try:
            client = MongoClient(cs.CONNECTION_STRING)
            print("Mongo connection established.")
        except:
            print("Mongo connection failed")

        return client[db_name]

    def __init__(self):
        pass


