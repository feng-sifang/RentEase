import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from dj_backend.models import Users


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

    print(data)
    if Users.objects.filter(email__exact=user_email):
        response = {
            "success": False
        }
    else:
        # create a new user in the official django user table
        user = Users.objects.create_user(
            username=user_email,
            email=user_email,
            last_name=user_last_name,
            first_name=user_first_name,
            password=user_password,
            user_type=user_type,
            total_cost=0
        )
        user.save()

        response = {
            "success": True
        }
    return JsonResponse(response)


def logout_handler(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({"success": True})


def get_user_info(request):
    if request.user.is_authenticated:
        user = Users.objects.get(id=request.user.id)
        response = {
            "success": True,
            "is_logged_in": request.user.is_authenticated,
            "type": user.user_type,
            
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone_number,
            "location": user.location,
            "about_me": user.about_me,
            "total_cost": user.total_cost,
        }
        return JsonResponse(response)
    else:
        return JsonResponse({"success": False})


def save_user_profile(request):
    data = json.loads(request.body)
    if request.user.is_authenticated:
        user = Users.objects.get(id=request.user.id)
        user.first_name = data["first_name"]
        user.last_name = data["last_name"]
        user.email = data["email"]
        user.phone_number = data["phone"]
        user.location = data["location"]
        user.about_me = data["about_me"]
        user.save()
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})
