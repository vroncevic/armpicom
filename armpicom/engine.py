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
    Main engine orchestrator class for Task Code Generator CLI.
'''

from __future__ import annotations

from collections.abc import Mapping, Sequence
from os.path import dirname, realpath
from typing import Any, override

from ats_utilities.base.engine import Base
from ats_utilities.base.component_bundle import BaseComponentBundle
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_value import require_not_satisfied
from ats_utilities.exceptions import ATSTypeError, ATSValueError, ATSGeneratorError

from armpicom.armpicom_bundle import ARMPicomBundle
from armpicom.service.iservice import IService
from armpicom.service.engine import Service
from armpicom.service.isubprocessor import ISubProcessor
from armpicom.infrastructure.subprocessor import SubProcessor
from armpicom.infrastructure.icli_command import ICLICommand
from armpicom.infrastructure.cli_bundle import CLIBundle
from armpicom.infrastructure.gen_picom_command import GenPicomCommand
from armpicom.infrastructure.icli import ICLI
from armpicom.infrastructure.cli import CLI

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = r'1.9.6'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ARMPicom(Base):
    '''
        Engine orchestrating the initialization and execution of ARMPicom.

        It defines:

            :attributes:
                | _info_file - Path to the info file.
                | _is_initialized - Flag indicating if the engine is initialized.
                | _checker - Interface for checking component validity.
                | _reporter - Interface for reporting component results.
                | _verbose - Flag indicating if the engine is verbose.
                | _generator - Interface for generating components.
                | _option_parser - Interface for parsing options.
                | _cli - Adapter for command line user interface.
            :methods:
                | __init__ - Initializes the ARMPicom engine with adapters and services.
                | process - Starts ARMPicom engine.
    '''

    _info_file: str = 'infrastructure/config/armpicom.cfg'
    _is_initialized: bool
    _checker: IChecker
    _reporter: IReporter
    _verbose: bool
    _generator: IGenerator
    _option_parser: IOptionManager
    _cli: ICLI

    def __init__(self, component_bundle: ARMPicomBundle | None = None) -> None:
        '''
            Initializes the ARMPicom engine with adapters and services.

            :param component_bundle: ARMPicom bundle containing adapters and services | None.
            :type component_bundle: <ARMPicomBundle | None>
            :exceptions: None.
        '''
        try:
            current_dir: str = dirname(realpath(__file__))
            super().__init__(BaseComponentBundle(info_file=f'{current_dir}/{self._info_file}', use_generator=True))

            require_not_satisfied(
                not self._is_initialized, f'failed to initialize engine with {current_dir}/{self._info_file}'
            )

            # Mark as not initialized (waiting for other components to be initialized)
            self._is_initialized = False

            # Dependency injection: Dependency Inversion Principle
            # Use provided component bundle or use default adapters
            bundle: ARMPicomBundle = component_bundle or ARMPicomBundle()

            # Initialization of outbound adapter (Generator)
            # Generator for generating code
            # Force default implementation of generator if not provided by bundle
            generator: IGenerator = bundle.generator or self._generator

            # Initialization of inbound adapter (Option Manager)
            # Option manager for parsing options
            # Force default implementation of option manager if not provided by bundle
            parser: IOptionManager = bundle.parser or self._options_parser

            # Initialization of outbound adapter (SubProcessor)
            # Sub processor for orchestrating generator
            # Force default implementation of sub processor if not provided by bundle
            subprocessor: ISubProcessor = bundle.subprocessor or SubProcessor(generator=generator)

            # Injecting outbound adapter into service
            # Force default implementation of service if not provided by bundle
            service: IService = bundle.service or Service(subprocessor=subprocessor)

            # Setting up CLI command strategies (Command strategies for CLI)
            commands: Sequence[ICLICommand] = [GenPicomCommand()]

            # Setting up inbound adapter (CLI interface)
            cli_bundle: CLIBundle = CLIBundle(service=service, parser=parser, commands=commands)
            self._cli = bundle.cli or CLI(cli_bundle)

            # Mark as initialized (all components initialized)
            self._is_initialized = all([
                component.is_initialized() for component in [
                    generator, parser, subprocessor, service, self._cli
                ] if component
            ])
            self._reporter.success([r'✅ armpicom: engine initialized successfully!'])

        except (ValueError, ATSValueError) as exc:
            print(f'\x1b[31m❌ armpicom: {exc}\x1b[0m')

        except Exception as exc:
            print(f'\x1b[31m❌ armpicom unexpected exception: {exc}\x1b[0m')

    @override
    def process(self) -> None:
        '''
            Starts ARMPicom via CLI adapter.

            :exceptions: None.
        '''
        result: Mapping[str, Any] = {}

        try:
            if self.is_initialized():
                self._reporter.success([r'🔥 Starting execution command...'])
                result = self._cli.run()
                self._reporter.success([r'✅ Execution finished!'])

                if result.get("returncode") != 0:
                    self._reporter.error([f'❌ armpicom: {result.get("stderr") or 'failed to execute command'}!'])
                    self._reporter.error([r'❌ armpicom: exiting with error!'])
                else:
                    self._reporter.success([f'✅ armpicom: {result.get("stdout") or 'done'}!'])
                    self._reporter.success([r'✅ armpicom: exiting successfully!'])
            else:
                self._reporter.error([r'❌ armpicom: engine not initialized!'])

        except (TypeError, ValueError, ATSTypeError, ATSValueError, ATSGeneratorError) as exc:
            print(f'\x1b[31m❌ armpicom: {exc}\x1b[0m')

        except Exception as exc:
            print(f'\x1b[31m❌ armpicom unexpected exception: {exc}\x1b[0m')
