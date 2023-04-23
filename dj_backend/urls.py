from django.urls import path
from dj_backend.views import *
from dj_backend.posts_handler import *

app_name = "dj_backend"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('property_list/', PropertyList.as_view(), name='property_list'),
    path('post-signin/', post_signin, name='post-signin'),
    path('user-profile/', UserProfileView.as_view(), name='user'),
    path('property/findAll/', property_findAll, name='property_findAll'),
    path('property/find/', PropertyQueryAPIView.as_view(), name='property_find'),
    path('property/side_card/', property_side_card, name='property_side_card'),
    path('property/add/', PropertyAddView.as_view(), name='property-add'),

]
