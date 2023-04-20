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


def post_register(request):
    data = json.loads(request.body)
    user_first_name = data["first_name"]
    user_last_name = data["last_name"]
    user_email = data["email"]
    user_password = data["password"]
    user_type = data["user_type"]

    if Users.objects.filter(user_email__exact=user_email):
        response = {
            "success": False
        }
    else:
        new_user = Users(user_first_name=user_first_name,
                         user_last_name=user_last_name,
                         user_email=user_email,
                         user_password=user_password,
                         user_type=user_type,
                         user_total_cost=0
                         )
        new_user.save()
        response = {
            "success": True
        }
    return JsonResponse(response)
