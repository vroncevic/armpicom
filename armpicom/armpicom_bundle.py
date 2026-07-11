# -*- coding: UTF-8 -*-

'''
Module
    armpicom_bundle.py
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
    Defines a ARMPicomBundle bundle for the CLI application.
'''

from __future__ import annotations

from typing import Any
from dataclasses import dataclass, asdict

from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.factory_value import require_not_none
from ats_utilities.factory_type import check_type

from armpicom.service.isubprocessor import ISubProcessor
from armpicom.service.iservice import IService
from armpicom.infrastructure.icli import ICLI

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = r'1.9.6'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

@dataclass(slots=True, kw_only=True)
class ARMPicomBundle:
    '''
        ARMPicomBundle holding all components (adapters and services) of the CLI application.

        It defines:

            :attributes:
                | service - Service orchestrating command execution (default None).
                | subprocessor - Subprocessor adapter for running commands (default None).
                | generator - Generator for generating project structure (default None).
                | cli - Command line user interface adapter (default None).
                | parser - CLI argument parser adapter (default None).
            :methods:
                | validate - Validates that ARMPicomBundle is valid.
                | merge - Merges non-None values from another ARMPicomBundle into this one.
                | to_dict - Converts the ARMPicomBundle to a dictionary.
    '''

    service: IService | None = None
    subprocessor: ISubProcessor | None = None
    generator: IGenerator | None = None
    cli: ICLI | None = None
    parser: IOptionManager | None = None

    def validate(self) -> None:
        '''
            Validates that ARMPicomBundle is valid (can be called after merge).
            Performs validation of service, subprocessor, generator, cli and parser attributes.
            Service must be non-None and an instance of IService interface.
            Subprocessor must be non-None and an instance of ISubProcessor interface.
            Generator must be non-None and an instance of IGenerator interface.
            CLI must be non-None and an instance of ICLI interface.
            Parser must be non-None and an instance of IOptionManager interface.

            :exceptions:
                | ATSValueError: Service must be provided.
                | ATSValueError: Subprocessor must be provided.
                | ATSValueError: Generator must be provided.
                | ATSValueError: CLI must be provided.
                | ATSValueError: Parser must be provided.
                | ATSTypeError: Service is not an IService.
                | ATSTypeError: Subprocessor is not an ISubProcessor.
                | ATSTypeError: Generator is not an IGenerator.
                | ATSTypeError: CLI is not an ICLI.
                | ATSTypeError: Parser is not an IOptionManager.
        '''
        require_not_none(self.service, r'service must be provided')
        require_not_none(self.subprocessor, r'subprocessor must be provided')
        require_not_none(self.generator, r'generator must be provided')
        require_not_none(self.cli, r'cli must be provided')
        require_not_none(self.parser, r'parser must be provided')
        check_type(self.service, IService, r'service must be an IService')
        check_type(self.subprocessor, ISubProcessor, r'subprocessor must be an ISubProcessor')
        check_type(self.generator, IGenerator, r'generator must be an IGenerator')
        check_type(self.cli, ICLI, r'cli must be an ICLI')
        check_type(self.parser, IOptionManager, r'parser must be an IOptionManager')

    def merge(self, other: ARMPicomBundle) -> None:
        '''
            Merges non-None values from another ARMPicomBundle into this one.

            :param other: Another ARMPicomBundle to merge into this one.
            :type other: <ARMPicomBundle>
            :exceptions:
                | ATSTypeError: Other is not an ARMPicomBundle.
        '''
        check_type(other, ARMPicomBundle, r'other must be an ARMPicomBundle')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the ARMPicomBundle to a dictionary.

            :return: Dictionary representation of the ARMPicomBundle.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return asdict(self)
