# -*- coding: UTF-8 -*-

'''
Module
    test_icli_command.py
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
    Unit tests for ICLICommand interface.
'''

from __future__ import annotations

import unittest
from collections.abc import Mapping, Sequence
from typing import Any

from ats_utilities.option.command.command_option import CommandOption

from armpicom.service.iservice import IService
from armpicom.infrastructure.icli_command import ICLICommand

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.9.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class DummyCLICommand(ICLICommand):
    '''
        Dummy CLI Command implementation for testing ICLICommand.
    '''

    @property
    def name(self) -> str:
        return "dummy"

    @property
    def help_text(self) -> str:
        return "help"

    @property
    def options(self) -> Sequence[CommandOption]:
        return []

    def execute(self, *, params: Mapping[str, Any], service: IService) -> Mapping[str, Any]:
        return {"returncode": 0}

    def __str__(self) -> str:
        return "DummyCLICommand"


class TestICLICommand(unittest.TestCase):
    '''
        Defines ICLICommand interface unit tests.
    '''

    def test_icli_command_subclass(self) -> None:
        '''
            Tests that DummyCLICommand correctly implements ICLICommand.
        '''
        cmd = DummyCLICommand()
        self.assertEqual(cmd.name, "dummy")
        self.assertEqual(cmd.help_text, "help")
        self.assertEqual(cmd.options, [])
        self.assertEqual(str(cmd), "DummyCLICommand")
