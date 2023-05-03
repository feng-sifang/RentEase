from django.views.generic import TemplateView
from rest_framework import status, generics
from rest_framework.decorators import api_view

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Property
from .serializers import PropertySerializer, PropertyQuerySerializer, PropertyCreateSerializer, PropertyListSerializer

class HomeView(TemplateView):
    template_name = 'home.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class UserProfileView(TemplateView):
    template_name = 'user-profile.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class PropertyList(TemplateView):
    template_name = 'property-list.html'


class UserCreditCard(TemplateView):
    template_name = 'user-creditcard.html'


class UserAddCreditCard(TemplateView):
    template_name = 'user-add-creditcard.html'


class PropertyQueryAPIView(CreateAPIView):
    serializer_class = PropertyQuerySerializer

    def create(self, request, *args, **kwargs):
        serializer = PropertyQuerySerializer(data=request.data)
        if serializer.is_valid():
            property_type = serializer.validated_data.get('property_type')
            property_city = serializer.validated_data.get('property_city')

            min_price = serializer.validated_data.get('min_price')
            max_price = serializer.validated_data.get('max_price')

            filters = {}
            if property_type:
                filters['property_type'] = property_type
            if property_city:
                filters['property_city'] = property_city
            if min_price and max_price:
                filters['property_price__range'] = (min_price, max_price)
            elif min_price:
                filters['property_price__gte'] = min_price
            elif max_price:
                filters['property_price__lte'] = max_price

            queryset = Property.objects.filter(**filters)
            serialized_data = PropertyListSerializer(queryset, many=True).data
            return Response(serialized_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyAddView(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyCreateSerializer


class PropertyDetailView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'property_id'

