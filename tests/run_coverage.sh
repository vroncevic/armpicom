#!/bin/bash
#
# @brief   armpicom
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2022
# @company None, free software to use 2022
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov armpicom_coverage.xml armpicom_coverage.json .coverage
rm -rf fresh_new/ full_simple_new/ new_simple_test/ full_simple/ latest_pro/
python3 -m coverage run -m --source=../armpicom unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o armpicom_coverage.xml 
python3 -m coverage json -o armpicom_coverage.json
python3 -m coverage report --format=markdown -m
python3 ats_coverage.py -n armpicom
echo "Done"