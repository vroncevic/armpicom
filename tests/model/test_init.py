# -*- coding: UTF-8 -*-

'''
Module
    test_init.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Unit tests for model initialization module.
'''

from __future__ import annotations

import unittest
import armpicom.model

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.9.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class TestModelInit(unittest.TestCase):
    '''
        Defines model package initialization unit tests.
    '''

    def test_metadata(self) -> None:
        '''
            Tests that model package metadata attributes are set correctly.
        '''
        self.assertEqual(armpicom.model.__author__, 'Vladimir Roncevic')
        self.assertEqual(armpicom.model.__copyright__, '(C) 2026, https://vroncevic.github.io/armpicom')
        self.assertEqual(armpicom.model.__credits__, ['Vladimir Roncevic', 'Python Software Foundation'])
        self.assertEqual(armpicom.model.__license__, 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE')
        self.assertEqual(armpicom.model.__version__, '1.9.6')
        self.assertEqual(armpicom.model.__maintainer__, 'Vladimir Roncevic')
        self.assertEqual(armpicom.model.__email__, 'elektron.ronca@gmail.com')
        self.assertEqual(armpicom.model.__status__, 'Development')
