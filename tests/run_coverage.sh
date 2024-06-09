#!/bin/bash
#
# @brief   armpicom
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2022
# @company None, free software to use 2022
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf fresh_new/ full_simple_new/ new_simple_test/ full_simple/ latest_pro/
python3 -m coverage run -m --source=../armpicom unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html
