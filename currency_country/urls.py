from django.urls import path

from .views import country, country_by_name



urlpatterns = [

    path('country/', country, name="country"),
    path('country_by_name/', country_by_name, name="country_by_name"),

]