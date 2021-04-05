import os
from permissions.classes.permission_engine import Engine


def get_user_files(path) -> dict:

    folder = {}
    permissions = Engine.fetch_accessible_files_by_name(os.path.basename(path).lower())

    if len(permissions) > 0:

        for permission in permissions:
            perm = {'document_id': permission.document_id.id,
                    'user_id': permission.user_id.id,
                    'can_view': permission.can_view,
                    'can_edit': permission.can_edit,
                    'can_delete': permission.can_delete}
            folder[permission.document_id.id] = perm

    d = {'name': os.path.basename(path), 'permissions': folder}

    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [get_user_files(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"

    return d
