from django.urls import path
from dj_backend.views import *
from dj_backend.request_handler import *

app_name = "dj_backend"
urlpatterns = [
    path('',                                    HomeView.as_view(), name='home'),
    path('login/',                              LoginView.as_view(), name='login'),
    path('register/',                           RegisterView.as_view(), name='register'),
    path('user-profile/',                       UserProfileView.as_view(), name='user_profile'),
    path('user-creditcard/',                    UserCreditCard.as_view(), name='user_credit_card'),
    path('user-add-creditcard/',                UserAddCreditCard.as_view(), name='user_add_credit_card'),
    path('property/list/',                      PropertyList.as_view(), name='property_list'),
    path('property/find/',                      PropertyQueryAPIView.as_view(), name='property_find'),
    path('property/add/',                       PropertyAddView.as_view(), name='property_add'),

    path('property/detail/<int:property_id>/',  property_detail, name='property-detail'),
    path('get-user-by-id/<int:user_id>/',       get_user_by_id, name='get_user_by_id'),
    path('property/edit/<int:property_id>/',    update_property, name='property-update'),
    path('property/delete/<int:property_id>/',  delete_property, name='property-delete'),
    path('post-signin/',                        post_signin, name='post_signin'),
    path('post-register/',                      post_register, name='post_register'),
    path('logout/',                             logout_handler, name='logout'),
    path('get-user-profile/',                   get_user_profile, name='get_user_profile'),
    path('save-user-profile/',                  save_user_profile, name='save_user_profile'),
    path('get-user-creditcard/',                get_user_creditcard, name='get_user_creditcard'),
    path('add-user-creditcard/',                add_user_creditcard, name='add_user_creditcard'),
    path('property/side-card/',                 property_side_card, name='property_side_card'),
    path('property/city-list/',                 property_city_list, name='property_city_list'),
    path('save-user-creditcard/',               save_user_creditcard, name='add_property'),
    path('get-points/',                         get_points, name='get_points'),
]
