# -*- coding: UTF-8 -*-

'''
Module
    pro_name_test.py
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
    Defines class ProNameTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ProName.
Execute
    python3 -m unittest -v pro_name_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from armpicom.pro.config.pro_name import ProName
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/armpicom'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.5.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProNameTestCase(TestCase):
    '''
        Defines class ProNameTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ProName.
        It defines:

            :attributes:
                | pro - Project name object.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_is_pro_name_ok - test pro name check.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_is_pro_name_ok(self) -> None:
        '''Test pro name check.'''
        pro = ProName()
        pro.pro_name = 'simple_test'
        self.assertTrue(pro.is_pro_name_ok())


if __name__ == '__main__':
    main()
