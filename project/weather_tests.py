'''
Test and lint weather module.
'''
import unittest
from unittest import mock
import pylint
import weather

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
            result = weather.prompt_location_info()
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
        self.assertTrue(weather.location_info_is_valid(good_location)[0])
        self.assertEqual(
            weather.location_info_is_valid(location_as_list),
            (False, 'location object must be a dict'))
        self.assertEqual(
            weather.location_info_is_valid(location_with_numeric_city),
            (False, 'city must be alphabetical'))
        self.assertEqual(
            weather.location_info_is_valid(location_with_numeric_state),
            (False, 'state must be alphabetical'))
        self.assertEqual(
            weather.location_info_is_valid(location_with_letter_zip),
            (False, 'zip must be numeric'))
        self.assertEqual(
            weather.location_info_is_valid(location_with_short_zip),
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
        test_url = weather.construct_url(
            zip_code='78727',
            api_key=weather.CIS245_KEY)
        self.assertEqual(
            test_url,
            'http://api.openweathermap.org/data/2.5/weather?' +
            'lat=30.4254&lon=-97.7195&appid=' +
            '3bf2254ec1d293cec6df10ab26d61f43')


    def test_get_weather(self):
        '''
        function 'get_weather' should
            - API token?
            - call url
            - select attributes
            - convert attributes to human-readable?
            - print and return dict
        '''
        test_url = weather.construct_url(
            zip_code='78727',
            api_key=weather.CIS245_KEY)
        test_data = weather.get_weather(test_url)
        self.assertTrue(isinstance(test_data, dict))

print(pylint.epylint.py_run('project.py'))

if __name__ == '__main__':
    unittest.main()
    # command-line args?
else:
    unittest.main(module='project', exit=False)
