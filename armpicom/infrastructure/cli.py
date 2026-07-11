# -*- coding: UTF-8 -*-

'''
Module
    cli.py
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
    Defines CLI class implementing inbound CLI port.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, override

from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.factory_class import to_str
from ats_utilities.factory_value import require_not_none

from armpicom.infrastructure.icli import ICLI
from armpicom.infrastructure.cli_bundle import CLIBundle
from armpicom.service.iservice import IService
from armpicom.infrastructure.icli_command import ICLICommand

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = r'1.9.6'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CLI(ICLI):
    '''
        Adapter that implements CLI commands for the code generator.

        It defines:

            :attributes:
                | _service - File generation orchestrator service.
                | _parser - CLI argument parser.
                | _commands - Map of command names to command instances.
                | _is_initialized - CLI component initialization status.
            :methods:
                | __init__ - Initializes the CLI with CLI adapters.
                | run - Parses CLI arguments and executes selected command.
                | is_initialized - Checks if the CLI component is initialized.
                | __str__ - Returns CLI instance as string representation.
    '''

    _service: IService
    _parser: IOptionManager
    _commands: Mapping[str, ICLICommand]
    _is_initialized: bool

    def __init__(self, component_bundle: CLIBundle):
        '''
            Initializes the CLI with CLI adapters.

            :param component_bundle: Bundle containing CLI adapters.
            :type component_bundle: <CLIBundle>
            :exceptions:
                | ATSValueError: Component bundle (CLIBundle) cannot be None.
                | ATSTypeError: Component bundle (CLIBundle) cannot be invalid.
        '''
        require_not_none(component_bundle, 'component bundle (CLIBundle) must be provided')
        component_bundle.validate()
        self._service = component_bundle.service
        self._parser = component_bundle.parser
        self._commands = {cmd.name: cmd for cmd in component_bundle.commands}
        self._parser.register_commands(component_bundle.commands)
        self._is_initialized = True

    @override
    def run(self) -> Mapping[str, Any]:
        '''
            Parses CLI arguments and executes selected command.

            :return: Return code, stdout and stderr messages.
            :return type: <Mapping[str, Any]>
            :exceptions:
                | ValueError: Parameters mapping must be provided.
                | TypeError: Parameters mapping must be a mapping.
                | ATSTypeError: If parameters are of invalid type.
                | ATSValueError: If parameter constraints are violated.
                | ATSGeneratorError: If archive parsing or template rendering fails.
        '''
        command_name, params = self._parser.parse_command()
        cmd = self._commands.get(command_name)

        return cmd.execute(params=params, service=self._service) if cmd else {
            "return_code": -1, "stdout": [], "stderr": ["Unknown command"]
        }

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if the CLI component is initialized.

            :return: True if the CLI component is initialized, False otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._is_initialized

    @override
    def __str__(self) -> str:
        '''
            Returns CLI instance as string representation.

            :return: CLI instance as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
