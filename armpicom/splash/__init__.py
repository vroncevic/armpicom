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
     Defined class Splash with attribute(s) and method(s).
     Load a splash screen info and add hyperlinks.
'''

import sys
from os import get_terminal_size
from time import sleep

try:
    from pathlib import Path
    from armpicom.splash.progress_bar import ProgressBar
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/armpicom'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.0.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Splash:
    '''
        Defined class Splash with attribute(s) and method(s).
        Load a splash screen info and add hyperlinks.
        It defines:

            :attributes:
                | ORG - organization name.
                | REPO - repository name.
                | INFO_URL - project info link.
                | INFO_TXT - project info text.
                | ISSUE_URL - project issue link.
                | ISSUE_TXT - project issue text.
                | AUTHOR_URL - author info link.
                | AUTHOR_TXT - author info text.
                | LOGO - path to logo file.
            :methods:
                | __init__ - initial constructor.
                | center - center console line.
                | __str__ - dunder method for Splash.
    '''

    ORG = 'vroncevic'
    REPO = 'armpicom'
    INFO_URL = 'https://{0}.github.io/{1}'.format(ORG, REPO)
    INFO_TXT = 'github.io/{0}'.format(REPO)
    ISSUE_URL = 'https://github.com/{0}/{1}/issues/new/choose'.format(
        ORG, REPO
    )
    ISSUE_TXT = 'github.io/issue'
    AUTHOR_URL = 'https://{0}.github.io/bio/'.format(ORG)
    AUTHOR_TXT = '{0}.github.io'.format(ORG)
    LOGO = '/conf/armpicom.logo'

    def __init__(self):
        '''
            Initial constructor.

            :exceptions: None
        '''
        current_dir = Path(__file__).resolve().parent
        size = get_terminal_size(0)
        with open('{0}/..{1}'.format(current_dir, Splash.LOGO), 'r') as logo:
            for line in logo:
                self.center(size.columns, 0, line.rstrip())
        info_text = '\x1b]8;;{0}\a{1}\x1b]8;;\a'.format(
            Splash.INFO_URL, Splash.INFO_TXT
        )
        self.center(size.columns, 2, info_text)
        issue_text = '\x1b]8;;{0}\a{1}\x1b]8;;\a'.format(
            Splash.ISSUE_URL, Splash.ISSUE_TXT
        )
        self.center(size.columns, 2, issue_text)
        author_text = '\x1b]8;;{0}\a{1}\x1b]8;;\a'.format(
            Splash.AUTHOR_URL, Splash.AUTHOR_TXT
        )
        self.center(size.columns, 2, author_text)
        print("\n")
        pb = ProgressBar(size.columns-int(size.columns/2))
        for i in range(0, size.columns-int(size.columns/2)):
            pb.set_and_plot(i + 1, size.columns)
            sleep(0.01)
        del pb

    def center(self, columns, additional_shifter, text):
        '''
            Center console line.

            :param columns: colums for open console session.
            :type columns: <int>
            :param additional_shifter: additional shifters.
            :type additional_shifter: <int>
            :param text: text for console session.
            :type text: <str>
            :exceptions: None
        '''
        start_position = (columns/2) - 21
        number_of_tabs = int((start_position/8) - 1 + additional_shifter)
        print('\011' * number_of_tabs, text)

    def __str__(self):
        '''
            Dunder method for Splash.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ()'.format(self.__class__.__name__)
