# -*- coding: UTF-8 -*-

'''
Module
    test_subprocessor.py
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
    Unit tests for SubProcessor adapter.
'''

from __future__ import annotations

import os
import tempfile
import unittest
from os.path import join
from unittest.mock import MagicMock

from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.engine import Checker
from ats_utilities.reporter.engine import Reporter
from ats_utilities.generator.igenerator import IGenerator

from armpicom.infrastructure.subprocessor import SubProcessor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.9.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class TestSubProcessor(unittest.TestCase):
    '''
        Defines SubProcessor adapter unit tests.
    '''

    def test_subprocessor_init_failure(self) -> None:
        '''
            Tests SubProcessor init raises ATSValueError when generator is None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            SubProcessor(None)  # type: ignore
        self.assertEqual(str(ctx.exception), 'subprocessor::__init__ - generator must be provided')

    def test_subprocessor_run_success(self) -> None:
        '''
            Tests successful execution of SubProcessor run with walks.
        '''
        mock_generator = MagicMock(spec=IGenerator)
        mock_context = ContextBundle(checker=Checker(), reporter=Reporter(), verbose=False)
        mock_generator.get_shared_context.return_value = mock_context

        with tempfile.TemporaryDirectory() as tmpdir:
            # create nested files to test both branches of directory walking
            with open(join(tmpdir, "file1.txt"), "w") as f:
                f.write("content1")
            
            os.makedirs(join(tmpdir, "nested"), exist_ok=True)
            with open(join(tmpdir, "nested", "file2.txt"), "w") as f:
                f.write("content2")
            
            mock_generator.generate.return_value = True
            
            sub = SubProcessor(mock_generator)
            self.assertTrue(sub.is_initialized())
            
            params = {"name": "testproject", "output": tmpdir}
            res = sub.run(params=params)

            self.assertEqual(res["returncode"], 0)
            self.assertIn("testproject successfully generated.", res["stdout"])
            self.assertEqual(res["stderr"], "")

    def test_subprocessor_run_failure(self) -> None:
        '''
            Tests failed execution of SubProcessor run.
        '''
        mock_generator = MagicMock(spec=IGenerator)
        mock_context = ContextBundle(checker=Checker(), reporter=Reporter(), verbose=False)
        mock_generator.get_shared_context.return_value = mock_context

        mock_generator.generate.return_value = False
        
        sub = SubProcessor(mock_generator)
        params = {"name": "testproject", "output": "./demo"}
        res = sub.run(params=params)

        self.assertEqual(res["returncode"], 1)
        self.assertEqual(res["stdout"], "")
        self.assertIn("failed to generate testproject project.", res["stderr"])

    def test_subprocessor_is_initialized(self) -> None:
        '''
            Tests is_initialized status of SubProcessor.
        '''
        mock_generator = MagicMock(spec=IGenerator)
        mock_context = ContextBundle(checker=Checker(), reporter=Reporter(), verbose=False)
        mock_generator.get_shared_context.return_value = mock_context

        sub = SubProcessor(mock_generator)
        
        mock_generator.is_initialized.return_value = True
        self.assertTrue(sub.is_initialized())

        mock_generator.is_initialized.return_value = False
        self.assertFalse(sub.is_initialized())

        self.assertIsNotNone(str(sub))
        self.assertIsNotNone(repr(sub))
