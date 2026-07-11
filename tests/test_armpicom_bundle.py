# -*- coding: UTF-8 -*-

'''
Module
    test_armpicom_bundle.py
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
    Unit tests for ARMPicomBundle.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.option.ioption_manager import IOptionManager

from armpicom.armpicom_bundle import ARMPicomBundle
from armpicom.service.iservice import IService
from armpicom.service.isubprocessor import ISubProcessor
from armpicom.infrastructure.icli import ICLI

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.9.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class TestARMPicomBundle(unittest.TestCase):
    '''
        Defines ARMPicomBundle unit tests.
    '''

    def test_bundle_validation_success(self) -> None:
        '''
            Tests successful validation of ARMPicomBundle.
        '''
        bundle = ARMPicomBundle(
            service=MagicMock(spec=IService),
            subprocessor=MagicMock(spec=ISubProcessor),
            generator=MagicMock(spec=IGenerator),
            cli=MagicMock(spec=ICLI),
            parser=MagicMock(spec=IOptionManager)
        )
        bundle.validate()  # Should not raise any error

    def test_bundle_validation_failures_none(self) -> None:
        '''
            Tests ARMPicomBundle validate raises error when fields are None.
        '''
        # service is None
        bundle = ARMPicomBundle(service=None)
        with self.assertRaises(ATSValueError) as ctx:
            bundle.validate()
        self.assertEqual(str(ctx.exception), 'armpicombundle::validate - service must be provided')

        # subprocessor is None
        bundle = ARMPicomBundle(service=MagicMock(spec=IService), subprocessor=None)
        with self.assertRaises(ATSValueError) as ctx:
            bundle.validate()
        self.assertEqual(str(ctx.exception), 'armpicombundle::validate - subprocessor must be provided')

        # generator is None
        bundle = ARMPicomBundle(
            service=MagicMock(spec=IService),
            subprocessor=MagicMock(spec=ISubProcessor),
            generator=None
        )
        with self.assertRaises(ATSValueError) as ctx:
            bundle.validate()
        self.assertEqual(str(ctx.exception), 'armpicombundle::validate - generator must be provided')

        # cli is None
        bundle = ARMPicomBundle(
            service=MagicMock(spec=IService),
            subprocessor=MagicMock(spec=ISubProcessor),
            generator=MagicMock(spec=IGenerator),
            cli=None
        )
        with self.assertRaises(ATSValueError) as ctx:
            bundle.validate()
        self.assertEqual(str(ctx.exception), 'armpicombundle::validate - cli must be provided')

        # parser is None
        bundle = ARMPicomBundle(
            service=MagicMock(spec=IService),
            subprocessor=MagicMock(spec=ISubProcessor),
            generator=MagicMock(spec=IGenerator),
            cli=MagicMock(spec=ICLI),
            parser=None
        )
        with self.assertRaises(ATSValueError) as ctx:
            bundle.validate()
        self.assertEqual(str(ctx.exception), 'armpicombundle::validate - parser must be provided')

    def test_bundle_validation_failures_type(self) -> None:
        '''
            Tests ARMPicomBundle validate raises type error when fields are invalid.
        '''
        # service is invalid type
        bundle = ARMPicomBundle(
            service="invalid_service",  # type: ignore
            subprocessor=MagicMock(spec=ISubProcessor),
            generator=MagicMock(spec=IGenerator),
            cli=MagicMock(spec=ICLI),
            parser=MagicMock(spec=IOptionManager)
        )
        with self.assertRaises(ATSTypeError) as ctx:
            bundle.validate()
        self.assertEqual(str(ctx.exception), 'armpicombundle::validate - service must be an IService')

    def test_bundle_merge_success(self) -> None:
        '''
            Tests ARMPicomBundle merge method.
        '''
        srv = MagicMock(spec=IService)
        sub = MagicMock(spec=ISubProcessor)
        gen = MagicMock(spec=IGenerator)
        cli = MagicMock(spec=ICLI)
        parser = MagicMock(spec=IOptionManager)

        bundle1 = ARMPicomBundle(
            service=srv,
            subprocessor=sub,
            generator=gen,
            cli=cli,
            parser=None
        )
        bundle2 = ARMPicomBundle(parser=parser)

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.service, srv)
        self.assertEqual(bundle1.subprocessor, sub)
        self.assertEqual(bundle1.generator, gen)
        self.assertEqual(bundle1.cli, cli)
        self.assertEqual(bundle1.parser, parser)

    def test_bundle_merge_invalid_type(self) -> None:
        '''
            Tests ARMPicomBundle merge raises error when other is not ARMPicomBundle.
        '''
        bundle = ARMPicomBundle()
        with self.assertRaises(ATSTypeError) as ctx:
            bundle.merge("not_a_bundle")  # type: ignore
        self.assertEqual(str(ctx.exception), 'armpicombundle::merge - other must be an ARMPicomBundle')

    def test_bundle_to_dict(self) -> None:
        '''
            Tests ARMPicomBundle to_dict method.
        '''
        srv = MagicMock(spec=IService)
        sub = MagicMock(spec=ISubProcessor)
        gen = MagicMock(spec=IGenerator)
        cli = MagicMock(spec=ICLI)
        parser = MagicMock(spec=IOptionManager)

        bundle = ARMPicomBundle(
            service=srv,
            subprocessor=sub,
            generator=gen,
            cli=cli,
            parser=parser
        )

        d = bundle.to_dict()
        self.assertEqual(d["service"], srv)
        self.assertEqual(d["subprocessor"], sub)
        self.assertEqual(d["generator"], gen)
        self.assertEqual(d["cli"], cli)
        self.assertEqual(d["parser"], parser)
