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
    Unit tests for main engine (ARMPicom).
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.option.ioption_manager import IOptionManager

from armpicom.engine import ARMPicom
from armpicom.armpicom_bundle import ARMPicomBundle
from armpicom.service.isubprocessor import ISubProcessor
from armpicom.service.iservice import IService
from armpicom.infrastructure.icli import ICLI

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.9.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class TestEngine(unittest.TestCase):
    '''
        Defines engine unit tests.
    '''

    def test_default_init(self) -> None:
        '''
            Tests default constructor initialization of ARMPicom.
        '''
        engine: ARMPicom = ARMPicom()
        self.assertTrue(engine.is_initialized())
        self.assertIsNotNone(engine._cli)

    @patch.object(ARMPicom, "_info_file", "invalid/path/armpicom.cfg")
    def test_init_not_initialized(self) -> None:
        '''
            Tests initialization fails when config is invalid.
        '''
        engine: ARMPicom = ARMPicom()
        self.assertFalse(engine.is_initialized())

    @patch('armpicom.engine.CLI', side_effect=Exception("Unexpected error"))
    def test_init_unexpected_exception(self, mock_cli: MagicMock) -> None:
        '''
            Tests initialization catches unexpected exception.
        '''
        engine: ARMPicom = ARMPicom()
        self.assertFalse(engine.is_initialized())

    def test_init_component_not_initialized(self) -> None:
        '''
            Tests engine is not initialized if one component is uninitialized.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = False

        bundle = ARMPicomBundle(
            service=MagicMock(spec=IService),
            subprocessor=MagicMock(spec=ISubProcessor),
            generator=MagicMock(spec=IGenerator),
            cli=mock_cli,
            parser=MagicMock(spec=IOptionManager)
        )
        engine: ARMPicom = ARMPicom(bundle)
        self.assertFalse(engine.is_initialized())

    def test_process_unexpected_exception(self) -> None:
        '''
            Tests engine process catches unexpected exception.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.side_effect = Exception("Unexpected error")

        bundle: ARMPicomBundle = ARMPicomBundle(
            service=MagicMock(spec=IService),
            subprocessor=MagicMock(spec=ISubProcessor),
            generator=MagicMock(spec=IGenerator),
            cli=mock_cli,
            parser=MagicMock(spec=IOptionManager)
        )
        engine: ARMPicom = ARMPicom(bundle)
        self.assertTrue(engine.is_initialized())

        engine.process()
        mock_cli.run.assert_called_once()

    def test_process_expected_exception(self) -> None:
        '''
            Tests engine process catches expected exception.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.side_effect = ATSValueError("Expected error")

        bundle: ARMPicomBundle = ARMPicomBundle(
            service=MagicMock(spec=IService),
            subprocessor=MagicMock(spec=ISubProcessor),
            generator=MagicMock(spec=IGenerator),
            cli=mock_cli,
            parser=MagicMock(spec=IOptionManager)
        )
        engine: ARMPicom = ARMPicom(bundle)
        self.assertTrue(engine.is_initialized())

        engine.process()
        mock_cli.run.assert_called_once()

    def test_process_failure_code(self) -> None:
        '''
            Tests failed command processing handling.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.return_value = {"returncode": 1, "stdout": "", "stderr": "Failed"}

        bundle: ARMPicomBundle = ARMPicomBundle(
            service=MagicMock(spec=IService),
            subprocessor=MagicMock(spec=ISubProcessor),
            generator=MagicMock(spec=IGenerator),
            cli=mock_cli,
            parser=MagicMock(spec=IOptionManager)
        )
        engine: ARMPicom = ARMPicom(bundle)
        self.assertTrue(engine.is_initialized())

        engine.process()
        mock_cli.run.assert_called_once()

    def test_process_not_initialized(self) -> None:
        '''
            Tests processing fails immediately if engine is uninitialized.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = False

        bundle: ARMPicomBundle = ARMPicomBundle(
            service=MagicMock(spec=IService),
            subprocessor=MagicMock(spec=ISubProcessor),
            generator=MagicMock(spec=IGenerator),
            cli=mock_cli,
            parser=MagicMock(spec=IOptionManager)
        )
        engine: ARMPicom = ARMPicom(bundle)
        self.assertFalse(engine.is_initialized())

        engine.process()
        mock_cli.run.assert_not_called()

    def test_process_success(self) -> None:
        '''
            Tests successful command processing with output details.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.return_value = {"returncode": 0, "stdout": "Success"}

        bundle: ARMPicomBundle = ARMPicomBundle(
            service=MagicMock(spec=IService),
            subprocessor=MagicMock(spec=ISubProcessor),
            generator=MagicMock(spec=IGenerator),
            cli=mock_cli,
            parser=MagicMock(spec=IOptionManager)
        )
        engine: ARMPicom = ARMPicom(bundle)
        self.assertTrue(engine.is_initialized())

        engine.process()
        mock_cli.run.assert_called_once()

    def test_process_success_default_stdout(self) -> None:
        '''
            Tests successful command processing with empty stdout.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.return_value = {"returncode": 0, "stdout": ""}

        bundle: ARMPicomBundle = ARMPicomBundle(
            service=MagicMock(spec=IService),
            subprocessor=MagicMock(spec=ISubProcessor),
            generator=MagicMock(spec=IGenerator),
            cli=mock_cli,
            parser=MagicMock(spec=IOptionManager)
        )
        engine: ARMPicom = ARMPicom(bundle)
        self.assertTrue(engine.is_initialized())

        engine.process()
        mock_cli.run.assert_called_once()
