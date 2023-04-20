from django.urls import path
from dj_backend.views import *
from dj_backend.posts_handler import *

app_name = "dj_backend"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('post-signin/', post_signin, name='post-signin'),
    path('user-profile/', UserProfileView.as_view(), name='user'),
    path('register/', RegisterView.as_view(), name='register'),
    path('post-register/', post_register, name='post-register')
]
