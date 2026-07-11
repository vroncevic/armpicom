# -*- coding: UTF-8 -*-

'''
Module
    gen_picom_command.py
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
    Defines GenPicomCommand class implementing ICLICommand strategy.
'''

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, override

from ats_utilities.factory_class import to_str
from ats_utilities.option.command.command_option import CommandOption

from armpicom.infrastructure.icli_command import ICLICommand
from armpicom.service.iservice import IService

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = r'1.9.6'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class GenPicomCommand(ICLICommand):
    '''
        CLI subcommand for generating picom configuration files.

        It defines:

            :attributes: None.
            :methods:
                | name - Returns the command name.
                | help_text - Returns the command help text.
                | options - Returns the list of command options.
                | execute - Executes the subcommand.
                | __str__ - Returns the GenPicomCommand as string representation.
    '''

    @property
    @override
    def name(self) -> str:
        '''
            Returns the command name.

            :return: The command name.
            :rtype: <str>
            :exceptions: None.
        '''
        return "create"

    @property
    @override
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: The command help text.
            :rtype: <str>
            :exceptions: None.
        '''
        return "Generate picom project files"

    @property
    @override
    def options(self) -> Sequence[CommandOption]:
        '''
            Returns the command options.

            :return: Sequence of command options.
            :rtype: <Sequence[CommandOption]>
            :exceptions: None.
        '''
        return [
            CommandOption(
                name="--name",
                help_text="Picom project name",
                default="mytool",
                required=True
            ),
            CommandOption(
                name="--output",
                help_text="Path to the output directory",
                default="./",
                required=True
            )
        ]

    @override
    def execute(self, *, params: Mapping[str, Any], service: IService) -> Mapping[str, Any]:
        '''
            Executes the subcommand.

            :param params: Subcommand parameters from CLI parser.
            :type params: <Mapping[str, Any]>
            :param service: Command orchestrator service instance.
            :type service: <IService>
            :return: The result of the subcommand execution.
            :rtype: <Mapping[str, Any]>
            :exceptions:
                | ValueError: Parameters mapping must be provided.
                | TypeError: Parameters mapping must be a mapping.
                | ATSTypeError: If parameters are of invalid type.
                | ATSValueError: If parameter constraints are violated.
                | ATSGeneratorError: If archive parsing or template rendering fails.
        '''
        return service.execute(params=params) if service.is_initialized() else {
            "return_code": -1, "stdout": [], "stderr": ["Service not initialized"]
        }

    @override
    def __str__(self) -> str:
        '''
            Returns the GenPicomCommand as string representation.

            :return: The GenPicomCommand as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
