import django_filters
from .models import Property


class PropertyFilter(django_filters.FilterSet):
    property_price = django_filters.RangeFilter()
    property_type = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Property
        fields = ['property_price', 'property_type']
