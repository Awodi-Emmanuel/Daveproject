from .folders import get_user_files


class Generator:
    BASE_PATH = "/Users/DELL/Documents/Projects/storage/"
    FOLDER_PREFIX = 'user_'

    @staticmethod
    def generate_user_folder_object(user_id):

        return get_user_files(Generator.BASE_PATH + Generator.FOLDER_PREFIX + user_id)
