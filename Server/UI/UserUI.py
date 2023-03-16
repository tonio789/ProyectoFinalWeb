from Model.User import Users
from MongoManager import MongoManager


class UserUI:

    def __init__(self):
        self.MongoManager = MongoManager()

    def post_user(self, user):
        user = user.split('-')

        web_user = Users(user[0], user[1], user[2], user[3], user[4])
        self.MongoManager.insert(self.MongoManager.DB.Users, web_user.dict_from_class())

    def attribute_exists(self, attribute_key, attribute_value):

        results_cursor = self.MongoManager.query(self.MongoManager.DB.Users, {attribute_key: attribute_value})
        attribute_list = [record for record in results_cursor]

        if len(attribute_list) == 0:
            return False
        else:
            return True
