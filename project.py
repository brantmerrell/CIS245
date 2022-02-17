'''
project to get and print weather data from
https://openweathermap.org/current#data

Feedback from pseudocode draft:
 - lack of input validation to make sure a zipcode is a zipcode or a city name is alphabetical.
 - pass units=imperial|other into query string and let webservice do conversion work.

ToDo / Wishlist:
 - construct query parameter using requests library rather than manually
 - prompt user for country code so pgeocode can look up zip internationally
 - prompt user for measurement system, default according to country
 - get API key through interactive login to openweathermap.org
 - choose API endpoint through menu-based selection
 - print chart of weather forecast using ascii art
'''

import os
import unittest
from unittest import mock
import requests
import pylint
import pgeocode
# To-Do: app ID
    # hard-code?
    # get automatically?
    # get interactively?


def prompt_location_info():
    '''
    interactively obtain the city, state, and zip for which the user wishes to check the weather.
    '''
    result = {
        'city': '',
        'state': '',
        'zip': ''
    }
    result['city'] = input('city: ')
    result['state'] = input('state: ')
    result['zip'] = input('zip: ')
    return result


def location_info_is_valid(location):
    '''
    evaluate location info; call prompt_location_info if location info is invalid
    '''
    result = (True, 'no errors detected')
    if not isinstance(location, dict):
        return (False, 'location object must be a dict')
    for attribute in ['city', 'state', 'zip']:
        if attribute not in location.keys():
            result = (False, 'location dict must contain city, state, and zip keys')
        if not isinstance(location[attribute], str):
            result = (False, f'location object {attribute} must be a string')
    if not location['zip'].isnumeric():
        result = (False, 'zip must be numeric')
    if location['zip'].count('') != 6:
        result = (False, 'zip must be a 5-digit number')
    if not location['city'].isalpha():
        result = (False, 'city must be alphabetical')
    if not location['state'].isalpha():
        result = (False, 'state must be alphabetical')
    return result


def construct_url(zip_code, api_key, country_code='us'):
    '''
    constructs url from
        - API Key
        - latitude & longitude
        - prompt_information_info
    '''
    result = 'http://api.openweathermap.org/data/2.5/weather?'
    zips = pgeocode.Nominatim(country_code)
    zip_data = zips.query_postal_code(zip_code)
    latitude = zip_data['latitude']
    longitude = zip_data['longitude']
    result += f'lat={latitude}&lon={longitude}&appid={api_key}'
    return result


def get_weather(weather_url):
    '''
    get weather from input url

    merge with construct_url?
    '''
    response = requests.get(weather_url).json()
    return response['main']


API_KEY = os.getenv('OPEN_WEATHER_API_KEY')
if API_KEY is None:
    API_KEY = input('please provide API key: ')
    os.environ['OPEN_WEATHER_API_KEY'] = API_KEY


class TestProject(unittest.TestCase):
    '''
    class for all unit tests of this project:
        - test_prompt_location_info
        - test_location_info_is_valid
        - test_construct_url
        - test_get_weather
    '''


    def test_prompt_location_info(self):
        '''
        function 'prompt_location_info' should
            - prompt for city, state, zip
            - return dictionary of string values for city, state, zip
        '''
        mock_args = ['Austin', 'TX', '78727']
        with mock.patch('builtins.input') as mocked_input:
            mocked_input.side_effect = mock_args
            result = prompt_location_info()
        self.assertEqual(result['city'], 'Austin')
        self.assertEqual(result['state'], 'TX')
        self.assertEqual(result['zip'], '78727')


    def test_location_info_is_valid(self):
        '''
            function 'location_info_is_valid' should
                - return (bool, message) tuple
                - require numeric zip
                - require 5-character zip
                - require alphabetic city
                - require alphabetic state
        '''
        good_location = {
            'city': 'Austin',
            'state': 'TX',
            'zip': '78727'
            }
        location_as_list = ['Austin', 'TX', '78727']
        location_with_numeric_city = {
            'city': 'Aus1in',
            'state': 'TX',
            'zip': '78727'
            }
        location_with_numeric_state = {
            'city': 'Austin',
            'state': '5X',
            'zip': '78727'
            }
        location_with_letter_zip = {
            'city': 'Austin',
            'state': 'TX',
            'zip': '787d7'
            }
        location_with_short_zip = {
            'city': 'Austin',
            'state': 'TX',
            'zip': '7877'
            }
        self.assertTrue(location_info_is_valid(good_location)[0])
        self.assertEqual(
            location_info_is_valid(location_as_list),
            (False, 'location object must be a dict'))
        self.assertEqual(
            location_info_is_valid(location_with_numeric_city),
            (False, 'city must be alphabetical'))
        self.assertEqual(
            location_info_is_valid(location_with_numeric_state),
            (False, 'state must be alphabetical'))
        self.assertEqual(
            location_info_is_valid(location_with_letter_zip),
            (False, 'zip must be numeric'))
        self.assertEqual(
            location_info_is_valid(location_with_short_zip),
            (False, 'zip must be a 5-digit number'))


    def test_construct_url(self):
        '''
        function 'construct_url' should
            - API key:
                - check environment variables
                - prompt user
            - until location is valid:
                - call prompt_location_info
                - validate using 'location_info_is_valid'
                - validate user intention
            - latitude / longitude!
            - construct query string
            - return URL
        '''
        test_url = construct_url(
            zip_code='78727',
            api_key=API_KEY)
        self.assertEqual(
            test_url,
            'http://api.openweathermap.org/data/2.5/weather?' + 
            'lat=30.4254&lon=-97.7195&appid=' +
            '06de9d0d22fa2dff3a3ef81a85009c5e')


    def test_get_weather(self):
        '''
        function 'get_weather' should
            - API token?
            - call url
            - select attributes
            - convert attributes to human-readable?
            - print and return dict
        '''
        test_url = construct_url(
            zip_code='78727',
            api_key=API_KEY)
        test_data = get_weather(test_url)
        self.assertTrue(isinstance(test_data, dict))


print(pylint.epylint.py_run('project.py'))

USER_CONTINUE = True
while USER_CONTINUE:
    VALID_AND_INTENTIONAL_LOCATION = False
    LOCATION = None
    while not VALID_AND_INTENTIONAL_LOCATION:
        LOCATION = prompt_location_info()
        VALID_LOCATION = location_info_is_valid(LOCATION)
        if not VALID_LOCATION[0]:
            print(VALID_LOCATION[1])
        else:
            print('is this the LOCATION you want to check?')
            print(LOCATION)
            INTENTIONAL_LOCATION = input('yes or no: ')
            if INTENTIONAL_LOCATION in ('yes', 'y'):
                VALID_AND_INTENTIONAL_LOCATION = True


    WEATHER_URL = construct_url(LOCATION['zip'], API_KEY)
    
    print(WEATHER_URL)

    WEATHER_DATA = get_weather(WEATHER_URL)

    print(WEATHER_DATA)

    print('would you like to run the program again?')
    RUN_AGAIN = input('yes or no: ')
    if RUN_AGAIN in ('no', 'n'):
        USER_CONTINUE = False


if __name__ == '__main__':
    unittest.main()
    # command-line args?
else:
    unittest.main(module='project', exit=False)
