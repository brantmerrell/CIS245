'''
project to get and print weather data from
https://openweathermap.org/current#data

Feedback from pseudocode draft:
 - lack of input validation to make sure a zipcode is a zipcode or a city name is alphabetical.
 - pass units=imperial|other into query string and let webservice do conversion work.
'''

import unittest
from unittest import mock
#import requests
import pylint
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
    print('please enter city, state, and zip:')
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




# evaluate whether info is valid and sufficient to construct query parameters
def construct_url():
    return None
    # if so, proceed to step 2
    # if not, return to step 1 with message to user
# step 3 get_forecast(): send the query parameters to
    # units = imperial|metric|other
    # api.openweathermap.org/data/2.5/weather?q={city,state}|{zip}&{app_id}
    # inform user if connection was successful
    # print any messages (error or otherwise) from the response

# step 4 format_forecast(): format response data for user-readability
    # parse from json or xml to dict object data
    # report = {}
    # report[temp] = format_temperature(main[temp], sys[sys.country])
    # report[feels_like] = format_temperature(main.feels_like, sys[sys.country])
    # report[temp_range[0]] = format_temperature(main.temp_min, sys[sys.country])
    # report[temp_range[1]] = format_temperature(main.temp_max, sys[sys.country])
    # report[pressure] = format_pressure(main.pressure, sys[sys.country])
    # report[humidity] = format_humidity(main.humidity)
    # report[wind_speed] = format_speed(wind.speed, sys[sys.country])
    # report[wind_direction] = format_direction(wind.direction):

# step 5: return / print weather forecast:
    # return report object constructed in step 4
    # offer to re-run

# helper functions (omit functionalities already provided by the openweather endpoint):
    # validate_city(city, state) validates whether city / country exists. What API module?
    # format_direction(degrees): north, northeast, east, etc... + R
    # format_humidity(humid): converts humidity to a string of integer & percentage sign
    # format_speed(speed, country): string of integer with mph or mkh depending on country

# main() function:
    # distinguish whether app is being called from the python repl or the command line.


class TestProject(unittest.TestCase):
    '''
    class for all unit tests of this project:
        - test_prompt_location_info
        - test_location_info_is_valid
        - test_construct_url
    '''


    def test_prompt_location_info(self):
        '''
        function "prompt_location_info" should
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
            function "location_info_is_valid" should
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
            - until location is valid:
                - call prompt_location_info
                - validate using 'location_info_is_valid'
                - validate user intention
            - construct query string
            - return URL
        '''
        return None


    def test_get_weather(self):
        '''
        function 'get_weather' should
            - API token?
            - call url
            - return request as dict
        '''
        return None

    def test_display_weather(self):
        '''
        function 'display weather' should
            - select attributes
            - convert dates to human-readable?
            - other human-readable?
            - print and return table
        '''
        return None


print(pylint.epylint.py_run('project.py'))

if __name__ == '__main__':
    unittest.main()
    # command-line args?
else:
    unittest.main(module='primary_colors_strings', exit=False)
