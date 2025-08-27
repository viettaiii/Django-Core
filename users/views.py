from django.contrib.auth import get_user_model
from core.views import CoreTablePage

User = get_user_model()

class UserPage(CoreTablePage):
    model = User
    page_title = "Users"
    page_actions = [{"label": "Create User", "href": "/admin/auth/user/add/"}]
    
    columns = [
        {"field": "id", "label": "ID", "orderable": True},
        {"field": "username", "label": "Username"},
        {"field": "email", "label": "Email"},
        {"field": "is_active", "label": "Active", "type": "boolean"},
        {"field": "date_joined", "label": "Joined", "type": "datetime", "format": "Y-m-d H:i"},
    ]
    
    filters = {
        "username": {"lookup": "icontains", "type": "text"},
        "email": {"lookup": "icontains", "type": "text"},
        "is_active": {"type": "boolean"},
        # map alias -> model field via `field`
        "joined_after": {"type": "date", "lookup": "gte", "field": "date_joined"},
    }
