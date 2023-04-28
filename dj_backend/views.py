from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import status, generics, mixins
from rest_framework.mixins import CreateModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from .models import Property
from .serializers import PropertySerializer, PropertyQuerySerializer, PropertyCreateSerializer, PropertyListSerializer, \
    PropertyUpdateSerializer
from .filters import PropertyFilter


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


class PropertyUpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyUpdateSerializer
    lookup_field = 'property_id'

    def get_object(self):
        obj = super().get_object()
        if self.request.data.get('property_type') == 'House':
            obj = obj.as_house()
        elif self.request.data.get('property_type') == 'CommercialBuilding':
            obj = obj.as_commercial_building()
        return obj

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        print(instance)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class PropertyDetailView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'property_id'
