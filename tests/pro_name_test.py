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
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from armpicom.pro.config.pro_name import ProName
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/armpicom'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.6.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProNameTestCase(TestCase):
    '''
        Defines class ProNameTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ProName.
        Project name unittests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_pro_name_default_create - Default on create is not None.
                | test_pro_name_is_config_ok - Is config ok.
                | test_pro_name_is_config_not_none - Is config not None.
                | test_pro_name_create_empty - Create Empty config.
                | test_pro_name_create_with_none - Create None config.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_pro_name_default_create(self) -> None:
        '''Default on create is not None'''
        configuration = ProName()
        self.assertIsNotNone(configuration)

    def test_pro_name_is_config_ok(self) -> None:
        '''Is config ok'''
        configuration = ProName()
        configuration.pro_name = 'app_example'
        self.assertTrue(configuration.is_pro_name_ok())

    def test_pro_name_is_config_not_none(self) -> None:
        '''Is config not None'''
        configuration = ProName()
        configuration.pro_name = 'app_example'
        self.assertTrue(bool(configuration.pro_name))

    def test_pro_name_create_empty(self) -> None:
        '''Create Empty config'''
        configuration = ProName()
        configuration.pro_name = ""
        self.assertFalse(bool(configuration.pro_name))
        self.assertFalse(configuration.is_pro_name_ok())

    def test_pro_name_create_with_none(self) -> None:
        '''Create None config'''
        configuration = ProName()
        with self.assertRaises(ATSTypeError):
            configuration.pro_name = None


if __name__ == '__main__':
    main()
