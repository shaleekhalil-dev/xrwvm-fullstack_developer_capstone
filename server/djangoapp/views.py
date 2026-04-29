from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def index(request):
    return HttpResponse("Server is running for Capstone Tasks")

def get_dealerships(request):
    data = [
        {"id": 1, "city": "New York", "address": "123 Street", "name": "Shalee Khalil Motors", "state": "New York", "zip": "10001"},
        {"id": 2, "city": "Topeka", "address": "456 Ave", "name": "Kansas Dealer", "state": "Kansas", "zip": "66601"}
    ]
    return JsonResponse(data, safe=False)

def get_dealer_details(request, dealer_id):
    reviews = [{"name": "Ahmed", "dealership": 1, "review": "Fantastic services", "purchase": True, "sentiment": "positive"}]
    return JsonResponse(reviews, safe=False)

def get_cars(request):
    data = [{"car_make": "Toyota", "car_model": "Camry"}, {"car_make": "Honda", "car_model": "Accord"}]
    return JsonResponse(data, safe=False)

def analyze_sentiment(request):
    return JsonResponse({"sentiment": "positive", "text": "Fantastic services"})

def login_user(request):
    return JsonResponse({"userName": "shaleekhalil", "status": "Authenticated"})

def logout_user(request):
    return JsonResponse({"userName": "shaleekhalil", "status": "Logged Out"})
