import os
from permissions.models import DocumentPermission
from permissions.classes.permission_engine import Engine


def get_user_folder(path, user) -> dict:
    folder = []
    documents = Engine.fetch_user_files_by_name(os.path.basename(path).lower(), user)

    if len(documents) > 0:

        for document in documents:
            perm = {'document_id': document.id,
                    'date_last_edited': document.date_last_edited,
                    'created_at': document.created_at,
                    'updated_at': document.updated_at,
                    'permissions': get_document_permissions(user, document.id)
                    }

            folder.append(perm)

    d = {'name': os.path.basename(path), 'items': folder}

    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [get_user_folder(path=os.path.join(path, x), user=user) for x in os.listdir(path)]
    else:
        d['type'] = "file"

    return d


def get_company_folder(path, user, company) -> dict:
    folder = []
    documents = Engine.fetch_company_files_by_name(os.path.basename(path).lower(), company, user)

    if len(documents) > 0:

        for document in documents:
            perm = {'document_id': document.id,
                    'date_last_edited': document.date_last_edited,
                    'created_at': document.created_at,
                    'updated_at': document.updated_at,
                    'permissions': get_document_permissions(user, document.id)
                    }

            folder.append(perm)

    d = {'name': os.path.basename(path), 'items': folder}

    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [get_company_folder(path=os.path.join(path, x), user=user, company=company) for x in
                         os.listdir(path)]
    else:
        d['type'] = "file"

    return d


def get_document_permissions(user, document) -> dict:
    permissions = DocumentPermission.objects.get(user_id=user, document_id=document)

    if permissions:
        return {
            'can_view': permissions.can_view,
            'can_edit': permissions.can_edit,
            'can_delete': permissions.can_delete
        }
    return {
        'can_view': False,
        'can_edit': False,
        'can_delete': False,
    }


def get_current_directory(path, user) -> dict:
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [get_user_folder(os.path.join(path, x), user) for x in os.listdir(path)]
    else:
        d['type'] = "file"

    return d
