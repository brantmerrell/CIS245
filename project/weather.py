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
import requests
import pgeocode


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


CIS245_KEY = '3bf2254ec1d293cec6df10ab26d61f43'
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
    WEATHER_URL = construct_url(LOCATION['zip'], CIS245_KEY)
    WEATHER_DATA = get_weather(WEATHER_URL)

    print(WEATHER_DATA)

    print('would you like to run the program again?')
    RUN_AGAIN = input('yes or no: ')
    if RUN_AGAIN in ('no', 'n'):
        USER_CONTINUE = False
