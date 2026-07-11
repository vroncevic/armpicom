# -*- coding: UTF-8 -*-

'''
Module
    icli_command.py
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
    Defines abstract ICLICommand strategy interface and CommandOption.
'''

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Mapping, Sequence
from typing import Any

from ats_utilities.option.ioption_manager import IOptionCommand
from ats_utilities.option.command.command_option import CommandOption

from armpicom.service.iservice import IService

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = r'1.9.6'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ICLICommand(IOptionCommand):
    '''
        Abstract base class representing a CLI subcommand strategy.

        It defines:

            :methods:
                | name - Property returning name of the command.
                | help_text - Property returning help text of the command.
                | options - Property returning sequence of command options.
                | execute - Performs subcommand actions.
                | __str__ - Returns the string representation of the command.
    '''

    @property
    @abstractmethod
    def name(self) -> str:
        '''
            Returns the command name.

            :return: The command name.
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @property
    @abstractmethod
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: The command help text.
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @property
    @abstractmethod
    def options(self) -> Sequence[CommandOption]:
        '''
            Returns the command options.

            :return: Sequence of command options.
            :rtype: <Sequence[CommandOption]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def execute(self, *, params: Mapping[str, Any], service: IService) -> Mapping[str, Any]:
        '''
            Executes the file generation logic for this command.

            :param params: Subcommand parameters from CLI parser.
            :type params: <Mapping[str, Any]>
            :param service: Orchestration service instance.
            :type service: <IService>
            :return: Return code, stdout and stderr messages.
            :return type: <Mapping[str, Any]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of the command.

            :return: The string representation of the command.
            :rtype: <str>
            :exceptions: None.
        '''
        pass    
