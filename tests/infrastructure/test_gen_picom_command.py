# -*- coding: UTF-8 -*-

'''
Module
    test_gen_picom_command.py
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
    Unit tests for GenPicomCommand.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from armpicom.service.iservice import IService
from armpicom.infrastructure.gen_picom_command import GenPicomCommand

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.9.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class TestGenPicomCommand(unittest.TestCase):
    '''
        Defines GenPicomCommand unit tests.
    '''

    def test_gen_picom_command_metadata_and_execution(self) -> None:
        '''
            Tests GenPicomCommand properties and execution.
        '''
        cmd = GenPicomCommand()
        self.assertEqual(cmd.name, "create")
        self.assertEqual(cmd.help_text, "Generate picom project files")
        self.assertEqual(len(cmd.options), 2)
        
        self.assertEqual(cmd.options[0].name, "--name")
        self.assertEqual(cmd.options[1].name, "--output")

        self.assertIsNotNone(str(cmd))
        self.assertIsNotNone(repr(cmd))

        # Test execute when service is initialized
        mock_service = MagicMock(spec=IService)
        mock_service.is_initialized.return_value = True
        params = {"name": "testproject", "output": "./demo"}
        
        expected_res = {"returncode": 0, "stdout": "project generated"}
        mock_service.execute.return_value = expected_res
        
        res = cmd.execute(params=params, service=mock_service)
        mock_service.execute.assert_called_once_with(params=params)
        self.assertEqual(res, expected_res)

        # Test execute when service is not initialized
        mock_service_uninit = MagicMock(spec=IService)
        mock_service_uninit.is_initialized.return_value = False
        
        res_uninit = cmd.execute(params=params, service=mock_service_uninit)
        self.assertEqual(res_uninit.get("return_code"), -1)
        self.assertEqual(res_uninit.get("stderr"), ["Service not initialized"])
