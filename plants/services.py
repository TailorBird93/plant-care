
import requests
from django.conf import settings

TREFLE_API_URL = 'https://trefle.io/api/v1'

def search_plants(query):
    url = f"{TREFLE_API_URL}/plants"
    params = {
        'token': settings.TREFLE_API_KEY,
        'q': query
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['data']
    return []
