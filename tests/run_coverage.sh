#!/bin/bash
#
# @brief   armpicom
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2018
# @company None, free software to use 2018
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf simple_test/
python3 -m coverage run -m --source=../armpicom unittest discover -s ./ -p '*_test.py'
python3 -m coverage html
