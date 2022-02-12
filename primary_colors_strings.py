'''module to learn how the unittest and pylint modules work'''

import re
import unittest
from unittest import mock
import pylint

def primary_colors_strings(my_input=None):
    '''return list of primary colors in string.'''
    if my_input is None:
        my_input = input('input string: ')
    result = []
    if re.search(re.compile('[Bb][Ll][Uu][Ee]'), my_input):
        result.append('blue')
    if re.search(re.compile('[Yy][Ee][Ll]{2,5}[Oo][Ww]'), my_input):
        result.append('yellow')
    if re.search(re.compile('[Rr][Ee][Dd]'), my_input):
        result.append('red')
    return result

def two_inputs():
    '''function to learn how to mock 2 inputs during testing'''
    input_1 = input('input_1: ')
    input_2 = input('input_2: ')
    return (input_1, input_2)


class TestPrimaryColorsStringsFunction(unittest.TestCase):
    '''test primary_colors_strings function'''

    def test_blue_randomcase(self):
        '''Function should do a case-insensitive test for "blue".'''
        result = primary_colors_strings('a_BlUe_and_yellow_cdEF')
        self.assertTrue('blue' in result)

    def test_red_lowercase(self):
        '''function should do a case-insensitive test for red'''
        result = primary_colors_strings('A_red_CDEF')
        self.assertTrue('red' in result)

    def test_yellow_with_one_l(self):
        '''function should not recognize yellow with only one l'''
        yellow_result_1 = primary_colors_strings('yelow')
        self.assertFalse('yellow' in yellow_result_1)

    def test_yellow_with_five_l(self):
        '''function should recognize yellow with up to 5 ls'''
        yellow_result_5 = primary_colors_strings('yelllllow')
        self.assertTrue('yellow' in yellow_result_5)

    def test_interactive_single(self):
        '''how can a unit test pass a value into an interactive function?'''
        unittest.mock.builtins.input = lambda _: "blueyellow"
        self.assertTrue('blue' in primary_colors_strings())

    def test_two_inputs(self):
        '''how can a unit test test pass multiple values into an interactive function?'''
        mock_args = ['foo', 'bar']
        with mock.patch('builtins.input') as mocked_input:
            mocked_input.side_effect = mock_args
            result = two_inputs()
        self.assertTrue('foo' in result)
        self.assertTrue('bar' in result)


print(pylint.epylint.py_run('primary_colors_strings.py'))


if __name__ == '__main__':
    unittest.main()
else:
    unittest.main(module='primary_colors_strings', exit=False)
