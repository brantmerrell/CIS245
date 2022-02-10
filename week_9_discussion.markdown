Choose one of the questions below for their initial discussion posting.  A minimum of three responses to another peer’s posting is required. 

## 1) Discussion 1
**There are various software code management solutions available.  Each has its pros and cons.  Perform research for 3 different SCM tools.  What are the pros and cons of each?  Is there an associated cost?  Is one more popular than the other?  Imagine that you’re a software development manager, which would you choose and why?**
Code management tools:
    - github
    - BitBucket
    - Mercurial
    - Monotone
    - CVS
    - SVN Subversion
    - TFS
    - Codacy
    - Veracode
## 2) Discussion 2
**There are various tools for conducting peer reviews.  Perform research on peer review tools.  List several tools along with their pros and cons if any.  Is there a cost?  Imagine that you’re a software development manager, which would you choose and why?**
Peer review tools:
    - Merge Requests
    - DevOps testing
    - Embold
    - 
### Unit Tests
The following code snippet contains a function followed by unit tests:
```
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
```
These unit tests help describe the primary developer's intentions (and lack thereof) to reviewers and to future developers.

For example, we can see in `def test_yellow_with_five_l` that it was the developer's intention that 'yelllllow' with five Ls counts as 'yellow'. This decision might not pass review, because it's a very random misspelling. After all, bluue with two Us doesn't count as blue, so why should 'yelllllow' with five Ls? The reviewers need to have this conversation before signing off on the work. Either way though, there is a unit test that waves its hand and says, "this is what this function does." 

On the flip side, I've commented out `def test_red_lowercase` because it doesn't pass. The reason it doesn't pass is that `primary_colors_strings('A_red_CDEF')` doesn't return 'red' in its return list. More specifically, `primary_colors_strings` uses the regex pattern `[Rr][Ee][D]` to look for red in the input string. [Rr] means R or r, [Ee] means E or e, [D] just means D. If `test_red_lowercase` is not present, it tells reviewers that using [D] instead of [Dd] is probably an accident. If it fails, it tells the developer to fix something. 

