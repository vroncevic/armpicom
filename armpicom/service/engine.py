# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Defines application service for file generation.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, override

from armpicom.service.iservice import IService
from armpicom.model.generate_project import GeneratedProject
from armpicom.service.isubprocessor import ISubProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = r'1.9.6'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Service(IService):
    '''
        Service for orchestrating the file generation process.

        It defines:

            :attributes:
                | _subprocessor - Adapter for subprocessing.
            :methods:
                | execute - Generates and writes user files.
                | is_initialized - Checks if the service is initialized.
    '''

    def __init__(self, subprocessor: ISubProcessor) -> None:
        '''
            Initializes the Service.

            :param subprocessor: Subprocessor adapter.
            :type subprocessor: <ISubProcessor>
            :exceptions:
                | ValueError: Subprocessor must be provided.
        '''
        if subprocessor is None:
            raise ValueError(r'service::init - subprocessor must be provided')

        self._subprocessor: ISubProcessor = subprocessor

    @override
    def execute(self, *, params: Mapping[str, Any]) -> Mapping[str, Any]:
        '''
            Generates picom configuration files.

            :param params: Parameters for template formatting.
            :type params: <Mapping[str, Any]>
            :return: Return code, stdout and stderr messages.
            :return type: <Mapping[str, Any]>
            :exceptions:
                | ValueError: Parameters mapping must be provided.
                | TypeError: Parameters mapping must be a mapping.
                | ATSTypeError: If parameters are of invalid type.
                | ATSValueError: If parameter constraints are violated.
                | ATSGeneratorError: If archive parsing or template rendering fails.
        '''
        project: GeneratedProject = GeneratedProject.check_parameters(params)

        return self._subprocessor.run(params=project.params)

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if the service is initialized.

            :return: True if the service is initialized, False otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._subprocessor.is_initialized()
