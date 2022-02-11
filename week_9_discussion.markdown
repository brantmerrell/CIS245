Choose one of the questions below for their initial discussion posting.  A minimum of three responses to another peer’s posting is required. 

## 1) Discussion 1
**There are various software code management solutions available.  Each has its pros and cons.  Perform research for 3 different SCM tools.  What are the pros and cons of each?  Is there an associated cost?  Is one more popular than the other?  Imagine that you’re a software development manager, which would you choose and why?**

## 2) Discussion 2
**There are various tools for conducting peer reviews.  Perform research on peer review tools.  List several tools along with their pros and cons if any.  Is there a cost?  Imagine that you’re a software development manager, which would you choose and why?**  
Peer review tools:

### Review Board
Review Board is a flexible code-review platform hosted online. It comes with a standard package of options including commenting, replying to comments, approving changes, tracking issues, and automated code review. It stands out for being lightweight and for its flexibility not only with Git, but also Mercurial and a handful of other version control systems.

### GitLab
GitLab is a DevOps-oriented git management platform. It allows teams to merge git branches into each other using "Merge Requests", in which reviewers can see a history of commits, pipelines, and changes within a branch before agreeing to merge it into the destination branch. It's designed for teams that use CI (Continuous Integration) and CD (Continuous Deployment) practices.  

Among other things, that means the branch being merged should be identical to its destination branch in every way except in the changes made intentionally by the branch's creator. In human language, that sounds obvious. However in practice, the branch being merged and the branch it is being merged into are often both being changed on a regular basis, so making them identical requires a `git rebase` (or something analogous for other version control systems - GitLab only supports Git). GitLab makes this expectation more possible by providing a "rebase" button.

As part of its DevOps emphasis, GitLab encourages development teams to automate the testing process on a regular basis, and is built to make this as easy as possible. GitLab can re-run tests on a git branch each time the branch is modified and block branches from being merged if they do not pass certain tests. 

### Continuous Integration (CI)
CI has come to mean several things. It began as a practice for merging all branches to the central branch on a frequent basis. It more broadly refers to a set of DevOps practices that include using test-driven development and automatically running tests when merging code. CI uses unit tests to make code review more coherent and efficient. In a CI-assisted code review, 
 - The developer's intentional and unintentional work is showcased by tests or the lack thereof;  
 - Oddities of the code are represented as concise tests;  
 - Code is defended from oversimplification in refactoring by tests;  
 - Reviewers are able to follow highly complicated work by stepping through tests in debug mode;  
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

