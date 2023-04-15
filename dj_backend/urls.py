from django.urls import path
from dj_backend.views import *

app_name = "dj_backend"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-profile/', UserProfileView.as_view(), name='user'),
]
