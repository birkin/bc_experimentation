# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
Sample testing code.
To run:
    cd into the `CLPS1950_python/basic/` directory
    type `python ./test.py`
"""

import logging, unittest


class WordcountTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_sum(self):
        import wordcount
        expected = 7
        self.assertEqual(
            expected,
            wordcount.sample_sum(3, 4) )

        """
        (clps1950_bc) bbox-2015$ python ./test.py
        F
        ======================================================================
        FAIL: test_sum (__main__.WordcountTest)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
          File "./test.py", line 18, in test_sum
            wordcount.sample_sum(3, 4) )
        AssertionError: 7 != 5

        ----------------------------------------------------------------------
        Ran 1 test in 0.001s

        FAILED (failures=1)
        """

    ## end class WordcountTest()



if __name__ == '__main__':
    unittest.main()
