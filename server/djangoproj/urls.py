from django.urls import path, include
from django.views.generic import RedirectView
from djangoapp import views

urlpatterns = [
    path('djangoapp/', include('djangoapp.urls')),
    path('', views.index, name='index'),
    path('dealers/', views.index), # عشان لو المتصفح معلق على كلمة dealers
]
