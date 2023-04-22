import json
from dj_backend.models import Users
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def post_signin(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        username = data["login_email"]
        password = data["login_password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = {"success": True}
            return JsonResponse(response)

    response = {"success": False}
    return JsonResponse(response)


def post_register(request):
    data = json.loads(request.body)
    user_first_name = data["first_name"]
    user_last_name = data["last_name"]
    user_email = data["email"]
    user_password = data["password"]
    user_type = data["user_type"]

    # ! caution: here the users table is not an official django user table
    if Users.objects.filter(user_email__exact=user_email):
        response = {
            "success": False
        }
    else:
        # create a new user in the official django user table
        user = User.objects.create_user(
            username=user_email,
            email=user_email,
            last_name=user_last_name,
            first_name=user_first_name,
            password=user_password)
        user.save()
        # create a new user in the users table
        new_user = Users(
            user_first_name=user_first_name,
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
