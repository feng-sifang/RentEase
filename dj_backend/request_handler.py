import json

from django.db.models import Count
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from dj_backend.models import Users, Property, Renters, Agents, CreditCard, House, CommercialBuilding, Apartment, Land, \
    VacationHome
from datetime import datetime


def post_signin(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        username = data["login_email"]
        password = data["login_password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = {"success": True}
            return JsonResponse(response)

    response = {"success": False}
    return JsonResponse(response)


def post_register(request):
    data = json.loads(request.body)
    user_first_name = data["first_name"]
    user_last_name = data["last_name"]
    user_email = data["email"]
    user_password = data["password"]
    user_type = data["user_type"]

    if Users.objects.filter(email__exact=user_email):
        response = {
            "success": False
        }
    else:
        if user_type == "Renter":
            # create a new user in the official django user table
            renter = Renters.objects.create_user(
                username=user_email,
                email=user_email,
                last_name=user_last_name,
                first_name=user_first_name,
                password=user_password,
                user_type=user_type,
                budget=0,
                desired_move_in_date="",
                total_cost=0
            )
            renter.save()

        elif user_type == "Agent":
            agent = Agents.objects.create_user(
                username=user_email,
                email=user_email,
                last_name=user_last_name,
                first_name=user_first_name,
                password=user_password,
                user_type=user_type,
            )
            agent.save()

        response = {
            "success": True
        }
    return JsonResponse(response)


def logout_handler(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({"success": True})


def get_user_profile(request):
    if request.user.is_authenticated:
        user = Users.objects.get(id=request.user.id)
        # response with common information
        response = {
            "user_id": user.id,
            "success": True,
            "is_logged_in": True,
            "user_type": user.user_type,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone_number,
            "location": user.location,
        }
        if user.user_type == "Renter":

            renter = Renters.objects.get(users_ptr_id=request.user.id)
            response = {
                **response,
                "rental_preferences": renter.rental_preferences,
                "desired_move_in_date": renter.desired_move_in_date,
                "preferred_location": renter.preferred_location,
                "budget": renter.budget,
                "total_cost": renter.total_cost,
            }

        elif user.user_type == "Agent":

            agent = Agents.objects.get(users_ptr_id=request.user.id)
            response = {
                **response,
                "job_title": agent.job_title,
                "company": agent.company,
                "contact_information": agent.contact_information,
            }

        return JsonResponse(response)
    else:
        return JsonResponse({"success": False})


def save_user_profile(request):
    data = json.loads(request.body)
    if request.user.is_authenticated:
        user = Users.objects.get(id=request.user.id)
        user.first_name = data["first_name"]
        user.last_name = data["last_name"]
        user.email = data["email"]
        user.phone_number = data["phone"]
        user.location = data["location"]
        user.save()

        if user.user_type == "Renter":
            renter = Renters.objects.get(users_ptr_id=user.id)
            renter.rental_preferences = data["rental_preferences"]
            renter.desired_move_in_date = data["desired_move_in_date"]
            renter.preferred_location = data["preferred_location"]
            renter.budget = data["budget"]

            renter.save()

        elif user.user_type == "Agent":
            agent = Agents.objects.get(users_ptr_id=user.id)
            agent.job_title = data["job_title"]
            agent.company = data["company"]
            agent.contact_information = data["contact_information"]

            agent.save()

        return JsonResponse({"success": True})

    else:
        return JsonResponse({"success": False})


def property_side_card(request):
    grouped_by_type = Property.objects.values('property_type').annotate(total_count=Count('property_id'))
    grouped_by_city = Property.objects.values('property_city').annotate(total_count=Count('property_id'))
    grouped_by_availability = Property.objects.values('property_availability').annotate(
        total_count=Count('property_id'))

    type_data = list(grouped_by_type)
    city_data = list(grouped_by_city)
    availability_data = list(grouped_by_availability)

    return JsonResponse({
        'type_data': type_data,
        'city_data': city_data,
        'availability_data': availability_data,
    })


def get_user_creditcard(request):
    if request.user.is_authenticated:
        credit_cards = CreditCard.objects.filter(user_id_id=request.user.id)
        credit_cards_list = [model_to_dict(card) for card in credit_cards]

        if len(credit_cards_list) == 0:
            return JsonResponse({"success": False})
        return JsonResponse({"success": True, "credit_cards": credit_cards_list}, safe=False)
    else:
        return JsonResponse({"success": False})


def add_user_creditcard(request):
    data = json.loads(request.body)
    expiry_date = datetime.strptime(data['expiry_date'], '%Y-%m-%d').date()
    print(data)
    new_card = CreditCard.objects.create(
        number=data['number'],
        holder_name=data['holder_name'],
        expiry_date=expiry_date,
        cvv=data['cvv'],
        street=data['street'],
        city=data['city'],
        zip=data['zip'],
        country=data['country'],
        user_id_id=request.user.id,
    )
    new_card.save()

    return JsonResponse({"success": True})


def save_user_creditcard(request):
    data = json.loads(request.body)
    for creditcard in data['creditCards']:
        card = CreditCard.objects.get(credit_card_id=creditcard['credit_card_id'])
        card.number = creditcard['number']
        card.holder_name = creditcard['holder_name']
        card.expiry_date = creditcard['expiry_date']
        card.cvv = creditcard['cvv']
        card.street = creditcard['street']
        card.city = creditcard['city']
        card.zip = creditcard['zip']
        card.country = creditcard['country']
        card.save()

    return JsonResponse({"success": True})


def get_points(request):
    if request.user.is_authenticated:
        user = Renters.objects.get(id=request.user.id)

        return JsonResponse({"success": True, "total_points": int(user.total_cost)})
    else:
        return JsonResponse({"success": False})


def update_property(request, property_id):
    data = json.loads(request.body)
    property = Property.objects.get(property_id=property_id)
    property.property_type = data["property_type"]
    property.property_description = data["property_description"]
    property.property_city = data["property_city"]
    property.property_state = data["property_state"]
    property.property_address = data["property_address"]
    property.property_price = data["property_price"]
    property.save()

    if property.property_type == "House":
        house = House.objects.get(property_ptr_id=property_id)
        house.num_of_rooms = data["num_of_rooms"]
        house.save()

    elif property.property_type == "CommercialBuilding":
        commercial_building = CommercialBuilding.objects.get(property_ptr_id=property_id)
        commercial_building.business_type = data["business_type"]
        commercial_building.save()

    elif property.property_type == "Apartment":
        apartment = Apartment.objects.get(property_ptr_id=property_id)
        apartment.num_of_rooms = data["num_of_rooms"]
        apartment.building_type = data["building_type"]
        apartment.save()

    elif property.property_type == "Land":
        land = Land.objects.get(property_ptr_id=property_id)
        land.land_size = data["land_size"]
        land.save()

    elif property.property_type == "VacationHome":
        vacation_home = VacationHome.objects.get(property_ptr_id=property_id)
        vacation_home.characteristics = data["characteristics"]
        vacation_home.save()

    return JsonResponse({"success": True})


def property_detail(request, property_id):
    property = Property.objects.get(property_id=property_id)
    response = {
        "property_id": property.property_id,
        "property_type": property.property_type,
        "property_description": property.property_description,
        "property_city": property.property_city,
        "property_state": property.property_state,
        "property_address": property.property_address,
        "property_price": property.property_price,
    }
    print(property.property_type)
    if property.property_type == "House":
        house = House.objects.get(property_ptr_id=property_id)
        response = {
            **response,
            "num_of_rooms": house.num_of_rooms,
        }

    elif property.property_type == "CommercialBuilding":
        commercial_building = CommercialBuilding.objects.get(property_ptr_id=property_id)
        response = {
            **response,
            "business_type": commercial_building.business_type,
        }

    elif property.property_type == "Apartment":
        apartment = Apartment.objects.get(property_ptr_id=property_id)
        response = {
            **response,
            "num_of_rooms": apartment.num_of_rooms,
            "building_type": apartment.building_type,
        }

    elif property.property_type == "Land":
        land = Land.objects.get(property_ptr_id=property_id)
        response = {
            **response,
            "land_size": land.land_size,
        }

    elif property.property_type == "VacationHome":
        vacation_home = VacationHome.objects.get(property_ptr_id=property_id)
        response = {
            **response,
            "characteristics": vacation_home.characteristics,
        }

    return JsonResponse(response)
