# -*- coding: UTF-8 -*-

'''
 Module
     test_pro_name.py
 Copyright
     Copyright (C) 2022 Vladimir Roncevic <elektron.ronca@gmail.com>
     armpicom is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     armpicom is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined class ProNameTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of ProName.
 Execute
     python3 -m unittest -v test_pro_name
'''

import sys
import unittest

try:
    from armpicom.pro.config.pro_name import ProName
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/armpicom'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.5.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProNameTestCase(unittest.TestCase):
    '''
        Defined class ProNameTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ProName.
        It defines:

            :attributes:
                | pro - Project name object.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_is_pro_name_ok - test pro name check.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.pro = ProName()

    def tearDown(self):
        '''Call after test case.'''
        self.pro = None

    def test_is_pro_name_ok(self):
        '''Test pro name check.'''
        self.pro.pro_name = 'simple_test'
        self.assertEqual(self.pro.is_pro_name_ok(), True)


if __name__ == '__main__':
    unittest.main()
