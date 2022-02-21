'''
This week we will create a program that performs file processing activities.
Your program this week will use the OS library in order to validate that a directory exists before
creating a file in that directory. Your program will prompt the user for the directory they would
like to save the file in as well as the name of the file. The program should then prompt the user
for their name, address, and phone number. Your program will write this data to a comma separated
line in a file and store the file in the directory specified by the user.

Once the data has been written your program should read the file you just wrote to the file system
and display the file contents to the user for validation purposes.

Submit a link to your Github repository.
'''
import os
import csv
#from prettytable import PrettyTable

def prompt_filepath():
    '''prompt for and return filepath & filename'''
    dir_exists = False
    while not dir_exists:
        user_directory = input('please provide a (currently existing) directory: ')
        dir_exists = os.path.isdir(user_directory)
    user_file = input('please provide a file name: ')
    user_filepath = user_directory + '/' + user_file
    return user_filepath


def prompt_user_info():
    '''prompt for and return name, address, and phone number information'''
    user_information = {}
    user_information['name'] = input('please provide a name: ')
    user_information['address'] = input('please provide an address: ')
    user_information['phone'] = input('please provide a phone number: ')
    return user_information


def write_user_info(user_information, user_filepath):
    '''write csv user information to filepath (directory path + filename)'''
    connection_w = open(user_filepath, 'w')
    connection_w.write(user_information)
    connection_w.close()


def read_user_info(user_filepath):
    '''read csv information from filepath'''
    connection_r = open(user_filepath, 'r')
    print(connection_r.read())


def print_user_info(user_data):
    '''print use info as PrettyTable'''
    print(user_data)

#FILEPATH = prompt_filepath()
#USER_INFO = prompt_user_info()
#write_user_info(USER_INFO, FILEPATH)
#USER_INFO_2 = read_user_info(FILEPATH)
#print_user_info(USER_INFO_2)
