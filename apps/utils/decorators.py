from django.core.exceptions import PermissionDenied


def require_ajax(view):
    def _wrapped_view(request, *args, **kwargs):
        if request.is_ajax():
            return view(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    return _wrapped_view
