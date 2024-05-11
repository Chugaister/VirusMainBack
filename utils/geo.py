from typing import Optional
from typing import Tuple
from geopy.geocoders import Nominatim


def address_to_coordinates(address) -> Tuple[Optional[float], Optional[float]]:
    geolocator = Nominatim(user_agent="your_app_name")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

