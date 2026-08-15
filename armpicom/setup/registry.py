# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core armpicom components for simplification of armpicom bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from armpicom.core.service.iservice import IService
from armpicom.core.service.isubprocessor import ISubProcessor
from armpicom.infrastructure.cli.icli import ICLI
from armpicom.setup.bundle import ARMPicomBundle
from armpicom.setup.validator import ARMPicomBundleValidator
from armpicom.setup.keys import ARMPicomBundleKeys
from armpicom.setup.dependencies import ARMPicomBundleDependencies
from armpicom.setup.dep_validator import ARMPicomBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '2.0.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ARMPicomBundleRegistry:
    '''
        Encapsulates core armpicom components for simplification of armpicom bundle.

        It defines:

            :methods:
                | create_bundle - Creates the armpicom bundle.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: ARMPicomBundleDependencies) -> ARMPicomBundle:
        '''
            Creates the armpicom bundle.

            :param dependencies: The armpicom bundle dependencies.
            :return: The armpicom bundle.
            :exceptions:
                | ATSValueError: The armpicom bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The armpicom bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The armpicom bundle must be provided and have proper values.
                | ATSTypeError:  The armpicom bundle must be an instance of ARMPicomBundle and
                |                its attributes must be instances of their respective types.
        '''
        ARMPicomBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(ARMPicomBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(ARMPicomBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(ARMPicomBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(ARMPicomBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: ARMPicomBundle = ARMPicomBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        ARMPicomBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: The registry version.
            :exceptions: None.
        '''
        return __version__
