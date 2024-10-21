
# import requests
# from django.conf import settings

# TREFLE_API_URL = 'https://trefle.io/api/v1'

# def search_plants(query):
#     url = f"{TREFLE_API_URL}/plants"
#     params = {
#         'token': settings.TREFLE_API_KEY,
#         'q': query
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         return response.json()['data']
#     return []


import requests
from django.conf import settings

# Correct API Endpoint for searching plants
TREFLE_API_SEARCH_URL = 'https://trefle.io/api/v1/plants/search'

def search_plants(query):
    url = TREFLE_API_SEARCH_URL
    params = {
        'token': settings.TREFLE_API_KEY,  # Ensure this is correctly set in your settings
        'q': query
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        # Log the error for debugging
        print(f"Error fetching data from Trefle API: {response.status_code} - {response.text}")
        return []
