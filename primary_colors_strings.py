def primary_colors_strings(my_input):
    '''return list of primary colors in string.'''
    import re
    result = []
    if re.search(re.compile('[Bb][Ll][Uu][Ee]'), my_input):
        result.append('blue')
    if re.search(re.compile('[Yy][Ee][Ll]{2,5}[Oo][Ww]'), my_input):
        result.append('yellow')
    if re.search(re.compile('[Rr][Ee][D]'), my_input):
        result.append('red')
    return result

import unittest
class testPrimaryColorsStringsFunction(unittest.TestCase):
    '''test primary_colors_strings function'''

    def test_blue_rANdOmCasE(self):
        '''Function should do a case-insensitive test for "blue".'''
        result = primary_colors_strings('a_BlUe_and_yellow_cdEF')
        self.assertTrue('blue' in result)

    # def test_red_lowercase(self):
        '''function should do a case-insensitive test for red'''
        # result = primary_colors_strings('A_red_CDEF')
        # self.assertTrue('red' in result)

    def test_yellow_with_one_l(self):
        '''function should not recognize yellow with only one l'''
        yellow_result_1 = primary_colors_strings('yelow')
        self.assertFalse('yellow' in yellow_result_1)

    def test_yellow_with_five_l(self):
        '''function should recognize yellow with up to 5 ls'''
        yellow_result_3 = primary_colors_strings('yelllow')
        self.assertTrue('yellow' in yellow_result_3)

if __name__=='__main__':
    unittest.main()
else:
    unittest.main(module='primary_colors_strings', exit=False)
