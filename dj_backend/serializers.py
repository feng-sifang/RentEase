from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from .models import Property, House, CommercialBuilding, Apartment, Land, VacationHome


class PropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class PropertyQuerySerializer(serializers.Serializer):
    property_type = serializers.CharField(allow_blank=True)
    property_city = serializers.CharField(allow_blank=True)
    min_price = serializers.CharField(allow_blank=True)
    max_price = serializers.CharField(allow_blank=True)


class PropertyCreateSerializer(serializers.ModelSerializer):
    num_of_rooms = serializers.CharField(required=False)
    business_type = serializers.CharField(required=False)
    building_type = serializers.CharField(required=False)
    land_size = serializers.CharField(required=False)
    characteristics = serializers.CharField(required=False)

    class Meta:
        model = Property
        fields = ('property_type', 'property_price', 'property_description',
                  'property_address', 'property_city', 'property_state', 'property_price',
                  'user_id', 'neighbour', 'num_of_rooms', 'business_type', 'building_type', 'land_size',
                  'characteristics')

    def validate_num_of_rooms(self, value):
        try:
            return int(value)
        except ValueError:
            raise serializers.ValidationError("Rooms must be a valid integer")

    def create(self, validated_data):
        property_type = validated_data['property_type'] = validated_data.pop('property_type')
        if property_type == 'House':
            validated_data['num_of_rooms'] = validated_data.pop('num_of_rooms', None)
            house = House.objects.create(**validated_data)
            return house
        elif property_type == 'Apartment':
            apartment = Apartment.objects.create(**validated_data)
            return apartment
        elif property_type == 'CommercialBuilding':
            commercial_building = CommercialBuilding.objects.create(**validated_data)
            return commercial_building
        elif property_type == 'Land':
            land = Land.objects.create(**validated_data)
            return land
        elif property_type == 'Vacation Home':
            vacation_home = VacationHome.objects.create(**validated_data)
            return vacation_home
        else:
            raise serializers.ValidationError("Invalid property_type")
