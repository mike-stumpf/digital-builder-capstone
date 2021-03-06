import os
import googlemaps
import logging

from ..enums import *


def get_location_for_zipcode(zipcode):
    """
    gets bounds from zip code
    :param zipcode: string or int
    :return: bounds dictionary
    """
    # https://developers.google.com/maps/documentation/geocoding/overview
    location = {
        location_latitude: None,
        location_longitude: None
    }
    google_api_key = os.getenv(env_google_api_key)
    gmaps = googlemaps.Client(key=google_api_key)
    geocode_result = gmaps.geocode(str(zipcode))
    try:
        if len(geocode_result) > 0:
            location = geocode_result[0]['geometry']['location']
    except Exception as err:
        logging.exception(err)
        pass
    return location
