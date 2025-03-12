from django.shortcuts import redirect
from functools import wraps
def require_auth(view_func):
    @wraps(view_func)
    def wrapper(req, *args, **kwargs):
        if not req.user.is_authenticated:
            return redirect('login_url')  
        return view_func(req, *args, **kwargs)
    return wrapper