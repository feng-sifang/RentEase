import json
from django.http import JsonResponse
from dj_backend.models import Users


def check_login(request):
    response = {}
    if request.user.is_authenticated:
        response = {
            "success": True,
            "is_logged_in": True,
            "user_first_name": Users.objects.get(user_email=request.user.email).user_first_name,
            "user_type": Users.objects.get(user_email=request.user.email).user_type,
        }
    return JsonResponse(response)
