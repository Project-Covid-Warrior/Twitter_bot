''''
location mself.APPing module

modules used geopy

'''

# author
__author__ = ("aadilvarsh", "https://github.com/aadilvarsh")
# author end


import pprint
from geopy.geocoders import Nominatim
import geopy


# constans

class loc:

    def __init__(self):
        self.APP = Nominatim(user_agent=__name__)

    def locate(self, address: str):
        '''
            method to return raw
            args: address

        '''

        loc_ = self.APP.geocode(address)

        if loc is not None:
            return pprint.pformat(loc_.raw)

        else:
            return {'status': 404}

    def coords(self, address: str):
        '''
            method to return cords
            args: address
        '''

        loc_ = self.APP.geocode(address)

        if loc_ is not None:
            lat = loc_.raw['lat']
            lon = loc_.raw['lon']

            return {'coords': (lat, lon),
                    'lat': lat,
                    'lon': lon, }
        else:

            return {'status': 404}

    def address_map(self, address: str):
        '''
            method to map elements out of address
            args:
            address
        '''

        loc_ = self.APP.geocode(address)

        if loc_ is not None:
            loc_ = loc_.raw

            addr = loc_['display_name']
            class_ = loc_['type']

            return {
                'addr': addr,
                'class': class_
            }
        else:

            return {'status': 404}
