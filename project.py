'''project to get and print weather data.'''

import re
import requests
import unittest
from unittest import mock
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
    errors = ''
    if type(location) is not dict:
        return( (False, 'location object must be a dict') )
    for attribute in ['city','state','zip']:
        if attribute not in location.keys():
            return( (False, 'location dict must contain city, state, and zip keys') )
        if type(location[attribute]) is not str:
            return( (False, f'location object {attribute} must be a string') )
    if not location['zip'].isnumeric():
        return ( (False, 'zip must be numeric') )
    if location['zip'].count('') != 6:
        return ( (False, 'zip must be a 5-digit number') )
    if not location['city'].isalpha():
        return ( (False, 'city must be alphabetical') )
    if not location['state'].isalpha():
        return ( (False, 'state must be alphabetical') )
    return (True, 'no errors detected')




# evaluate whether info is valid and sufficient to construct query parameters
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


class testProject(unittest.TestCase):
    def test_hello_world(self):
        '''Ascertain that nothing breaks on run'''
        self.assertTrue(True)

    def test_prompt_location_info(self):
        mock_args = ['Austin', 'TX', '78727']
        with mock.patch('builtins.input') as mocked_input:
            mocked_input.side_effect = mock_args
            result = prompt_location_info()
        self.assertEqual(result['city'], 'Austin')
        self.assertEqual(result['state'], 'TX')
        self.assertEqual(result['zip'], '78727')

    def test_location_info_is_valid__zip(self):
        good_zip_location = {
            'city': 'Austin',
            'state': 'TX',
            'zip': '78727'
            }
        bad_zip_location = {
            'city': 'Austin',
            'state': 'TX',
            'zip': '787d7'
            }
        print(location_info_is_valid(good_zip_location))
        self.assertTrue(location_info_is_valid(good_zip_location)[0])
        self.assertFalse(location_info_is_valid(bad_zip_location)[0])

print(pylint.epylint.py_run('project.py'))

if __name__=='__main__':
    unittest.main()
    # command-line args?
else:
    unittest.main(module='primary_colors_strings', exit=False)


'''
Feedback from pseudocode draft:
Great work on your flow chart. I've attached it here just for record keeping purposes.

My only comments on your flow chart concern the lack of input validation to make sure a zipcode is a zipcode or a city name is alphabetical -- or whatever you determine to be valid string input for the city name.

Also, less of a problem, more of a tip, you seem to have invested a bunch of effort in converting units and formatting data in your flow chart.

If you review the API documentation you will see that you can pass units=imperial into your query string and the web service will provide the data in imperial (or whatever other unit of measure the API accepts).

https://openweathermap.org/current#data
'''
