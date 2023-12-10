# -*- coding: UTF-8 -*-

'''
Module
    template_dir_test.py
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
    Defines class TemplateDirTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of TemplateDir.
Execute
    python3 -m unittest -v template_dir_test
'''

import sys
from typing import List
from unittest import TestCase, main
from os.path import dirname, realpath

try:
    from armpicom.pro.config.template_dir import TemplateDir
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


class TemplateDirTestCase(TestCase):
    '''
        Defines class TemplateDirTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of TemplateDir.
        It defines:

            :attributes:
                | template - Template dir object.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_is_template_dir_ok - test template dir check.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_is_template_dir_ok(self) -> None:
        '''Test template dir check.'''
        template = TemplateDir()
        current_dir: str = dirname(realpath(__file__))
        template.template_dir = f'{current_dir}/../armpicom/conf/template/'
        self.assertTrue(template.is_template_dir_ok())


if __name__ == '__main__':
    main()
