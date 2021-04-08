from .folders import get_current_directory
from pathlib import Path


class Directory:

    # Macos Base Path: /var/www/html/storage/
    # Windows Base Path: /Users/DELL/Documents/Projects/storage/
    BASE_PATH = " /var/www/html/storage/"  # os.environ.get('BASE_PATH'),
    USER_PREFIX = "user_"  # os.environ.get('USER_PREFIX'),

    @staticmethod
    def create_single_directory(user, current_path, dir_name):

        new_directory_path = Directory.BASE_PATH + Directory.USER_PREFIX + str(user) + "/" + current_path + dir_name
        current_directory_path = Directory.BASE_PATH + Directory.USER_PREFIX + str(user) + "/" + current_path

        print(new_directory_path)
        print(current_directory_path)

        try:

            if not Path(new_directory_path).is_dir():
                Path(new_directory_path).mkdir()
                return get_current_directory(current_directory_path)

            return {"message": "Folder already exists", "status": "failed"}

        except FileExistsError:

            return {"message": "Something went wrong while creating your folder", "status": "failed"}
