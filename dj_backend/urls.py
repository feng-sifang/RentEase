from django.urls import path
from dj_backend.views import *
from dj_backend.request_handler import *

app_name = "dj_backend"
urlpatterns = [
    path('',                               HomeView.as_view(), name='home'),
    path('login/',                         LoginView.as_view(), name='login'),
    path('register/',                      RegisterView.as_view(), name='register'),
    path('user-profile/',                  UserProfileView.as_view(), name='user_profile'),
    path('user-profile/credit-card/',      AddCreditCard.as_view(), name='add_credit_card'),
    path('property/list/',                 PropertyList.as_view(), name='property_list'),
    path('property/find/',                 PropertyQueryAPIView.as_view(), name='property_find'),
    path('property/add/',                  PropertyAddView.as_view(), name='property_add'),

    path('post-signin/',                   post_signin, name='post_signin'),
    path('post-register/',                 post_register, name='post_register'),
    path('logout/',                        logout_handler, name='logout'),
    path('get-user-profile/',              get_user_info, name='get_user_profile'),
    path('save-user-profile/',             save_user_profile, name='save_user_profile'),
    path('property/side-card/',            property_side_card, name='property_side_card'),
]
