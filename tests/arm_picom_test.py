# -*- coding: UTF-8 -*-

'''
Module
    arm_picom_test.py
Copyright
    Copyright (C) 2022-2025 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class ArmPICOMTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ArmPICOM.
Execute
    python3 -m unittest -v arm_picom_test
'''

import sys
from typing import List
from os import makedirs
from unittest import TestCase, main

try:
    from armpicom import ArmPICOM
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2025, https://vroncevic.github.io/armpicom'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__: str = '1.9.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ArmPICOMTestCase(TestCase):
    '''
        Defines class ArmPICOMTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ArmPICOM.
        ArmPICOM unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create (not None).
                | test_missing_args - Test missing args.
                | test_wrong_arg - Test wrong arg.
                | test_process - Generate project structure.
                | test_pro_already_exists - Test pro already exists.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default on create (not None)'''
        generator: ArmPICOM = ArmPICOM()
        self.assertIsNotNone(generator)

    def test_missing_args(self) -> None:
        '''Test missing args'''
        sys.argv.clear()
        generator: ArmPICOM = ArmPICOM()
        self.assertFalse(generator.process())

    def test_wrong_arg(self) -> None:
        '''Test wrong arg'''
        sys.argv.clear()
        sys.argv.insert(0, '-d')
        sys.argv.insert(1, 'wrong_pro')
        generator: ArmPICOM = ArmPICOM()
        self.assertFalse(generator.process())

    def test_process(self) -> None:
        '''Generate project structure'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'latest_pro')
        generator: ArmPICOM = ArmPICOM()
        self.assertTrue(generator.process())

    def test_pro_already_exists(self) -> None:
        '''Test pro already exists'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'fresh_new')
        generator: ArmPICOM = ArmPICOM()
        makedirs('fresh_new')
        self.assertFalse(generator.process())


if __name__ == '__main__':
    main()
