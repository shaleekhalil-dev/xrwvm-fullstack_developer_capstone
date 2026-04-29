from django.urls import path
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_dealers', views.get_dealerships, name='get_dealers'),
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_details'),
    path('get_cars', views.get_cars, name='get_cars'),
    path('analyze', views.analyze_sentiment, name='analyze'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
]
