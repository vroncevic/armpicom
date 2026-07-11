# -*- coding: UTF-8 -*-

'''
Module
    test_icli.py
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
    Unit tests for ICLI interface.
'''

from __future__ import annotations

import unittest
from collections.abc import Mapping
from typing import Any

from armpicom.infrastructure.icli import ICLI

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.9.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class DummyCLI(ICLI):
    '''
        Dummy CLI implementation for testing ICLI.
    '''

    def run(self) -> Mapping[str, Any]:
        return {"returncode": 0}

    def is_initialized(self) -> bool:
        return True

    def __str__(self) -> str:
        return "DummyCLI"


class TestICLI(unittest.TestCase):
    '''
        Defines ICLI interface unit tests.
    '''

    def test_icli_subclass(self) -> None:
        '''
            Tests that DummyCLI correctly implements ICLI.
        '''
        cli = DummyCLI()
        self.assertTrue(cli.is_initialized())
        self.assertEqual(cli.run(), {"returncode": 0})
        self.assertEqual(str(cli), "DummyCLI")
