import json
from dj_backend.models import Users
from django.http import JsonResponse


def post_signin(request):
    data = json.loads(request.body)

    user_email = data["login-email"]
    user_password = data["login-password"]

    if Users.objects.filter(user_email__exact=user_email, user_password__exact=user_password):
        response = {
            "success": True,
            "user_type": Users.objects.get(user_email__exact=user_email).user_type
        }
    else:
        response = {
            "success": False
        }
    return JsonResponse(response)
