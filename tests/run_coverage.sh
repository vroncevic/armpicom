#!/bin/bash
#
# @brief   armpicom
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2018
# @company None, free software to use 2018
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf new_simple_test/ full_simple/ latest/
python3 -m coverage run -m --source=../armpicom unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html
