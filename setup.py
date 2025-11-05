#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    setup.py
Copyright
    Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines setup for tool armpicom.
'''

from __future__ import print_function
from typing import List, Optional
from os.path import abspath, dirname, join
from setuptools import setup

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/armpicom'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__: str = '1.9.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

TOOL_DIR: str = 'armpicom/'
CONF: str = 'conf'
TEMPLATE: str = 'conf/template'
LOG: str = 'log'
BUILD: str = 'conf/template/build'
SRC: str = 'conf/template/src'
THIS_DIR: str = abspath(dirname(__file__))
long_description: Optional[str] = None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()
PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: List[str] = ['3.10', '3.11', '3.12']
SUPPORTED_PY_VERSIONS: List[str] = [
    f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS
]
PYP_CLASSIFIERS: List[str] = SUPPORTED_PY_VERSIONS
setup(
    name='armpicom',
    version='1.9.3',
    description='Python package for generation of RPI configuration/build',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/armpicom',
    license='GPL-3.0-or-later',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='setup, python, install, RPI Pico, CMake, generator',
    platforms='any',
    classifiers=PYP_CLASSIFIERS,
    packages=['armpicom', 'armpicom.pro'],
    install_requires=['ats-utilities'],
    package_data={
        'armpicom': [
            'py.typed',
            f'{CONF}/armpicom.logo',
            f'{CONF}/armpicom.cfg',
            f'{CONF}/armpicom_util.cfg',
            f'{CONF}/project.yaml',
            f'{TEMPLATE}/CMakeLists.template',
            f'{TEMPLATE}/pico_sdk_import.template',
            f'{TEMPLATE}/pro_auto_set_url.template',
            f'{BUILD}/armpicom.md',
            f'{SRC}/CMakeLists.template',
            f'{SRC}/main.template',
            f'{LOG}/armpicom.log'
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            f'{TOOL_DIR}run/armpicom_run.py'
        ]
    )]
)
