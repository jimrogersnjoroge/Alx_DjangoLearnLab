Managing Permissions and Groups in Django
Creating and Configure Groups with Assigned Permissions:
The application has the following groups defined with each detailing the permissions  assigned:

Editors Group:
They have can_edit and can_create permissions
Viewers Group:
They have can_view permission only
Admins Group:
They have can_create, can_edit and can_view permissions

Enforncing persmissions:
Permissions are enforced using the @permission_required(bookshelf.permission, raise_exception=True) decorator