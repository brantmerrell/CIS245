'''tests for file_processor'''
import os
import shutil
import unittest
from unittest import mock
import pylint
import file_processor as fp

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
            result = fp.prompt_filepath()
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
        user_prompt_info_basic = [
            'John Doe',
            '1545 foo street',
            '(123)456-7890']
        with mock.patch('builtins.input') as mocked_input:
            mocked_input.side_effect = user_prompt_info_basic
            result = fp.prompt_user_info()
        self.assertEqual(
            result,
            {
                'name': 'John Doe',
                'address': '1545 foo street',
                'phone': '(123)456-7890'
            }
        )




print(pylint.epylint.py_run('file_processor.py'))
print(pylint.epylint.py_run('file_processor_tests.py'))

if __name__ == '__main__':
    unittest.main()
else:
    unittest.main(module='file_processor', exit=False)
