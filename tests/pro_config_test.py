# -*- coding: UTF-8 -*-

'''
Module
    pro_config_test.py
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
    Defines class ProConfigTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ProConfig.
Execute
    python3 -m unittest -v pro_config_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from armpicom.pro.config import ProConfig
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/armpicom'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.6.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProConfigTestCase(TestCase):
    '''
        Defines class ProConfigTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ProConfig.
        Project configuration unittests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | create - Default on create is not None.
                | create_with_none - Create None config.
                | create_empty - Create empty config.
                | test_is_config_ok - Test project config check.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_pro_config_default_create(self) -> None:
        '''Default on create is not None'''
        configuration = ProConfig()
        self.assertIsNotNone(configuration)

    def test_pro_config_is_config_ok(self) -> None:
        '''Is config ok'''
        configuration = ProConfig()
        configuration.config = {
            'base': 'none', 'extended': 'none', 'extra': 'none'
        }
        self.assertTrue(configuration.is_config_ok())

    def test_pro_config_is_config_not_none(self) -> None:
        '''Is config not None'''
        configuration = ProConfig()
        configuration.config = {
            'base': 'none', 'extended': 'none', 'extra': 'none'
        }
        self.assertTrue(bool(configuration.config))

    def test_pro_config_create_empty(self) -> None:
        '''Create Empty config'''
        configuration = ProConfig()
        configuration.config = {}
        self.assertFalse(bool(configuration.config))
        self.assertFalse(configuration.is_config_ok())

    def test_pro_config_create_with_none(self) -> None:
        '''Create None config'''
        configuration = ProConfig()
        with self.assertRaises(ATSTypeError):
            configuration.config = None


if __name__ == '__main__':
    main()
