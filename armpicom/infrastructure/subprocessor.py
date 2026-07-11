# -*- coding: UTF-8 -*-

'''
Module
    subprocessor.py
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
    Defines sub-processor adapter implementing ISubProcessor.
'''

from __future__ import annotations

from collections.abc import Mapping
from os import walk
from os.path import dirname, realpath, relpath
from typing import Any, override

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.factory_class import to_str
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_value import require_not_none

from armpicom.service.isubprocessor import ISubProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = r'1.9.6'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class SubProcessor(ISubProcessor):
    '''
        Adapter that executes sub-processes.

        It defines:

            :attributes:
                | _scheme - Path to the scheme json file.
                | _templates - Path to the templates tgz file.
                | _generator - Generator adapter used to generate code from templates.
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
            :methods:
                | run - Executes a sub-process.
                | is_initialized - Checks if the subprocessor is initialized.
                | __str__ - Returns the SubProcessor as string representation.
    '''

    _scheme: str = 'config/scheme.json'
    _templates: str = 'config/templates.tgz'
    _generator: IGenerator
    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(self, generator: IGenerator) -> None:
        '''
            Initializes the SubProcessor adapter.

            :param generator: Generator adapter.
            :type generator: <IGenerator>
            :exceptions:
                | ATSValueError - The generator must be provided.
        '''
        require_not_none(generator, r'generator must be provided')
        self._generator = generator
        factory_context_bundle(self, self._generator.get_shared_context())

    @override
    def run(self, *, params: Mapping[str, Any]) -> Mapping[str, Any]:
        '''
            Executes the generator.

            :param params: The command parameters for generator.
            :type params: <Mapping[str, Any]>
            :return: Return code, stdout and stderr messages.
            :rtype: <Mapping[str, Any]>
            :exceptions:
                | ATSTypeError: If parameters are of invalid type.
                | ATSValueError: If parameter constraints are violated.
                | ATSGeneratorError: If archive parsing or template rendering fails.
        '''
        current_dir: str = dirname(realpath(__file__))
        output_dir: str = params.get('output')
        project_name: str = params.get('name')
        scheme: str = f'{current_dir}/{self._scheme}'
        templates: str = f'{current_dir}/{self._templates}'

        success = self._generator.generate(
            GeneratorBundle(
                archive_path=templates,
                target_dir=output_dir,
                template_key='base',
                scheme=scheme,
                template_values={'project_name': project_name}
            )
        )

        if success:
            self._reporter.success(["    Generated files:"])

            for root, dirs, files in walk(output_dir):
                for file in files:
                    rel_dir = relpath(root, output_dir)

                    if rel_dir == '.':
                        self._reporter.success([f"      {file}"])
                    else:
                        self._reporter.success([f"      {rel_dir}/{file}"])

        return {
            "returncode": 0 if success else 1,
            "stdout": f'project {project_name} successfully generated.' if success else '',
            "stderr": f'failed to generate {project_name} project.' if not success else ''
        }

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if the subprocessor is initialized.

            :return: True if the subprocessor is initialized, False otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._generator.is_initialized()

    @override
    def __str__(self) -> str:
        '''
            Returns the SubProcessor as string representation.

            :return: The SubProcessor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
