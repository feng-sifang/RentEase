from rest_framework import serializers

from .models import Property, House, CommercialBuilding


class PropertyQuerySerializer(serializers.Serializer):
    property_type = serializers.CharField(allow_blank=True)
    property_city = serializers.CharField(allow_blank=True)
    min_price = serializers.CharField(allow_blank=True)
    max_price = serializers.CharField(allow_blank=True)


class PropertyCreateSerializer(serializers.ModelSerializer):
    num_of_rooms = serializers.CharField(required=False)
    business_type = serializers.CharField(required=False)

    class Meta:
        model = Property
        fields = ('property_type', 'property_price', 'property_description',
                  'property_address', 'property_city', 'property_state', 'property_price',
                  'user_id', 'num_of_rooms', 'business_type')

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
        elif property_type == 'CommercialBuilding':
            commercial_building = CommercialBuilding.objects.create(**validated_data)
            return commercial_building
        else:
            raise serializers.ValidationError("Invalid property_type")


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('num_of_rooms',)


class PropertySerializer(serializers.ModelSerializer):
    house = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = ('property_id', 'property_type', 'property_description','property_price','property_address',
                  'property_city','property_state','user_id', 'house')

    def get_house(self, obj):
        if obj.property_type == "House":
            house_obj = House.objects.get(pk=obj.pk)
            return HouseSerializer(house_obj).data
        return None

    def to_representation(self, instance):
        # Get the original representation
        ret = super().to_representation(instance)
        # Merge the 'house' field into the main representation
        if ret['house'] is not None:
            house_data = ret.pop('house')
            ret.update(house_data)
        return ret
