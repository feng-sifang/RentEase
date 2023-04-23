from django.urls import path
from dj_backend.views import *
from dj_backend.request_handler import *

app_name = "dj_backend"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('property-list/', PropertyList.as_view(), name='property-list'),
    path('post-signin/', post_signin, name='post-signin'),
    path('user-profile/', UserProfileView.as_view(), name='user-profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('post-register/', post_register, name='post-register'),
    path('logout/', logout_handler, name='logout'),
    path('get-user-profile/', get_user_info, name='get-user-profile'),
    path('save-user-profile/', save_user_profile, name='save-user-profile'),
    path('property/find/', PropertyQueryAPIView.as_view(), name='property_find'),
    path('property/side_card/', property_side_card, name='property_side_card'),
    path('property/add/', PropertyAddView.as_view(), name='property-add')
]
