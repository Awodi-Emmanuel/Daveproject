from .folders import get_user_files


class Generator:
    
    # Macos Base Path: /var/www/html/storage/
    # Windows Base Path: /Users/DELL/Documents/Projects/storage/
    BASE_PATH = "/var/www/html/storage/"  # os.environ.get('BASE_PATH'),
    FOLDER_PREFIX = "user_"  # os.environ.get('BASE_PATH'),

    @staticmethod
    def generate_user_folder_object(user_id):
        return get_user_files(Generator.BASE_PATH + Generator.FOLDER_PREFIX + user_id)
