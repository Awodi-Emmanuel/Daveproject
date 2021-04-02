from .folders import path_to_dict
from permissions.classes.permission_engine import Engine

class Generator:

    BASE_PATH = "/var/www/html/storage/"

    @staticmethod
    def generateUserFolderObject(user_id):

        permission_object = Engine.fetch_accessible_files(user=user_id)
        folder_object = path_to_dict(Generator.BASE_PATH + "user_" + user_id)
        user_folder_object = []

        print(folder_object)
        print(permission_object)
        # for permissions in permission_object:

    @staticmethod
    def matchFolderFileToPermission(folder_object):
        