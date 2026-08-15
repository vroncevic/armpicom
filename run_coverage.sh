#!/bin/bash
#
# @brief   armpicom
# @version 2.0.3
# @date    Sat Aug 07 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py armpicom
pylint armpicom > armpicom.report
echo "Done"
