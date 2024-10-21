import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)
TREFLE_API_SEARCH_URL = 'https://trefle.io/api/v1/plants/search'

def search_plants(query):
    url = TREFLE_API_SEARCH_URL
    params = {
        'token': settings.TREFLE_API_KEY,
        'q': query
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json().get('data', [])
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.text}")
    except requests.exceptions.RequestException as err:
        logger.error(f"Request exception: {err}")
    return []
