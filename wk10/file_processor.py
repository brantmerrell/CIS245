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
import shutil
import unittest
from unittest import mock
import pylint
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


class TestFileProcessor(unittest.TestCase):
    '''test functions in file_processor'''
    def setUp(self):
        if os.path.exists('dumydir'):
            shutil.rmtree('dumydir')
        os.mkdir('dumydir')
        os.mkdir('dumydir/subdumydir')


    def tearDown(self):
        shutil.rmtree('dumydir')


    def test_prompt_filepath(self):
        '''
        prompt_filepath should:
            prompt for dir until input dir exists
            prompt for filename (no adding dirs)
            return combined dir & filename
        '''
        dir_prompts_with_one_fake_dir = [
            'dumydir/fakedir',
            'dumydir/subdumydir',
            'my_file.csv'
            ]
        with mock.patch('builtins.input') as mocked_input:
            mocked_input.side_effect = dir_prompts_with_one_fake_dir
            result = prompt_filepath()
        self.assertEqual(
            result,
            'dumydir/subdumydir/my_file.csv'
            )

    def test_prompt_user_info(self):
        '''
        prompt_user_info:
            prompts for name, address, phone number
            validation:
                name is alphabetical
                address has 1+ letter and 1+ number
                phone number consists of 10+ numbers 0-5 of '()-.'
            return object is a dictionary with keys name, address, phone
        '''
        user_prompt_info_sequence = [
            'John 3 Doe', # name: numers invalid
            'John Doe', # name: valid
            '', # address: not enough characters
            'foo', # address: not enough numbers
            '123', # address: not enough letters
            'a1', # address: minimum valid example
            '(1)2-3.45', # phone: not enough numbers
            '[1]123.456(78-9)' # phone: invalid brackets
            '(1)123.456(78-9)' # phone: valid example
            ]
        with mock.patch('builtins.input') as mocked_input:
            mocked_input.side_effect = user_prompt_info_sequence
            result = prompt_user_info()
        self.assertEqual(
            result,
            {
                'name': 'John Doe',
                'address': 'a1',
                'phone': '(1)123,456(78-9)'
            }
        )




print(pylint.epylint.py_run('file_processor.py'))

if __name__ == '__main__':
    unittest.main()
else:
    unittest.main(module='file_processor', exit=False)
