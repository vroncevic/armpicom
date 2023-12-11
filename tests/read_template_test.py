# -*- coding: UTF-8 -*-

'''
Module
    read_template_test.py
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
    Defines class ReadTemplateTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ReadTemplate.
Execute
    python3 -m unittest -v read_template_test
'''

import sys
from typing import Any, List, Dict
from os.path import dirname, realpath
from unittest import TestCase, main

try:
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from armpicom.pro.read_template import ReadTemplate
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


class ReadTemplateTestCase(TestCase):
    '''
        Defines class ReadTemplateTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ReadTemplate.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_read_template_create - Test read template create.
                | test_read_template_empty - Test read template empty.
                | test_read_template_none - Test read template None.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_read_template_create(self) -> None:
        '''Test read template create'''
        template = ReadTemplate()
        self.assertIsNotNone(template)

    def test_read_template_empty(self) -> None:
        '''Test read template empty'''
        template = ReadTemplate()
        templates: Dict[Any, Any] = {}
        with self.assertRaises(ATSValueError):
            self.assertFalse(
                template.read(templates)
            )

    def test_read_template_none(self) -> None:
        '''Test read template None'''
        template = ReadTemplate()
        with self.assertRaises(ATSTypeError):
            self.assertFalse(
                template.read(None)  # type: ignore
            )

    def test_read_template(self) -> None:
        '''Test read template'''
        current_dir: str = dirname(realpath(__file__))
        pro: str = '/../armpicom/conf/project.yaml'
        template = ReadTemplate()
        yml2obj = Yaml2Object(f'{current_dir}{pro}')
        self.assertTrue(bool(template.read(yml2obj.read_configuration())))


if __name__ == '__main__':
    main()