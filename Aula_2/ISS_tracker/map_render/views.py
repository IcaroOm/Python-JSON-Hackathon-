from django.shortcuts import render
from django.http import JsonResponse
import requests
from .models import IssLocation
from datetime import datetime
import folium


def fetch_and_store_iss_data():
    api_url = "https://api.wheretheiss.at/v1/satellites/25544"
    response = requests.get(api_url)
    data = response.json()
    timestamp = datetime.utcfromtimestamp(data['timestamp'])
    IssLocation.objects.create(
        timestamp=timestamp,
        latitude=data['latitude'],
        longitude=data['longitude']
    )


def display_iss_map(request):
    iss_locations = IssLocation.objects.all()
    m = folium.Map(location=[iss_locations.last().latitude, iss_locations.last().longitude], zoom_start=2)

    for location in iss_locations:
        folium.Marker([location.latitude, location.longitude], popup=str(location.timestamp)).add_to(m)

    return render(request, 'map_render/iss_map.html', {'map': m._repr_html_()})


def update_map(request):
    fetch_and_store_iss_data()  # Fetch and store ISS data
    return JsonResponse({'status': 'success'})
