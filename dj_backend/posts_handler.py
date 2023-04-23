import json

from django.core import serializers
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt

from dj_backend.models import Users, Property
from django.http import JsonResponse



@csrf_exempt
def post_signin(request):
    data = json.loads(request.body)

    user_email = data["login-email"]
    user_password = data["login-password"]

    if Users.objects.filter(user_email__exact=user_email, user_password__exact=user_password):
        response = {
            "success": True
        }
    else:
        response = {
            "success": False
        }
    return JsonResponse(response)


def create_response(success, code, message, data=None):
    response_data = {
        'success': success,
        'code': code,
        'message': message,
        'data': data or {},
    }
    return JsonResponse(response_data)

def success_response(data=None):
    return create_response(True, 20000, 'Success', data)

def error_response(message=None, code=20001):
    return create_response(False, code, message or 'Failed')
def property_findAll(request):
    data = Property.objects.all()
    properties_json = serializers.serialize('json', data)
    properties_data = json.loads(properties_json)
    # Remove the 'model' from the serialized data
    clean_properties_data = [{**property_data['fields'], 'id': property_data['pk']} for property_data in
                             properties_data]
    return success_response(clean_properties_data)


def property_side_card(request):
    grouped_by_type = Property.objects.values('property_type').annotate(total_count=Count('property_id'))
    grouped_by_city = Property.objects.values('property_city').annotate(total_count=Count('property_id'))
    grouped_by_availability = Property.objects.values('property_availability').annotate(total_count=Count('property_id'))

    type_data = list(grouped_by_type)
    city_data = list(grouped_by_city)
    availability_data = list(grouped_by_availability)

    return JsonResponse({
        'type_data': type_data,
        'city_data': city_data,
        'availability_data': availability_data,
    })

