# -*- coding: UTF-8 -*-

'''
 Module
     test_pro_config.py
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
     Defined class ProConfigTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of ProConfig.
 Execute
     python3 -m unittest -v test_pro_config
'''

import sys
import unittest

try:
    from armpicom.pro.config import ProConfig
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


class ProConfigTestCase(unittest.TestCase):
    '''
        Defined class ProConfigTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ProConfig.
        It defines:

            :attributes:
                | configuration - Project config object.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_is_config_ok - test project config check.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.configuration = ProConfig()

    def tearDown(self):
        '''Call after test case.'''
        self.configuration = None

    def test_is_config_ok(self):
        '''Test project config check.'''
        self.configuration.config = {
            'base': 'none', 'extended': 'none', 'extra': 'none'
        }
        self.assertEqual(self.configuration.is_config_ok(), True)


if __name__ == '__main__':
    unittest.main()
