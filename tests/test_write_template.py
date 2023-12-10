# -*- coding: UTF-8 -*-

'''
 Module
     test_write_template.py
 Copyright
     Copyright (C) 2022 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class WriteTemplateTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of WriteTemplate.
 Execute
     python3 -m unittest -v test_write_template
'''

import sys
import unittest

try:
    from armpicom.pro.write_template import WriteTemplate
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/armpicom'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/armpicom/blob/dev/LICENSE'
__version__ = '1.5.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplateTestCase(unittest.TestCase):
    '''
        Defined class WriteTemplateTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of WriteTemplate.
        It defines:

            :attributes:
                | template - Write template object.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_write_template - test write template check.
    '''

    templates = [{'CMakeLists.txt': '#\n# @brief   ${PRO} main entry point for build process\n# @version v1.0.3\n# @date    ${DATE}\n# @author  Vladimir Roncevic <elektron.ronca@gmail.com>\n#\n\n# Setup CMake version and RPI Pico SDK import\ncmake_minimum_required(VERSION 3.12)\ninclude(pico_sdk_import.cmake)\n\n# Setup project info\nproject(${PRO} C CXX ASM)\nset(CMAKE_PROJECT_VERSION 1.0.0)\nset(CMAKE_C_STANDARD 11)\nset(CMAKE_CXX_STANDARD 17)\nset(PRO_PATH $${PROJECT_SOURCE_DIR})\n\n# Initialize the SDK\npico_sdk_init()\n\n# Setup project url\ninclude(pro_auto_set_url.cmake)\n\n# Add source directory\nadd_subdirectory(src)\n\n'}, {'pico_sdk_import.cmake': '#\n# @brief   ${PRO} RPI Pico SDK import\n# @version v1.0.3\n# @date    ${DATE}\n# @author  Vladimir Roncevic <elektron.ronca@gmail.com>\n#\n\n# Checking SDK path\nif (DEFINED ENV{PICO_SDK_PATH} AND (NOT PICO_SDK_PATH))\n    set(PICO_SDK_PATH $$ENV{PICO_SDK_PATH})\n    message("Using PICO_SDK_PATH from environment (\'$${PICO_SDK_PATH}\')")\nendif ()\n\n# Checking SDK path fetched from GIT\nif (DEFINED ENV{PICO_SDK_FETCH_FROM_GIT} AND (NOT PICO_SDK_FETCH_FROM_GIT))\n    set(PICO_SDK_FETCH_FROM_GIT $$ENV{PICO_SDK_FETCH_FROM_GIT})\n    message(\n        "Using PICO_SDK_FETCH_FROM_GIT"\n        "from environment (\'$${PICO_SDK_FETCH_FROM_GIT}\')"\n    )\nendif ()\n\nif (DEFINED ENV{PICO_SDK_FETCH_FROM_GIT_PATH} AND (NOT PICO_SDK_FETCH_FROM_GIT_PATH))\n    set(PICO_SDK_FETCH_FROM_GIT_PATH $$ENV{PICO_SDK_FETCH_FROM_GIT_PATH})\n    message(\n        "Using PICO_SDK_FETCH_FROM_GIT_PATH"\n        "from environment (\'$${PICO_SDK_FETCH_FROM_GIT_PATH}\')"\n    )\nendif ()\n\n# Setup RPI PICO SDK path\nset(\n    PICO_SDK_PATH "$${PICO_SDK_PATH}" CACHE PATH "Path to the RPI Pi Pico SDK"\n)\nset(\n    PICO_SDK_FETCH_FROM_GIT "$${PICO_SDK_FETCH_FROM_GIT}"\n    CACHE BOOL\n    "Set to ON to fetch copy of SDK from git if not otherwise locatable"\n)\nset(\n    PICO_SDK_FETCH_FROM_GIT_PATH "$${PICO_SDK_FETCH_FROM_GIT_PATH}"\n    CACHE FILEPATH "location to download SDK"\n)\n\n# Fetch RPI PI SDK from GitHub\nif (NOT PICO_SDK_PATH)\n    if (PICO_SDK_FETCH_FROM_GIT)\n        include(FetchContent)\n        set(FETCHCONTENT_BASE_DIR_SAVE $${FETCHCONTENT_BASE_DIR})\n        if (PICO_SDK_FETCH_FROM_GIT_PATH)\n            get_filename_component(\n                FETCHCONTENT_BASE_DIR "$${PICO_SDK_FETCH_FROM_GIT_PATH}"\n                REALPATH BASE_DIR "$${CMAKE_SOURCE_DIR}"\n            )\n        endif ()\n        FetchContent_Declare(\n            pico_sdk\n            GIT_REPOSITORY https://github.com/RPIpi/pico-sdk\n            GIT_TAG master\n        )\n        if (NOT pico_sdk)\n            message("Downloading RPI Pi Pico SDK")\n            FetchContent_Populate(pico_sdk)\n            set(PICO_SDK_PATH $${pico_sdk_SOURCE_DIR})\n        endif ()\n        set(FETCHCONTENT_BASE_DIR $${FETCHCONTENT_BASE_DIR_SAVE})\n    else ()\n        message(\n            FATAL_ERROR\n            "SDK location was not specified."\n            "Please set PICO_SDK_PATH or set PICO_SDK_FETCH_FROM_GIT."\n        )\n    endif ()\nendif ()\n\nget_filename_component(\n    PICO_SDK_PATH "$${PICO_SDK_PATH}" REALPATH BASE_DIR "$${CMAKE_BINARY_DIR}"\n)\nif (NOT EXISTS $${PICO_SDK_PATH})\n    message(FATAL_ERROR "Directory \'$${PICO_SDK_PATH}\' not found")\nendif ()\n\nset(PICO_SDK_INIT_CMAKE_FILE $${PICO_SDK_PATH}/pico_sdk_init.cmake)\n\n# Check RPI PI SDK init configuration\nif (NOT EXISTS $${PICO_SDK_INIT_CMAKE_FILE})\n    message(\n        FATAL_ERROR\n        "Dir \'$${PICO_SDK_PATH}\' does not appear to contain RPI Pi Pico SDK"\n    )\nendif ()\n\nset(\n    PICO_SDK_PATH $${PICO_SDK_PATH} CACHE PATH "Path to RPI Pi Pico SDK" FORCE\n)\n\ninclude($${PICO_SDK_INIT_CMAKE_FILE})\n'}, {
        'pro_auto_set_url.cmake': '#\n# @brief   ${PRO} setup project url\n# @version v1.0.3\n# @date    ${DATE}\n# @author  Vladimir Roncevic <elektron.ronca@gmail.com>\n#\n\n# Macro for setup project url\nmacro(pro_auto_set_url TARGET)\n    file(\n        RELATIVE_PATH URL_REL_PATH "$${PRO_PATH}" "$${CMAKE_CURRENT_LIST_DIR}"\n    )\n    pico_set_program_url($${TARGET} "$${URL_REL_PATH}")\nendmacro()\n\n'}, {'src/main.c': '/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */\n/*\n * main.c\n * Copyright (C) ${YEAR} Vladimir Roncevic <elektron.ronca@gmail.com>\n *\n * ${PRO} is free software: you can redistribute it and/or modify it\n * under the terms of the GNU General Public License as published by the\n * Free Software Foundation, either version 3 of the License, or\n * (at your option) any later version.\n *\n * ${PRO} is distributed in the hope that it will be useful, but\n * WITHOUT ANY WARRANTY; without even the implied warranty of\n * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n * See the GNU General Public License for more details.\n *\n * You should have received a copy of the GNU General Public License along\n * with this program_name.  If not, see <http://www.gnu.org/licenses/>.\n */\n\n#include "pico/stdlib.h"\n\nint main() {\n#ifndef PICO_DEFAULT_LED_PIN\n#warning blink example requires a board with a regular LED\n#else\n    const uint LED_PIN = PICO_DEFAULT_LED_PIN;\n    gpio_init(LED_PIN);\n    gpio_set_dir(LED_PIN, GPIO_OUT);\n    while (true) {\n        gpio_put(LED_PIN, 1);\n        sleep_ms(250);\n        gpio_put(LED_PIN, 0);\n        sleep_ms(250);\n    }\n#endif\n}\n\n'}, {'src/CMakeLists.txt': '#\n# @brief   ${PRO} setup output files\n# @version v1.0.3\n# @date    ${DATE}\n# @author  Vladimir Roncevic <elektron.ronca@gmail.com>\n#\n\n# Create executable\nadd_executable("$${CMAKE_PROJECT_NAME}" main.c)\n\n# Pull in our pico_stdlib which pulls in commonly used features\ntarget_link_libraries("$${CMAKE_PROJECT_NAME}" pico_stdlib)\n\n# Create extra output files map/bin/hex\npico_add_extra_outputs("$${CMAKE_PROJECT_NAME}")\n\n# Add url via pico_set_program_url\npro_auto_set_url("$${CMAKE_PROJECT_NAME}")\n\n'}]

    def setUp(self):
        '''Call before test case.'''
        self.template = WriteTemplate()

    def tearDown(self):
        '''Call after test case.'''
        self.template = None

    def test_write_template(self):
        '''Test write template check.'''
        self.assertEqual(
            self.template.write(
                WriteTemplateTestCase.templates, 'simple_test'
            ),
            True
        )


if __name__ == '__main__':
    unittest.main()
