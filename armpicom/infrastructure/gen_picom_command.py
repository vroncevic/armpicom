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

from typing import Any, override
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.option.command_option import CommandOption
from armpicom.infrastructure.icli_command import ICLICommand
from armpicom.domain.ports.iservice import IService

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/armpicom'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__: str = '1.9.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class GenPicomCommand(ICLICommand):
    '''
        CLI subcommand for generating picom configuration files.

        It defines:

            :attributes: None.
            :methods:
                | name - Returns the command name key.
                | help_text - Returns the command help text.
                | options - Returns the list of command options.
                | execute - Executes the subcommand.
                | __str__ - Returns the GenPicomCommand as string representation.
    '''

    @property
    @override
    def name(self) -> str:
        '''
            Returns the command name key.

            :return: The command name key.
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
    def options(self) -> list[CommandOption]:
        '''
            Returns the command options.

            :return: List of command options.
            :rtype: <list[CommandOption]>
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
    def execute(self, params: dict[str, Any], service: IService) -> dict[str, Any]:
        '''
            Executes the subcommand.

            :param params: Subcommand parameters from CLI parser.
            :type params: <dict[str, Any]>
            :param service: Command orchestrator service instance.
            :type service: <IService>
            :return: The result of the subcommand execution.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return service.execute(params=params)

    @override
    def __str__(self) -> str:
        '''
            Returns the GenPicomCommand as string representation.

            :return: The GenPicomCommand as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
