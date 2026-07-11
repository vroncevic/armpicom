# -*- coding: UTF-8 -*-

'''
Module
    test_cli.py
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
    Unit tests for CLI adapter.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock
from typing import Any, override

from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.option.command.command_option import CommandOption
from ats_utilities.option.ioption_manager import IOptionManager

from armpicom.service.iservice import IService
from armpicom.infrastructure.icli_command import ICLICommand
from armpicom.infrastructure.cli_bundle import CLIBundle
from armpicom.infrastructure.cli import CLI

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.9.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class DummyCommand(ICLICommand):
    '''
        Dummy CLI command for testing CLI.
    '''

    @property
    @override
    def name(self) -> str:
        return "dummy"

    @property
    @override
    def help_text(self) -> str:
        return "Dummy command for tests"

    @property
    @override
    def options(self) -> list[CommandOption]:
        return []

    @override
    def execute(self, *, params: dict[str, Any], service: IService) -> dict[str, Any]:
        return {"returncode": 0, "stdout": "dummy executed"}

    @override
    def __str__(self) -> str:
        return f"DummyCommand(name='{self.name}', help_text='{self.help_text}')"


class TestCLI(unittest.TestCase):
    '''
        Defines CLI adapter unit tests.
    '''

    def test_cli_init_missing_bundle(self) -> None:
        '''
            Tests CLI initialization raises ValueError when bundle is None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            CLI(None)  # type: ignore
        self.assertEqual(str(ctx.exception), 'cli::__init__ - component bundle (CLIBundle) must be provided')

    def test_cli_run_executes_command(self) -> None:
        '''
            Tests that CLI.run parses arguments and delegates execution to the matched command.
        '''
        mock_service: MagicMock = MagicMock(spec=IService)
        mock_parser: MagicMock = MagicMock(spec=IOptionManager)
        mock_command: DummyCommand = DummyCommand()

        mock_parser.parse_command.return_value = ("dummy", {"req": "val", "foo": "baz"})

        cli_bundle: CLIBundle = CLIBundle(service=mock_service, parser=mock_parser, commands=[mock_command])
        cli: CLI = CLI(cli_bundle)
        
        self.assertTrue(cli.is_initialized())
        
        res = cli.run()

        mock_parser.parse_command.assert_called_once()
        self.assertEqual(res, {"returncode": 0, "stdout": "dummy executed"})

        self.assertIsNotNone(str(cli))

    def test_cli_run_unknown_command(self) -> None:
        '''
            Tests CLI behavior when parser returns an unknown command.
        '''
        mock_service: MagicMock = MagicMock(spec=IService)
        mock_parser: MagicMock = MagicMock(spec=IOptionManager)

        mock_parser.parse_command.return_value = ("unknown", {})

        cli_bundle: CLIBundle = CLIBundle(service=mock_service, parser=mock_parser, commands=[])
        cli: CLI = CLI(cli_bundle)
        res = cli.run()

        self.assertEqual(res.get("return_code"), -1)
        self.assertEqual(res.get("stderr"), ["Unknown command"])
