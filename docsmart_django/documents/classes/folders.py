import os
from permissions.classes.permission_engine import Engine


def get_user_files(path, user) -> dict:
    folder = {}
    documents = Engine.fetch_accessible_files_by_name(os.path.basename(path).lower(), user)

    if len(documents) > 0:

        for document in documents:
            perm = {'document_id': document.id,
                    'date_last_edited': document.date_last_edited,
                    'created_at': document.created_at,
                    'updated_at': document.updated_at,
                    'permissions': {'can_view': document.permissions}
                    #                 'can_edit': document.permissions.id,
                    #                 'can_delete': document.permissions.id}
                    }
            folder[document.id] = perm

    d = {'name': os.path.basename(path), 'permissions': folder}

    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [get_user_files(path=os.path.join(path, x), user=user) for x in os.listdir(path)]
    else:
        d['type'] = "file"

    return d


def get_company_files() -> dict:
    pass


def get_current_directory(path) -> dict:
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [get_user_files(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"

    return d
