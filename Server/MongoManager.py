from pymongo import MongoClient


class MongoManager:
    """
    Clase que se encarga de comunicarse
    con la base de datos local de MongoDB.
    """

    def __init__(self):
        self.CLIENT = MongoClient("mongodb://127.0.0.1:27017")
        self.DB = self.CLIENT.test

    def insert(self, collection, document):
        """
        Método de inserción a la DB.
        :param collection: El collection (tabla en SQL) en el que vamos a insertar.
        :param document: El documento (fila de una tabla en SQL) que vamos a insertar.
        """

        collection.insert_one(document)

    def query(self, collection, query):

        return collection.find(query)
