# import requests module
# To-Do: app ID
    # hard-code?
    # get automatically?
    # get interactively?

# step 1 prompt_user_info():
    # start w/ greeting
    # prompt for city
    # prompt for state
    # prompt for zip
    # save and exit for specified user-input?
    # if there is a user-message from step 2, display it
    # ask user if information is correct before proceeding to step 3

# step 2 evaluate_user_info(): evaluate whether info is valid and sufficient to construct query parameters
    # if so, proceed to step 2
    # if not, return to step 1 with message to user

# step 3 get_forecast(): send the query parameters to api.openweathermap.org/data/2.5/weather?q={city,state}|{zip}&{app_id}
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
    # validate_city(city, state) validates whether city / country exists. It's unclear what API / module to use at this time
    # format_temperature(temp, country): returns string of temperature in Fahrenheit or Celsius depending on country
    # format_pressure(pressure, country): returns string of pressure in inHg or mbar depending on country
    # format_direction(degrees): returns north, northeast, east, southeast, south, southwest, west, or northwest with degrees of imprecision leftover. ie. southeast + 3 degrees clockwise.
    # format_humidity(humid): converts humidity to a string of integer & percentage sign
    # format_speed(speed, country): string of integer with mph or mkh depending on country

# main() function: 
    # distinguish whether app is being called from the python repl or the command line.
    # if called from the command line, load any command-line arguments into step 1 before prompting user
