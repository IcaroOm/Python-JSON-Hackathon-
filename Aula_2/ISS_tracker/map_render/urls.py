from django.urls import path
from .views import display_iss_map, update_map

urlpatterns = [
    path('map/', display_iss_map, name='display_iss_map'),
    path('update-map/', update_map, name='update_map'),
]
