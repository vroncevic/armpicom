# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
Copyright
    Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class GenArmPICOM with attribute(s) and method(s).
    Generates project setup for RPI Pico by templates and parameters.
'''

import sys
from typing import List, Dict
from os.path import dirname, realpath

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from armpicom.pro.config import ProConfig
    from armpicom.pro.config.pro_name import ProName
    from armpicom.pro.read_template import ReadTemplate
    from armpicom.pro.write_template import WriteTemplate
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/armpicom'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.6.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenArmPICOM(FileCheck, ProConfig, ProName):
    '''
        Defines class GenArmPICOM with attribute(s) and method(s).
        Generates project setup for RPI Pico by templates and parameters.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _PRO_STRUCTURE - Project setup (template, module).
                | _reader - Reader API.
                | _writer - Writer API.
            :methods:
                | __init__ - Initial GenArmPICOM constructor.
                | get_reader - Getter for template reader.
                | get_writer - Getter for template writer.
                | gen_project - Generate RPI PI Pico CMake structure.
    '''

    _GEN_VERBOSE: str = 'ARMPICOM::PRO::GENARMPICOM'
    _PRO_STRUCTURE: str = '/../conf/project.yaml'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initial GenArmPICOM constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        FileCheck.__init__(self, verbose)
        ProConfig.__init__(self, verbose)
        ProName.__init__(self, verbose)
        verbose_message(verbose, [f'{self._GEN_VERBOSE} init generator'])
        self._reader: ReadTemplate | None = ReadTemplate(verbose)
        self._writer: WriteTemplate | None = WriteTemplate(verbose)
        current_dir: str = dirname(realpath(__file__))
        pro_structure: str = f'{current_dir}{self._PRO_STRUCTURE}'
        self.check_path(pro_structure, verbose)
        self.check_mode('r', verbose)
        self.check_format(pro_structure, 'yaml', verbose)
        if self.is_file_ok():
            yml2obj = Yaml2Object(pro_structure)
            self.config = yml2obj.read_configuration()

    def get_reader(self) -> ReadTemplate | None:
        '''
            Getter for template reader.

            :return: Template reader object | None
            :rtype: <ReadTemplate> | <NoneType>
            :exceptions: None
        '''
        return self._reader

    def get_writer(self) -> WriteTemplate | None:
        '''
            Getter for template writer.

            :return: Template writer object | none
            :rtype: <WriteTemplate> | <NoneType
            :exceptions: None
        '''
        return self._writer

    def gen_project(self, pro_name: str | None, verbose: bool = False) -> bool:
        '''
            Generate RPI PI Pico CMake structure.

            :param pro_name: Project name | None
            :type pro_name: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('str:pro_name', pro_name)
        ])
        if error_id == checker.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(pro_name):
            raise ATSValueError('missing project name')
        status: bool = False
        if self.config and self._reader and self._writer:
            templates: List[Dict[str, str]] = self._reader.read(
                self.config, verbose
            )
            if templates:
                status = self._writer.write(templates, pro_name, verbose)
        return status
