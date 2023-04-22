from django.urls import path
from dj_backend.views import *
from dj_backend.posts_handler import *
from dj_backend.api import *

app_name = "dj_backend"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('post-signin/', post_signin, name='post-signin'),
    path('user-profile/', UserProfileView.as_view(), name='user-profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('post-register/', post_register, name='post-register'),
    path('check-login/', check_login, name='check-login'),
]
