# Add your code below
''''
location mself.APPing module

modules used geopy

'''

# author
__author__ = ("aadilvarsh", "https://github.com/aadilvarsh")
# author end


from geopy.geocoders import Nominatim
import geopy
import json


class loc:

    def __init__(self):
        self.APP = Nominatim(user_agent=__name__)

    def locate(self, address: str):
        '''
            method to return raw
            args: address

        '''

        loc_ = self.APP.geocode(address)

        if loc_ is not None:
            return loc_.raw

        else:
            return {'status': 404}
