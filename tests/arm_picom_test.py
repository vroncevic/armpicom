# -*- coding: UTF-8 -*-

'''
Module
    arm_picom_test.py
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
    Defines class GenPICOMTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ArmPICOM.
Execute
    python3 -m unittest -v arm_picom_test
'''

import sys
from typing import List
from os import makedirs, rmdir
from unittest import TestCase, main

try:
    from armpicom import ArmPICOM
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


class GenPICOMTestCase(TestCase):
    '''
        Defines class GenPICOMTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ArmPICOM.
        Project generation unittests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create is not None.
                | test_missing_args - Missing args.
                | test_process - Generate project.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default on create is not None'''
        generator: ArmPICOM = ArmPICOM()
        self.assertIsNotNone(generator)

    def test_missing_args(self) -> None:
        '''Missing args'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_armpicom_run.py')
        generator: ArmPICOM = ArmPICOM()
        self.assertFalse(generator.process())

    def test_wrong_arg(self) -> None:
        '''Generate project'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_armpicom_run.py')
        sys.argv.insert(2, '-d')
        sys.argv.insert(3, 'wrong')
        generator: ArmPICOM = ArmPICOM()
        self.assertFalse(generator.process())

    def test_process(self) -> None:
        '''Generate project'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_armpicom_run.py')
        sys.argv.insert(2, '-g')
        sys.argv.insert(3, 'latest')
        generator: ArmPICOM = ArmPICOM()
        self.assertTrue(generator.process())

    def test_tool_not_operational(self) -> None:
        '''Generate project'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_armpicom_run.py')
        sys.argv.insert(2, '-g')
        sys.argv.insert(3, 'fresh')
        generator: ArmPICOM = ArmPICOM()
        generator.tool_operational = False
        self.assertFalse(generator.process())

    def test_pro_already_exists(self) -> None:
        '''Generate project'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_armpicom_run.py')
        sys.argv.insert(2, '-g')
        sys.argv.insert(3, 'fresh_new')
        generator: ArmPICOM = ArmPICOM()
        makedirs('fresh_new')
        self.assertFalse(generator.process())
        rmdir('fresh_new')


if __name__ == '__main__':
    main()
