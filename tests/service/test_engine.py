# -*- coding: UTF-8 -*-

'''
Module
    test_engine.py
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
    Unit tests for application service (Service).
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from armpicom.service.isubprocessor import ISubProcessor
from armpicom.service.engine import Service

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.9.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class TestService(unittest.TestCase):
    '''
        Defines application service unit tests.
    '''

    def test_init_success(self) -> None:
        '''
            Tests successful service initialization.
        '''
        mock_sub = MagicMock(spec=ISubProcessor)
        service = Service(mock_sub)
        self.assertEqual(service._subprocessor, mock_sub)

    def test_init_failure(self) -> None:
        '''
            Tests initialization fails when subprocessor is None.
        '''
        with self.assertRaises(ValueError) as ctx:
            Service(None)  # type: ignore
        self.assertEqual(str(ctx.exception), 'service::init - subprocessor must be provided')

    def test_execute(self) -> None:
        '''
            Tests execute delegates run and returns parameters from subprocessor.
        '''
        mock_sub = MagicMock(spec=ISubProcessor)
        expected_res = {"returncode": 0, "stdout": "ok"}
        mock_sub.run.return_value = expected_res

        service = Service(mock_sub)
        params = {"name": "test"}
        res = service.execute(params=params)

        mock_sub.run.assert_called_once_with(params=params)
        self.assertEqual(res, expected_res)

    def test_is_initialized(self) -> None:
        '''
            Tests is_initialized delegates check to subprocessor.
        '''
        mock_sub = MagicMock(spec=ISubProcessor)
        
        service = Service(mock_sub)
        
        mock_sub.is_initialized.return_value = True
        self.assertTrue(service.is_initialized())
        
        mock_sub.is_initialized.return_value = False
        self.assertFalse(service.is_initialized())

    def test_str_repr(self) -> None:
        '''
            Tests string representation of Service.
        '''
        mock_sub = MagicMock(spec=ISubProcessor)
        service = Service(mock_sub)
        
        service_str = str(service)
        self.assertIsNotNone(service_str)
        self.assertIsInstance(service_str, str)
        self.assertNotEqual(service_str, "")
