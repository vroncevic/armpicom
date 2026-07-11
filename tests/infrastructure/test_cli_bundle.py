# -*- coding: UTF-8 -*-

'''
Module
    test_cli_bundle.py
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
    Unit tests for CLIBundle.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock
from collections.abc import Sequence
from typing import Any, override

from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.option.command.command_option import CommandOption
from ats_utilities.option.ioption_manager import IOptionManager

from armpicom.service.iservice import IService
from armpicom.infrastructure.icli_command import ICLICommand
from armpicom.infrastructure.cli_bundle import CLIBundle

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
        Dummy CLI command for testing CLIBundle.
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


class TestCLIBundle(unittest.TestCase):
    '''
        Defines CLIBundle unit tests.
    '''

    def test_cli_bundle_validation(self) -> None:
        '''
            Tests validation checks of CLIBundle.
        '''
        # All None
        bundle = CLIBundle(service=None, parser=None, commands=None)
        with self.assertRaises(ATSValueError) as ctx:
            bundle.validate()
        self.assertEqual(str(ctx.exception), 'clibundle::validate - service must be provided')

        # parser None
        bundle_partial1 = CLIBundle(service=MagicMock(spec=IService), parser=None, commands=None)
        with self.assertRaises(ATSValueError) as ctx:
            bundle_partial1.validate()
        self.assertEqual(str(ctx.exception), 'clibundle::validate - parser must be provided')

        # commands None
        bundle_partial2 = CLIBundle(
            service=MagicMock(spec=IService), parser=MagicMock(spec=IOptionManager), commands=None
        )
        with self.assertRaises(ATSValueError) as ctx:
            bundle_partial2.validate()
        self.assertEqual(str(ctx.exception), 'clibundle::validate - commands sequence must be provided')

        # Type errors
        bundle_type1 = CLIBundle(
            service="invalid_service",  # type: ignore
            parser=MagicMock(spec=IOptionManager),
            commands=[DummyCommand()]
        )
        with self.assertRaises(ATSTypeError) as ctx:
            bundle_type1.validate()
        self.assertEqual(str(ctx.exception), 'clibundle::validate - service must be of type IService')

        bundle_type2 = CLIBundle(
            service=MagicMock(spec=IService),
            parser="invalid_parser",  # type: ignore
            commands=[DummyCommand()]
        )
        with self.assertRaises(ATSTypeError) as ctx:
            bundle_type2.validate()
        self.assertEqual(str(ctx.exception), 'clibundle::validate - parser must be of type IOptionManager')

        bundle_type3 = CLIBundle(
            service=MagicMock(spec=IService),
            parser=MagicMock(spec=IOptionManager),
            commands=123  # type: ignore
        )
        with self.assertRaises(ATSTypeError) as ctx:
            bundle_type3.validate()
        self.assertEqual(str(ctx.exception), 'clibundle::validate - commands must be of type Sequence')

        # Valid bundle validation should not raise error
        bundle_valid = CLIBundle(
            service=MagicMock(spec=IService),
            parser=MagicMock(spec=IOptionManager),
            commands=[DummyCommand()]
        )
        bundle_valid.validate()

    def test_cli_bundle_helpers(self) -> None:
        '''
            Tests CLIBundle helper methods (merge, to_dict).
        '''
        mock_service = MagicMock(spec=IService)
        mock_parser = MagicMock(spec=IOptionManager)
        cmd = DummyCommand()

        bundle1 = CLIBundle(service=mock_service, parser=None, commands=None)
        bundle2 = CLIBundle(service=None, parser=mock_parser, commands=[cmd])
        bundle1.merge(bundle2)

        self.assertEqual(bundle1.service, mock_service)
        self.assertEqual(bundle1.parser, mock_parser)
        self.assertEqual(bundle1.commands, [cmd])

        d = bundle1.to_dict()
        self.assertEqual(d["service"], mock_service)
        self.assertEqual(d["parser"], mock_parser)
        self.assertEqual(len(d["commands"]), 1)
        self.assertEqual(d["commands"][0].name, cmd.name)

    def test_cli_bundle_merge_invalid_type(self) -> None:
        '''
            Tests CLIBundle merge raises error when other is not CLIBundle.
        '''
        bundle = CLIBundle()
        with self.assertRaises(ATSTypeError) as ctx:
            bundle.merge("not_a_bundle")  # type: ignore
        self.assertEqual(str(ctx.exception), 'clibundle::merge - other must be of type CLIBundle')
