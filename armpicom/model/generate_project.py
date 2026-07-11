# -*- coding: UTF-8 -*-

'''
Module
    generate_file.py
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
    Defines domain models representing generated files.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Self

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = r'1.9.6'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(frozen=True, slots=True, kw_only=True)
class GeneratedProject:
    '''
        Domain model representing a generated file.

        It defines:

            :attributes:
                | params - Mapping with parameters to fill the template.
            :methods:
                | check_parameters - Method that validates parameter values.
    '''

    params: Mapping[str, Any]

    @classmethod
    def check_parameters(cls, params: Mapping[str, Any]) -> Self:
        '''
            Method that validates parameter values.

            :param params: Mapping with parameters to generate project.
            :type params: <Mapping[str, Any]>
            :return: The generated project domain model instance.
            :rtype: <GeneratedProject>
            :exceptions:
                | ValueError: Parameters mapping must be provided.
                | TypeError: Parameters mapping must be a mapping.
        '''
        if not params:
            raise ValueError(r'generated_project::check_parameters - params mapping must be provided')

        if not isinstance(params, Mapping):
            raise TypeError(r'generated_project::check_parameters - params must be a mapping')

        return cls(params=params)
