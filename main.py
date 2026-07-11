# -*- coding: UTF-8 -*-

'''
Module
    main.py
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
    Main entry point for Task Code Generator CLI.
'''

from __future__ import annotations

from armpicom.engine import ARMPicom

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/armpicom'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = r'1.9.6'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def main() -> None:
    '''
        Bootstraps and runs the ARMPicom application with required adapters.

        :exceptions: None
    '''
    armpicom: ARMPicom = ARMPicom()
    armpicom.process()


if __name__ == "__main__":
    main()
