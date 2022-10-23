from .folders import get_user_folder, get_company_folder
from company.models import Company


class Generator:
    # Macos Base Path: /var/www/html/storage/
    # Windows Base Path: /Users/DELL/Documents/Projects/storage/
    BASE_PATH = "/var/www/html/storage/"  # os.environ.get('BASE_PATH'),
    FOLDER_PREFIX = "user_"  # os.environ.get('BASE_PATH'),

    @staticmethod
    def generate_user_folder_object(user_id):
        return get_user_folder(path=Generator.BASE_PATH + Generator.FOLDER_PREFIX + user_id, user=user_id)
    

    @staticmethod
    def generate_company_folder_object(user_id):

        company = Company.objects.get(user__id=user_id)
        return get_company_folder(path=Generator.BASE_PATH + Generator.FOLDER_PREFIX + user_id, user=user_id, company=company.id)
