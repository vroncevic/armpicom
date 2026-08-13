#!/bin/bash
#
# @brief   armpicom
# @version v1.9.9
# @date    Sat Aug 07 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 ats_coverage.py
pylint armpicom > armpicom.report
echo "Done"
