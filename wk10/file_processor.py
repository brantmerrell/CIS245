'''
File Processor:
    - prompts user for directory & filename
    - validates directory existence
    - prompts for name, address, phone number
    - creates file with csv information
    - reads file
    - displays file contents to user

Submit a link to your Github repository.

ToDo / wishlist:
    - interactively build filepath (outside assignment scope)
'''
import os
import re
import pandas
#import unittest
#from unittest import mock

print([x for x in dir(os.path) if re.search('is', x)])

def prompt_for_directory():
    return input('please provide an input directory: ')


def prompt_for_file():
    return input('please provide an input file: ')


def directory_exists(input_directory):
    if os.path.isdir(input_directory):
        return (True, 'directory exists')
    elif os.path.isfile(input_directory):
        return (False, input_directory + ' is a file')
    elif os.path.exists(input_directory):
        return (False, input_directory + 
                ' is something other than a file or directory')
    else:
        return (False, input_directory + ' does not exist')
        

def mkdir(input_directory):
    try:
        os.path.makedirs(input_directory)
        return True
    except:
        return False


def prompt_user_info():
    name=input('name: ')
    address=input('address: ')
    phone_number=input('phone number: ')
    return {
        'name': name,
        'address': address,
        'phone_number': phone_number
        }


#def write_user_info():
#def read_user_info():

#if __name__ == '__main__':
#    unittest.main()
#else:
#    unittest.main(module='file_processor', exit=False)
