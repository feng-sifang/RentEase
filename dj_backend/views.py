from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import status, generics
from rest_framework.mixins import CreateModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from .models import Property
from .serializers import PropertySerializer, PropertyQuerySerializer, PropertyCreateSerializer
from .filters import PropertyFilter

class HomeView(TemplateView):
    template_name = 'home.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class UserProfileView(TemplateView):
    template_name = 'user-profile.html'


class PropertyList(TemplateView):
    template_name = 'property_list.html'



class PropertyFindAPIView(CreateModelMixin, ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PropertyFilter
    ordering_fields = ['property_price']
    ordering = ['property_price']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PropertyQueryAPIView(CreateAPIView):
    serializer_class = PropertyQuerySerializer
    def create(self, request, *args, **kwargs):
        serializer = PropertyQuerySerializer(data=request.data)
        if serializer.is_valid():
            property_type = serializer.validated_data.get('property_type')
            min_price = serializer.validated_data.get('min_price')
            max_price = serializer.validated_data.get('max_price')

            filters = {}
            if property_type:
                filters['property_type'] = property_type
            if min_price and max_price:
                filters['property_price__range'] = (min_price, max_price)
            elif min_price:
                filters['property_price__gte'] = min_price
            elif max_price:
                filters['property_price__lte'] = max_price

            queryset = Property.objects.filter(**filters)
            serialized_data = PropertySerializer(queryset, many=True).data
            return Response(serialized_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PropertyAddView(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyCreateSerializer