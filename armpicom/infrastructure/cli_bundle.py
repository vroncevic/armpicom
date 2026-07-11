# -*- coding: UTF-8 -*-

'''
Module
    cli_bundle.py
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
    Defines a CLIBundle bundle for the infrastructure adapters.
'''

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, asdict
from typing import Any

from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.factory_value import require_not_none
from ats_utilities.factory_type import check_type

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


@dataclass(slots=True, kw_only=True)
class CLIBundle:
    '''
        Data class for CLI adapters bundle.

        It defines:

            :attributes:
                | service - Service orchestrating generation (default None).
                | parser - Argument parser for parsing CLI command args (default None).
                | commands - Sequence of CLI command instances (default None).
            :methods:
                | validate - Validates that CLIBundle is valid (can be called after merge).
                | merge - Merges non-None values from another CLIBundle.
                | to_dict - Converts the CLIBundle to a dictionary.
    '''

    service: IService | None = None
    parser: IOptionManager | None = None
    commands: Sequence[ICLICommand] | None = None

    def validate(self) -> None:
        '''
            Validates that CLIBundle is valid (can be called after merge).
            Performs validation of service, parser and commands attributes.
            Service must be non-None and an instance of IService interface.
            Parser must be non-None and an instance of IOptionManager interface.
            Commands sequence must be non-None and an instance of Sequence interface.

            :exceptions:
                | ATSValueError: Service must be provided.
                | ATSValueError: Parser must be provided.
                | ATSValueError: Commands sequence must be provided.
                | ATSTypeError: Service must be of type IService.
                | ATSTypeError: Parser must be of type IOptionManager.
                | ATSTypeError: Commands sequence must be of type Sequence.
        '''
        require_not_none(self.service, r'service must be provided')
        require_not_none(self.parser, r'parser must be provided')
        require_not_none(self.commands, r'commands sequence must be provided')
        check_type(self.service, IService, r'service must be of type IService')
        check_type(self.parser, IOptionManager, r'parser must be of type IOptionManager')
        check_type(self.commands, Sequence, r'commands must be of type Sequence')

    def merge(self, other: CLIBundle) -> None:
        '''
            Merges non-None values from another CLIBundle into this one.

            :param other: Another CLIBundle to merge into this one.
            :type other: <CLIBundle>
            :exceptions:
                | ATSTypeError: Other must be of type CLIBundle.
        '''
        check_type(other, CLIBundle, r'other must be of type CLIBundle')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the CLIBundle to a dictionary.

            :return: Dictionary representation of the CLIBundle.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return asdict(self)
