Choose one of the questions below for their initial discussion posting.  A minimum of three responses to another peer’s posting is required. 

## 1) Discussion 1
**There are various software code management solutions available.  Each has its pros and cons.  Perform research for 3 different SCM tools.  What are the pros and cons of each?  Is there an associated cost?  Is one more popular than the other?  Imagine that you’re a software development manager, which would you choose and why?**

## 2) Discussion 2
**There are various tools for conducting peer reviews.  Perform research on peer review tools.  List several tools along with their pros and cons if any.  Is there a cost?  Imagine that you’re a software development manager, which would you choose and why?**
Peer review tools:
 - Merge Requests  
 - DevOps testing  
 - Embold  
 - 
### Unit Tests
Some of the many benefits of unit tests are,  
 - They describe the developer's intentions and lack thereof;  
 - They highlight which discussions need to be had in the review process;  
 - They defend the function from oversimplification and refactoring processes;  
 - They enable reviewers to step through code in debuggers;  
For example, consider the following function followed by unit tests:
```
import re
import unittest

def primary_colors_strings(my_input):
    '''return list of primary colors in string.'''
    result = []
    if re.search(re.compile('[Bb][Ll][Uu][Ee]'), my_input):
        result.append('blue')
    if re.search(re.compile('[Yy][Ee][Ll]{2,5}[Oo][Ww]'), my_input):
        result.append('yellow')
    if re.search(re.compile('[Rr][Ee][D]'), my_input):
        result.append('red')
    return result


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
        yellow_result_5 = primary_colors_strings('yelllllow')
        self.assertTrue('yellow' in yellow_result_5)

if __name__=='__main__':
    unittest.main()
else:
    unittest.main(module='primary_colors_strings', exit=False)
```
`def test_yellow_with_five_l` shows that it was the developer's intention that 'yelllllow' with five Ls counts as 'yellow'. `def test_red_lowercase` doesn't pass, which simultaneously shows that it's the developer's intention that `A_red_CDEF` be counted as red, and that the code currently fails to do so (pattern `[Rr][Ee][D]` matches red with uppercase D - it needs to change to `[Rr][Ee][Dd]` to match any-case).  

Rather than glancing at the function and saying, "that seems right," reviewers should ask, why should we count yelllllow as yellow? We do not count yelow as yellow or bluue as blue, what is it about 2-5 Ls that we trust so much when detecting yellow? The unit tests highlight the oddities of the function provide a discussion point in the review process.  

If `[Bb][Ll][Uu][Ee]` is changed to `blue`, `test_blue_rANdOmCasE` fails - unless `my_input` is changed to `my_input.lower()`. If `[Yy][Ee][Ll]{2,5}[Oo][Ww]` is changed to `yellow`, `test_yellow_with_five_l` fails regardless of whether `my_input` is set `.tolower()`.The unit tests defend the function from being oversimplified in the review and refactoring processes.

If the function were more complicated, for example if it called other functions which called other functions, the developers could set breakpoints in the function and reach them in a debugger using unit tests. This would give them an idea of how it was designed regardless of whether the tests are likely inputs or written comprehensively.

