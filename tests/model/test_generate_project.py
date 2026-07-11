# -*- coding: UTF-8 -*-

'''
Module
    test_generate_project.py
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
    Unit tests for GeneratedProject model.
'''

from __future__ import annotations

import unittest
from typing import Any

from armpicom.model.generate_project import GeneratedProject

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.9.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class TestGeneratedProject(unittest.TestCase):
    '''
        Defines GeneratedProject unit tests.
    '''

    def test_check_parameters_success(self) -> None:
        '''
            Tests successful validation and instantiation of GeneratedProject.
        '''
        params = {"name": "World"}
        result = GeneratedProject.check_parameters(params)
        self.assertIsInstance(result, GeneratedProject)
        self.assertEqual(result.params, params)

    def test_check_parameters_value_error(self) -> None:
        '''
            Tests that empty parameters mapping raises ValueError.
        '''
        with self.assertRaises(ValueError) as ctx:
            GeneratedProject.check_parameters({})
        self.assertEqual(
            str(ctx.exception),
            'generated_project::check_parameters - params mapping must be provided'
        )

        with self.assertRaises(ValueError) as ctx:
            GeneratedProject.check_parameters(None)  # type: ignore
        self.assertEqual(
            str(ctx.exception),
            'generated_project::check_parameters - params mapping must be provided'
        )

    def test_check_parameters_type_error(self) -> None:
        '''
            Tests that non-mapping parameters raise TypeError.
        '''
        with self.assertRaises(TypeError) as ctx:
            GeneratedProject.check_parameters([("name", "World")])  # type: ignore
        self.assertEqual(
            str(ctx.exception),
            'generated_project::check_parameters - params must be a mapping'
        )
